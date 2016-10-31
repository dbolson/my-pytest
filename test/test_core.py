import conftest
import mypytest.core

def test_main_fn():
    assert mypytest.core.main_fn() == [1, 2]
