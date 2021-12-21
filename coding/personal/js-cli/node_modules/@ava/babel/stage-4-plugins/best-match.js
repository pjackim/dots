const process = require('process'); // eslint-disable-line node/prefer-global/process

function getClosestVersion() {
	if (!process.versions.v8) {
		// Assume compatibility with Node.js 10.18.0
		return 'v8-6.8';
	}

	const v8 = Number.parseFloat(process.versions.v8);
	if (v8 >= 6.8) {
		return 'v8-6.8';
	}

	return 'v8-6.8';
}

module.exports = require(`./${getClosestVersion()}.json`);
