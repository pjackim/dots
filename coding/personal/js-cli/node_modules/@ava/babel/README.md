# @ava/babel

Translations: [Français](https://github.com/avajs/ava-docs/tree/master/fr_FR/related/babel/README.md)

Adds [Babel 7](https://babeljs.io) support to [AVA](https://avajs.dev) so you can use the latest JavaScript syntax in your tests. We do this by compiling test and helper files using our `@ava/babel/stage-4` preset. We also use a second preset, `@ava/babel/transform-test-files` to enable [enhanced assertion messages](https://github.com/avajs/ava/blob/master/docs/03-assertions.md#enhanced-assertion-messages) and detect improper use of `t.throws()` assertions.

By default our Babel pipeline is applied to test and helper files ending in `.cjs` and `.js`. If your project uses Babel then we'll automatically compile these files using your project's Babel configuration. The `@ava/babel/transform-helper-files` preset is applied first, and the `@ava/babel/stage-4` last.

If you are using Babel for your source files then you must also [configure source compilation](#compile-sources).

## Enabling Babel support

Add this package to your project:

```console
npm install --save-dev @ava/babel
```

Then, enable Babel support either in `package.json` or `ava.config.*`:

**`package.json`:**

```json
{
	"ava": {
		"babel": true
	}
}
```

## Customize how AVA compiles your test files

You can override the default Babel configuration AVA uses for test file compilation in `package.json` or `ava.config.*`. For example, the configuration below adds support for JSX syntax and [preset-env](https://babeljs.io/docs/en/babel-preset-env).

**`package.json`:**

```json
{
	"ava": {
		"babel": {
			"extensions": [
				"js",
				"jsx"
			],
			"testOptions": {
				"plugins": ["@babel/plugin-syntax-jsx"],
				"presets": ["@babel/preset-env"]
			}
		}
	}
}
```

All [Babel options] are allowed inside the `testOptions` object.

## Compile additional files

By default, only test files are compiled. You can compile additional files as tests by providing glob patterns:

**`package.json`:**

```json
{
	"ava": {
		"babel": {
			"compileAsTests": ["test/helpers/**/*"]
		}
	}
}
```

## Reset AVA's cache

AVA caches the compiled test and helper files. It automatically recompiles these files when you change them. AVA tries its best to detect changes to your Babel configuration files, plugins and presets. If it seems like your latest Babel configuration isn't being applied, however, you can reset AVA's cache:

```console
$ npx ava reset-cache
```

## Add additional extensions

You can configure AVA to recognize additional file extensions and compile those test & helper files using Babel.

**`package.json`:**

```json
{
	"ava": {
		"babel": {
			"extensions": [
				"js",
				"jsx"
			]
		}
	}
}
```

See also AVA's [`extensions` option](https://github.com/avajs/ava/blob/master/docs/06-configuration.md#options).

## Make AVA skip your project's Babel options

You may not want AVA to use your project's Babel options, for example if your project is relying on Babel 6. Set the `babelrc` and `configFile` options to `false`.

**`package.json`:**

```json
{
	"ava": {
		"babel": {
			"testOptions": {
				"babelrc": false,
				"configFile": false
			}
		}
	}
}
```

## Disable AVA's stage-4 preset

You can disable AVA's stage-4 preset.

**`package.json`:**

```json
{
	"ava": {
		"babel": {
			"testOptions": {
				"presets": [
					["module:@ava/babel/stage-4", false]
				]
			}
		}
	}
}
```

Note that this *does not* stop AVA from compiling your test files using Babel.

If you want, you can disable the preset in your project's Babel configuration.

## Preserve ES module syntax

By default AVA's stage-4 preset will convert ES module syntax to CommonJS. This can be disabled.

**`package.json`:**

```json
{
	"ava": {
		"babel": {
			"testOptions": {
				"presets": [
					["module:@ava/babel/stage-4", {"modules": false}]
				]
			}
		}
	}
}
```

You'll have to use the [`esm`](https://github.com/standard-things/esm) module so that AVA can still load your test files. [See our recipe for details](https://github.com/avajs/ava/blob/master/docs/recipes/es-modules.md).

## Disable enhancements

By default, AVA will compile test and helper files with some additional enhancements. Disable this by setting `compileEnhancements` to `false`:

**`package.json`:**

```json
{
	"ava": {
		"babel": {
			"compileEnhancements": false
		}
	}
}
```

## Use Babel polyfills

AVA lets you write your tests using new JavaScript syntax, even on Node.js versions that otherwise wouldn't support it. However, it doesn't add or modify built-ins of your current environment. Using AVA would, for example, not provide modern features such as `Object.fromEntries()` to an underlying Node.js 10 environment.

By loading [Babel's `polyfill` module](https://babeljs.io/docs/usage/polyfill/) you can opt in to these features. Note that this will modify the environment, which may influence how your program behaves.

You can enable the `polyfill` module by adding it to AVA's `require` option.

**`package.json`:**

```json
{
	"ava": {
		"require": [
			"@babel/polyfill"
		]
	}
}
```

You'll need to install `@babel/polyfill` yourself.

## Compile sources

AVA does not currently compile source files. You'll have to load [Babel's `register` module](http://babeljs.io/docs/usage/require/), which will compile source files as needed.

You can enable the `register` module by adding it to AVA's `require` option.

**`package.json`:**

```json
{
	"ava": {
		"require": [
			"@babel/register"
		]
	}
}
```

You'll need to install `@babel/register` yourself.

`@babel/register` will *also* process your test and helper files. For most use cases this is unnecessary. If you create a new file that requires `@babel/register` you can tell it which file paths to ignore. For instance in your `test` directory create `_register.js`:

```js
// test/_register.js:
require('@babel/register')({
	// These patterns are relative to the project directory (where the `package.json` file lives):
	ignore: ['node_modules/*', 'test/*']
});
```

Now instead of requiring `@babel/register`, require `./test/_register` instead.

**`package.json`:**

```json
{
	"ava": {
		"require": [
			"./test/_register.js"
		]
	}
}
```

Note that loading `@babel/register` in every worker process has a non-trivial performance cost. If you have lots of test files, you may want to consider using a build step to compile your sources *before* running your tests. This isn't ideal, since it complicates using AVA's watch mode, so we recommend using `@babel/register` until the performance penalty becomes too great. Setting up a precompilation step is out of scope for this document, but we recommend you check out one of the many [build systems that support Babel](http://babeljs.io/docs/setup/). There is an [issue](https://github.com/avajs/ava/issues/577) discussing ways we could make this experience better.

## Webpack aliases

[Webpack aliases](https://webpack.js.org/configuration/resolve/#resolve-alias) can be used to provide a shortcut to deeply nested or otherwise inconvenient paths. If you already use aliases in your source files, you'll need to make sure you can use the same aliases in your test files.

Install `babel-plugin-webpack-alias-7` as a dev-dependency. Then add the plugin to AVA's Babel config:

`package.json`:

```json
{
	"ava": {
		"babel": {
			"testOptions": {
				"plugins": [
					[
						"babel-plugin-webpack-alias-7",
						{
							"config": "./path/to/webpack.config.test.js"
						}
					]
				]
			}
		}
	}
}
```

## `@ava/babel/stage-4`

Aspires to bring [finished ECMAScript proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md) to AVA's test and helper files.

Efficiently applies the minimum of transforms to run the latest JavaScript syntax on Node.js 10 and 12.

Built-ins are not added or extended, so features like Proxies, `Array.prototype.includes` or `String.prototype.padStart` will only be available if the Node.js version running the tests supports it. Consult [node.green] for details.

Sometimes a particular feature is *mostly* implemented in Node.js. In that case transforms are not applied.

Not all proposals can be supported via Babel transforms, see below for details. Babel may require "syntax" plugins in order to parse certain files. These plugins should be applied explicitly since this preset may not include them. If you use AVA's Babel compilation this is already taken care of.

### Supported proposals

| Proposal                                                                 | Supported
| ------------------------------------------------------------------------ | ---------
| [`Array.prototype.includes`][array-includes]                             | No
| [`Object.values`/`Object.entries`][object-values-entries]                | No
| [String padding][string-padding]                                         | No
| [`Object.getOwnPropertyDescriptors`][object-gopds]                       | No
| [Trailing commas in function parameter lists and calls][function-commas] | Yes
| [Shared memory and atomics][atomics]                                     | No
| [Lifting template literal restriction][template-literal-lift]            | No
| [`s` (`dotAll`) flag for regular expressions][dot-all]                   | Yes
| [RegExp named capture groups][named-groups]                              | No
| [RegExp Lookbehind Assertions][lookbehind]                               | No
| [RegExp Unicode Property Escapes][unicode-escapes]                       | No
| [`Promise.prototype.finally`][finally]                                   | No
| [Asynchronous Iteration][async-iteration]                                | Partially<sup>†</sup>
| [Optional `catch` binding][optional-catch]                               | Yes
| [JSON superset][json-superset]                                           | No
| [`Symbol.prototype.description`][symbol-description]                     | No
| [`Function.prototype.toString` revision][function-tostring-revision]     | No
| [`Object.fromEntries`][object-fromentries]                               | No
| [Well-formed `JSON.stringify`][well-formed-stringify]                    | No
| [`String.prototype.{trimStart,trimEnd}`][string-left-right-trim]         | No
| [`Array.prototype.{flat,flatMap}`][flatmap]                              | No
| [`String.prototype.matchAll`][string-matchall]                           | No
| [`import()`][dynamic-import]                                             | Yes
| [`Promise.allSettled`][promise-allsettled]                               | No
| [Optional Chaining][chaining]                                            | Yes
| [Nullish coalescing Operator][nullish-coalescing]                        | Yes

† [`@babel/plugin-proposal-async-generator-functions`](https://www.npmjs.com/package/@babel/plugin-proposal-async-generator-functions) relies on `Symbol.asyncIterator`, which AVA does not polyfill for you.

[array-includes]: https://github.com/tc39/Array.prototype.includes
[async-iteration]: https://github.com/tc39/proposal-async-iteration
[atomics]: https://github.com/tc39/ecmascript_sharedmem
[Babel options]: https://babeljs.io/docs/en/options
[chaining]: https://github.com/tc39/proposal-optional-chaining
[dot-all]: https://github.com/tc39/proposal-regexp-dotall-flag
[dynamic-import]: https://github.com/tc39/proposal-dynamic-import
[finally]: https://github.com/tc39/proposal-promise-finally
[flatmap]: https://github.com/tc39/proposal-flatMap
[function-commas]: https://github.com/tc39/proposal-trailing-function-commas
[function-tostring-revision]: https://github.com/tc39/Function-prototype-toString-revision
[json-superset]: https://github.com/tc39/proposal-json-superset
[lookbehind]: https://github.com/tc39/proposal-regexp-lookbehind
[named-groups]: https://github.com/tc39/proposal-regexp-named-groups
[node.green]: http://node.green
[nullish-coalescing]: https://github.com/tc39/proposal-nullish-coalescing
[object-fromentries]: https://github.com/tc39/proposal-object-from-entries
[object-gopds]: https://github.com/ljharb/proposal-object-getownpropertydescriptors
[object-values-entries]: https://github.com/tc39/proposal-object-values-entries
[optional-catch]: https://github.com/tc39/proposal-optional-catch-binding
[promise-allsettled]: https://github.com/tc39/proposal-promise-allSettled
[string-left-right-trim]: https://github.com/tc39/proposal-string-left-right-trim
[string-matchall]: https://github.com/tc39/String.prototype.matchAll
[string-padding]: https://github.com/tc39/proposal-string-pad-start-end
[symbol-description]: https://github.com/tc39/proposal-Symbol-description
[template-literal-lift]: https://github.com/tc39/proposal-template-literal-revision
[unicode-escapes]: https://github.com/tc39/proposal-regexp-unicode-property-escapes
[well-formed-stringify]: https://github.com/tc39/proposal-well-formed-stringify
