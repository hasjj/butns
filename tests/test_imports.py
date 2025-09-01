import importlib


def test_import_butns():
    m = importlib.import_module("butns")
    assert hasattr(m, "__version__")
