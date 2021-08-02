import unixpath
import os.path


def check(fn, *args, **kws):
    assert getattr(os.path, fn)(*args, **kws) == getattr(unixpath, fn)(*args, **kws)


def test_path():
    check('join', '.', '/foo')
    for fn in ['isabs', 'split', 'dirname', 'basename', 'normpath']:
        check(fn, '/')
        check(fn, '//')
        check(fn, '///')
        check(fn, '////')
        check(fn, './')
        check(fn, '/abc')
        check(fn, '/abc/')
        check(fn, '/abc//')
    assert '/' == unixpath.dirname('/')
    assert '//' == unixpath.dirname('//')
    assert '/' == unixpath.normpath('///')
    assert '/' == unixpath.normpath('////')
    assert '///' == unixpath.dirname('///')
    assert '////' == unixpath.dirname('////')
    assert 'a/b/../c' == unixpath.join('a', 'b', '..', 'c')
    assert 'a/c' == unixpath.normpath(unixpath.join('a', 'b', '..', 'c'))
    assert 'a/b' == unixpath.dirname('a/b/c')
    assert 'c' == unixpath.basename('a/b/c')
    assert '' == unixpath.basename('a/b/c/')
    assert '' == unixpath.basename('')
    assert '.' == unixpath.normpath('')
    assert unixpath.isabs('/foo')
    assert not unixpath.isabs('./foo')
