# require-precompiled

Modifies `require()` so you can load precompiled module sources.

## Install

```
$ npm install --save require-precompiled
```

## Usage

```js
const installPrecompiler = require('require-precompiled');
const cache = require('my-cache-implementation');

installPrecompiler(filename => {
	if (cache.hasEntryFor(filename)) {
		return cache.getPrecompiledCode(filename);
	}
	// fall through to underlying extension chain
	return null;
});

// any module required from this point on will be checked against the cache
const foo = require('some-module');
```

## API

```ts
function installPrecompiler(
	loadSource: (filename: string) => string | null,
	ext = '.js',
): void
```

The `loadSource()` function should return a source string when a precompiled source is available. Return `null` to fall back to Node.js' default behavior.

By default the precompiler is installed for `.js` files. You can specify alternative extensions by providing the second argument:

```js
installPrecompiler(filename => {
	// ...
}, '.cjs')
```

## License

MIT © [James Talmage](https://github.com/jamestalmage)
