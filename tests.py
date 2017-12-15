from setuptools_scm import format_version
from setuptools_scm_about import parse


def test_parse_with_valid_about(tmpdir):
    package = tmpdir.mkdir('myproject')
    package.join('__init__.py').write('')
    package.join('__about__.py').write('__version__ = "1.0"')
    assert format_version(parse(str(tmpdir))) == '1.0.dev0+unknown'


def test_parse_with_invalid_about(tmpdir):
    package = tmpdir.mkdir('myproject')
    package.join('__init__.py').write('')
    package.join('__about__.py').write('foo = "1.0"')
    assert parse(str(tmpdir)) is None


def test_parse_without_about(tmpdir):
    package = tmpdir.mkdir('myproject')
    package.join('__init__.py').write('')
    assert parse(str(tmpdir)) is None
