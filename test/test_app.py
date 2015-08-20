from app.impl import baz


pytest_plugins = "pytester"


def test_baz():
    assert baz() == "baz"


def test_foo(testdir):

    testdir.makepyfile("""
        from app.impl import foo

        def test_foo():
            assert foo() == "foo"
    """)

    result = testdir.runpytest()

    assert result.ret == 0


def test_bar(testdir):

    testdir.makepyfile("""
        from app.impl import bar

        def test_bar():
            assert bar() == "bar"
    """)

    result = testdir.runpytest()

    assert result.ret == 0
