.. image:: https://travis-ci.org/GreatFruitOmsk/setuptools_scm_about.svg?branch=master
    :target: https://travis-ci.org/GreatFruitOmsk/setuptools_scm_about
    :alt: Travis
.. image:: https://ci.appveyor.com/api/projects/status/abqxn2vbk5k2styb/branch/master?svg=true
    :target: https://ci.appveyor.com/project/GreatFruitOmsk/setuptools_scm_about-app
    :alt: AppVeyor
.. image:: https://codecov.io/gh/GreatFruitOmsk/setuptools_scm_about/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/GreatFruitOmsk/setuptools_scm_about
    :alt: Coverage
.. image:: https://pyup.io/repos/github/GreatFruitOmsk/setuptools_scm_about/shield.svg
    :target: https://pyup.io/repos/github/GreatFruitOmsk/setuptools_scm_about/
    :alt: Updates
.. image:: https://img.shields.io/pypi/v/setuptools_scm_about.svg
    :target: https://pypi.python.org/pypi/setuptools_scm_about
    :alt: PyPI

This is a `setuptools_scm <https://pypi.python.org/pypi/setuptools_scm>`_ plugin
that adds support for __about__.py files.

If version cannot be resolved via SCM, the fallback registered by this plugin will be called.
It will try to find the ``__about__.py`` file (using the ``**/__about__.py`` glob pattern) that defines
the ``__version__`` variable.

Since there is no SCM metadata available, package will return `VERSION.dev0+unknown` where VERSION is a version
from ``__about__.py``.

Usage
-----

Add ``'setuptools_scm_about'`` to the ``setup_requires`` parameter in your
project's ``setup.py`` file:

.. code:: python

    setup(
        ...,
        use_scm_version={
            'write_to': 'myproject/_version.py'
        },
        setup_requires=['setuptools_scm', 'setuptools_scm_about'],
        ...,
    )

Define ``__version__`` in ``myproject/__about__.py``:

.. code:: python

    __version__ = 1.0

Import ``__version__`` in ``myproject/__init__.py`` for external access:

.. code:: python

    try:
        from ._version import version as __version__
    except ImportError:
        from .__about__ import __version__
