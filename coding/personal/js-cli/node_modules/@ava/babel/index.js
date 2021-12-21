const fs = require('fs');
const path = require('path');
const installPrecompiler = require('@ava/require-precompiled');
const babel = require('@babel/core');
const {default: generate} = require('@babel/generator');
const concordance = require('concordance');
const convertSourceMap = require('convert-source-map');
const dotProp = require('dot-prop');
const escapeStringRegexp = require('escape-string-regexp');
const findUp = require('find-up');
const {isPlainObject} = require('is-plain-object');
const md5Hex = require('md5-hex');
const packageHash = require('package-hash');
const pkgConf = require('pkg-conf');
const sourceMapSupport = require('source-map-support');
const stripBomBuf = require('strip-bom-buf');
const writeFileAtomic = require('write-file-atomic');
const pkg = require('./package.json');

const computeStatement = node => generate(node).code;
const getNode = (ast, path) => dotProp.get(ast, path.replace(/\//g, '.'));

function getSourceMap(filePath, code) {
	let sourceMap = convertSourceMap.fromSource(code);

	if (!sourceMap) {
		const dirPath = path.dirname(filePath);
		sourceMap = convertSourceMap.fromMapFileSource(code, dirPath);
	}

	return sourceMap ? sourceMap.toObject() : undefined;
}

function enableParserPlugins(api) {
	api.assertVersion(7);

	return {
		name: 'ava-babel-pipeline-enable-parser-plugins',
		manipulateOptions(_, parserOptions) {
			parserOptions.plugins.push(
				'bigInt',
				'classPrivateProperties',
				'classProperties',
				'numericSeparator'
			);
		}
	};
}

// Compare actual values rather than file paths, which should be
// more reliable.
function makeValueChecker(ref) {
	const expected = require(ref);
	return ({value}) => value === expected || value === expected.default;
}

// Resolved paths are used to create the config item, rather than the plugin
// function itself, so Babel can print better error messages.
// See <https://github.com/babel/babel/issues/7921>.
function createConfigItem(ref, type, options = {}) {
	return babel.createConfigItem([require.resolve(ref), options], {type});
}

// Assume the stage-4 preset is wanted if there are `babelOptions`, but there is
// no declaration of a stage-` preset that comes with `false` for its options.
//
// Ideally we'd detect the stage-4 preset anywhere in the configuration
// hierarchy, but Babel's loadPartialConfig() does not return disabled presets.
// See <https://github.com/babel/babel/issues/7920>.
function wantsStage4(babelOptions, projectDir) {
	if (!babelOptions) {
		return false;
	}

	if (!babelOptions.presets) {
		return true;
	}

	const stage4 = require('./stage-4.js');
	return babelOptions.presets.every(array => {
		if (!Array.isArray(array)) {
			return true; // There aren't any preset options.
		}

		const [ref, options] = array;
		// Require the preset to handle any aliasing that may be taking place.
		const resolved = require(babel.resolvePreset(ref, projectDir));
		return resolved !== stage4 || options !== false;
	});
}

function hashPartialConfig({babelrc, config, options: {plugins, presets}}, projectDir, pluginAndPresetHashes) {
	const inputs = [];
	if (babelrc) {
		inputs.push(babelrc);

		const filename = path.basename(babelrc);
		if (filename === 'package.json') {
			inputs.push(JSON.stringify(pkgConf.sync('babel', {cwd: path.dirname(filename)})));
		} else {
			inputs.push(stripBomBuf(fs.readFileSync(babelrc)));
		}
	}

	if (config) {
		inputs.push(config, stripBomBuf(fs.readFileSync(config)));
	}

	for (const item of [...plugins, ...presets]) {
		if (!item.file) {
			continue;
		}

		const {file: {resolved: filename}} = item;
		if (pluginAndPresetHashes.has(filename)) {
			inputs.push(pluginAndPresetHashes.get(filename));
			continue;
		}

		const [firstComponent] = path.relative(projectDir, filename).split(path.sep);
		const hash = firstComponent === 'node_modules' ? packageHash.sync(findUp.sync('package.json', {cwd: path.dirname(filename)})) : md5Hex(stripBomBuf(fs.readFileSync(filename)));

		pluginAndPresetHashes.set(filename, hash);
		inputs.push(hash);
	}

	return md5Hex(inputs);
}

function createCompileFn({babelOptions, cacheDir, compileEnhancements, projectDir}) {
	// Note that Babel ignores empty string values, even for NODE_ENV. Here
	// default to 'test' unless NODE_ENV is defined, in which case fall back to
	// Babel's default of 'development' if it's empty.
	const envName = process.env.BABEL_ENV || ('NODE_ENV' in process.env ? process.env.NODE_ENV : 'test') || 'development';

	// Prepare inputs for caching seeds. Compute a seed based on the Node.js
	// version and the project directory. Dependency hashes may vary based on the
	// Node.js version, e.g. with the stage-4 Babel preset. Certain plugins
	// and presets are provided as absolute paths, which wouldn't necessarily
	// be valid if the project directory changes. Also include `envName`, so
	// options can be cached even if users change BABEL_ENV or NODE_ENV between
	// runs.
	const seedInputs = [
		process.versions.node,
		packageHash.sync(require.resolve('./package.json')),
		projectDir,
		envName,
		concordance.serialize(concordance.describe(babelOptions))
	];

	const partialCacheKey = md5Hex(seedInputs);
	const pluginAndPresetHashes = new Map();

	const ensureStage4 = wantsStage4(babelOptions, projectDir);
	const containsStage4 = makeValueChecker('./stage-4');
	const containsTransformTestFiles = makeValueChecker('./transform-test-files');

	const loadOptions = filename => {
		const partialConfig = babel.loadPartialConfig({
			babelrc: false,
			babelrcRoots: [projectDir],
			configFile: false,
			sourceMaps: true,
			...babelOptions,
			cwd: projectDir,
			envName,
			filename,
			sourceFileName: path.relative(projectDir, filename),
			sourceRoot: projectDir
		});

		if (!partialConfig) {
			return {hash: '', options: null};
		}

		const {options: partialOptions} = partialConfig;
		partialOptions.plugins.push(enableParserPlugins);

		if (ensureStage4 && !partialOptions.presets.some(preset => containsStage4(preset))) {
			// Apply last.
			partialOptions.presets.unshift(createConfigItem('./stage-4', 'preset'));
		}

		if (compileEnhancements && !partialOptions.presets.some(preset => containsTransformTestFiles(preset))) {
			// Apply first.
			partialOptions.presets.push(createConfigItem('./transform-test-files', 'preset', {powerAssert: true}));
		}

		const hash = hashPartialConfig(partialConfig, projectDir, pluginAndPresetHashes);
		const options = babel.loadOptions(partialOptions);
		return {hash, options};
	};

	return filename => {
		const {hash: optionsHash, options} = loadOptions(filename);
		if (!options) {
			return null;
		}

		const contents = stripBomBuf(fs.readFileSync(filename));
		const ext = path.extname(filename);
		const hash = md5Hex([partialCacheKey, contents, optionsHash]);
		const cachePath = path.join(cacheDir, `${hash}${ext}`);

		if (fs.existsSync(cachePath)) {
			return cachePath;
		}

		const inputCode = contents.toString('utf8');
		const inputSourceMap = getSourceMap(filename, inputCode);
		if (inputSourceMap) {
			options.inputSourceMap = inputSourceMap;
		}

		const {code, map} = babel.transformSync(inputCode, options);

		if (map) {
			// Save source map
			const mapPath = `${cachePath}.map`;
			writeFileAtomic.sync(mapPath, JSON.stringify(map));

			// Append source map comment to transformed code so that other libraries
			// (like nyc) can find the source map.
			const comment = convertSourceMap.generateMapFileComment(mapPath);
			writeFileAtomic.sync(cachePath, `${code}\n${comment}`);
		} else {
			writeFileAtomic.sync(cachePath, code);
		}

		return cachePath;
	};
}

function installSourceMapSupport(state) {
	sourceMapSupport.install({
		environment: 'node',
		handleUncaughtExceptions: false,
		retrieveSourceMap(url) {
			const precompiled = state[url];
			if (!precompiled) {
				return null;
			}

			try {
				const map = fs.readFileSync(`${precompiled}.map`, 'utf8');
				return {url, map};
			} catch (error) {
				if (error.code === 'ENOENT') {
					return null;
				}

				throw error;
			}
		}
	});
}

function isValidExtensions(extensions) {
	return Array.isArray(extensions) &&
		extensions.length > 0 &&
		extensions.every(ext => typeof ext === 'string' && ext !== '') &&
		new Set(extensions).size === extensions.length;
}

function isValidPatterns(patterns) {
	return Array.isArray(patterns) && patterns.length > 0 && patterns.every(pattern => typeof pattern === 'string');
}

module.exports = ({negotiateProtocol}) => {
	const protocol = negotiateProtocol(['ava-3.2'], {version: pkg.version});
	if (protocol === null) {
		return;
	}

	return {
		main({config}) {
			let valid = false;
			if (config === true) {
				valid = true;
			} else if (isPlainObject(config)) {
				const keys = Object.keys(config);
				if (keys.length === 0) {
					valid = true;
				} else if (keys.every(key => key === 'compileAsTests' || key === 'compileEnhancements' || key === 'extensions' || key === 'testOptions')) {
					valid =
						(config.compileAsTests === undefined || isValidPatterns(config.compileAsTests)) &&
						(config.compileEnhancements === undefined || typeof config.compileEnhancements === 'boolean') &&
						(config.extensions === undefined || isValidExtensions(config.extensions)) &&
						(config.testOptions === undefined || config.testOptions === false || isPlainObject(config.testOptions));
				}
			}

			if (!valid) {
				throw new Error(`Unexpected Babel configuration for AVA. See https://github.com/avajs/babel/blob/v${pkg.version}/README.md for allowed values.`);
			}

			const {
				compileAsTests = [],
				compileEnhancements = true,
				extensions = ['cjs', 'js'],
				testOptions
			} = config;

			const additionalPatterns = protocol.normalizeGlobPatterns(compileAsTests);
			const testFileExtension = new RegExp(`\\.(${extensions.map(ext => escapeStringRegexp(ext)).join('|')})$`);

			let compileFile;
			return {
				async compile({cacheDir, files}) {
					if (!compileFile) {
						compileFile = createCompileFn({
							babelOptions: testOptions === false ? false : {babelrc: true, configFile: true, ...testOptions},
							cacheDir,
							compileEnhancements,
							projectDir: protocol.projectDir
						});
					}

					const additionalFiles = additionalPatterns.length > 0 ? await protocol.findFiles({extensions, patterns: additionalPatterns}) : [];

					let compiledAnything = false;
					const lookup = {};
					for (const file of [...files, ...additionalFiles]) {
						if (!testFileExtension.test(file)) {
							continue;
						}

						try {
							lookup[file] = compileFile(file);
							compiledAnything = true;
						} catch (error) {
							throw Object.assign(error, {file});
						}
					}

					if (!compiledAnything) {
						return null;
					}

					return {
						extensions: [...extensions],
						lookup
					};
				},

				get extensions() {
					return [...extensions];
				},

				ignoreChange() {
					return false;
				},

				resolveTestFile(testFile) {
					return testFile;
				},

				updateGlobs(globs) {
					return globs;
				}
			};
		},

		worker({extensionsToLoadAsModules, state}) {
			installSourceMapSupport(state.lookup);

			const precompile = filename => Reflect.has(state.lookup, filename) ? fs.readFileSync(state.lookup[filename], 'utf8') : null;
			for (const ext of state.extensions) {
				installPrecompiler(precompile, `.${ext}`);
			}

			return {
				canLoad(ref) {
					return Reflect.has(state.lookup, ref);
				},

				async load(ref, {requireFn}) {
					for (const extension of extensionsToLoadAsModules) {
						if (ref.endsWith(`.${extension}`)) {
							throw new Error('@ava/babel cannot yet load ESM files');
						}
					}

					// Let the precompiler hook resolve the compiled source.
					return requireFn(ref);
				},

				powerAssert: {
					empower: require('empower-core'),
					format(context, format) {
						const ast = JSON.parse(context.source.ast);
						const args = context.args[0].events;
						return args
							.map(arg => {
								const node = getNode(ast, arg.espath);
								const statement = computeStatement(node);
								const formatted = format(arg.value);
								return [statement, formatted];
							})
							.reverse();
					}
				}
			};
		}
	};
};
