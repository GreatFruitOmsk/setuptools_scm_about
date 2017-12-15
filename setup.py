import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(base_dir, 'setuptools_scm_about', '__about__.py')) as f:
    exec(f.read(), about)

REQUIREMENTS = [
    'setuptools_scm>=1.10.0'
]

TEST_REQUIREMENTS = [
    'pytest'
]

CI_REQUIREMENTS = TEST_REQUIREMENTS + [
    'codecov',
    'docutils',
    'flake8',
    'pygments',
    'pytest-cov'
]


setup(
    version=about['__version__'],
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    extras_require={
        'tests': TEST_REQUIREMENTS,
        'ci': CI_REQUIREMENTS
    },
    entry_points={
        'setuptools_scm.parse_scm_fallback': [
            '. = setuptools_scm_about:parse'
        ]
    },
    cmdclass={'test': PyTest}
)
