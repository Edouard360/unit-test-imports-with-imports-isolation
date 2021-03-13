import sys
from unittest import mock
from importlib import import_module


def test_dev_libraries_not_imported_in_package_init():
    with mock.patch.dict(sys.modules):
        import_module("my_package")
        assert "libraries.dev" not in sys.modules
