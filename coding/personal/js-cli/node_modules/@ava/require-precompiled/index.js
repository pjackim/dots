'use strict';
module.exports = install;

/* eslint-disable node/no-deprecated-api, eslint-comments/disable-enable-pair */

// Save reference before a new handler is installed.
const {'.js': defaultHandler} = require.extensions;

function install(precompile, ext = '.js', extensions = require.extensions) {
	const {[ext]: fallbackHandler = defaultHandler} = extensions;

	extensions[ext] = function (module, filename) {
		const source = precompile(filename);
		if (source === null) {
			Reflect.apply(fallbackHandler, extensions, [module, filename]);
		} else {
			module._compile(source, filename);
		}
	};
}
