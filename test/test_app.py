import subprocess

from app.impl import baz

import os
os.environ['COVERAGE_PROCESS_START'] = ".coveragerc"

import pytest
import textwrap


pytest_plugins = "pytester"


@pytest.fixture
def sitecustomize(tmpdir):
    fh = tmpdir.join("sitecustomize.py")
    fh.write("import coverage; coverage.process_startup()")
    return fh


@pytest.fixture
def testfile(tmpdir, sitecustomize):

    src = textwrap.dedent("""
        from app.impl import foo, bar

        def test_foo():
            assert foo() == "foo"

        def test_bar():
            assert bar() == "bar"
        """)
    fh = tmpdir.join("subproc_test_app.py")
    fh.write(src)
    return fh


def test_baz():
    assert baz() == "baz"


#@pytest.mark.usefixtures('testdir')
def test_via_subproc(tmpdir, testfile):
    import os
    os.environ['PYTHONPATH'] = tmpdir.strpath
    proc = subprocess.Popen(["py.test", testfile.strpath, "-v"])
    proc.wait()

