import sys
from importlib import import_module


def test_dev_libraries():
    import_module("libraries.dev")
    assert "libraries.dev" in sys.modules
