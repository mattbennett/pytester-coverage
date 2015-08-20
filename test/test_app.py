import subprocess

from app.impl import baz

import os
os.environ['COVERAGE_PROCESS_START'] = ".coveragerc"

import pytest
import textwrap


pytest_plugins = "pytester"


SITECUSTOMIZE = "import coverage; coverage.process_startup()"

COVERAGERC = """
[run]
branch = true
source = app

[report]
show_missing = true
"""

TEST = textwrap.dedent("""
    from app.impl import foo, bar

    def test_foo():
        assert foo() == "foo"

    def test_bar():
        assert bar() == "bar"
    """)


@pytest.fixture
def sitecustomize(tmpdir):
    fh = tmpdir.join("sitecustomize.py")
    fh.write(SITECUSTOMIZE)
    return fh


@pytest.fixture
def testfile(tmpdir, sitecustomize):
    fh = tmpdir.join("subproc_test_app.py")
    fh.write(TEST)
    return fh


def test_baz():
    assert baz() == "baz"


@pytest.mark.subproc
def test_via_subproc(tmpdir, testfile):
    import os
    os.environ['PYTHONPATH'] = tmpdir.strpath
    proc = subprocess.Popen(["py.test", testfile.strpath, "-v"])
    proc.wait()


@pytest.yield_fixture
def testdir(request):
    testdir = request.getfuncargvalue("testdir")
    testdir.makepyfile(sitecustomize=SITECUSTOMIZE)

    fh = testdir.tmpdir.join(".coveragerc")
    fh.write(COVERAGERC)

    yield testdir

    dst = os.path.join(testdir._olddir.strpath, '.coverage.captured')
    os.rename(os.path.join(testdir.tmpdir.strpath, '.coverage'), dst)


@pytest.mark.pytest
def test_via_pytest(testdir):

    testdir.makepyfile(TEST)
    result = testdir.runpytest()

    assert result.ret == 0
