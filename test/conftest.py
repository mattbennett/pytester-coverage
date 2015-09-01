import os

import pytest


@pytest.fixture
def testdir(testdir):

    rc_path = os.path.join(
        os.path.dirname(__file__), os.pardir, '.coveragerc'
    )
    os.environ['COVERAGE_PROCESS_START'] = os.path.normpath(rc_path)

    testdir.makepyfile(sitecustomize="""
        import coverage; coverage.process_startup()
    """)

    return testdir
