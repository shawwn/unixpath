# unixpath

> unix-style path processing functions


## Why?

My goal was to provide `posixpath` path processing functions in pure Python (e.g. `normpath`, `join`, `split`, etc) *minus* any functions that rely on any kind of "filesystem" concept (`stat`, etc).

Basically, this is a "minimum viable unix path processing framework." Path processing functions are useful for e.g. ML libraries that want to use unix-style paths to refer to model variables.

(Honestly `unixpath` is kind of pointless. Its functions are copy-pasted from `posixpath`, so why not just `import posixpath` and not worry about the extra dependency on `unixpath`? Answer: because I was curious how Python implemented their unix path processing functions, so I made this library as a learning exercise.)


## Install

```
python3 -m pip install -U unixpath
```

## Usage

```py
import unixpath
unixpath.join('a', 'b') # 'a/b'
unixpath.join('a', 'b', '..', 'c') # 'a/b/../c'
unixpath.normpath('a/b/../c') # 'a/c'
```

## License

MIT

## Contact

A library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!

My Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It's the best way to reach me, and I'm always happy to hear from you.

- Twitter: [@theshawwn](https://twitter.com/theshawwn)
- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)
- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)
- Website: [shawwn.com](https://www.shawwn.com)

