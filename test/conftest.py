import os

import pytest


@pytest.yield_fixture
def testdir(testdir):

    os.environ['COVERAGE_PROCESS_START'] = ".coveragerc"

    testdir.makepyfile(sitecustomize="""
        import coverage; coverage.process_startup()
    """)

    fh = testdir.tmpdir.join(".coveragerc")
    project_root = os.path.join(os.path.dirname(__file__), os.path.pardir)
    with open(os.path.join(project_root, '.coveragerc')) as rc:
        fh.write(rc.read())

    yield testdir

    dst = os.path.join(testdir._olddir.strpath, '.coverage.captured')
    os.rename(os.path.join(testdir.tmpdir.strpath, '.coverage'), dst)
