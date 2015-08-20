import os

import pytest


@pytest.fixture
def coveragerc():
    project_root = os.path.join(os.path.dirname(__file__), os.path.pardir)
    with open(os.path.join(project_root, '.coveragerc')) as rc:
        return rc.read()


@pytest.yield_fixture
def testdir(testdir, coveragerc):

    os.environ['COVERAGE_PROCESS_START'] = ".coveragerc"

    testdir.makepyfile(sitecustomize="""
        import coverage; coverage.process_startup()
    """)

    fh = testdir.tmpdir.join(".coveragerc")
    fh.write(coveragerc)

    yield testdir

    dst = os.path.join(testdir._olddir.strpath, '.coverage.captured')
    os.rename(os.path.join(testdir.tmpdir.strpath, '.coverage'), dst)
