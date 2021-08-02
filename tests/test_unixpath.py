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
