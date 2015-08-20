from app.impl import baz


pytest_plugins = "pytester"


def test_baz():
    assert baz() == "baz"


def test_foo_bar(testdir):

    testdir.makepyfile("""
        from app.impl import foo, bar

        def test_foo():
            assert foo() == "foo"

        def test_bar():
            assert bar() == "bar"
    """)

    result = testdir.runpytest()

    assert result.ret == 0
