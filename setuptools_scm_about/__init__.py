import os.path

from .__about__ import __version__


def parse(root):
    import glob
    from setuptools_scm.utils import trace
    from setuptools_scm.version import meta

    for p in glob.iglob(os.path.join(root, '**/__about__.py')):
        try:
            about = {}
            with open(p) as f:
                exec(f.read(), about)
            return meta('{0}.dev0+unknown'.format(about["__version__"]), preformatted=True)
        except:
            trace('no __version__ in', p)
            continue
    else:
        return None
