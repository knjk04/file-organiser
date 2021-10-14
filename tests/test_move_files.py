import builtins
from unittest import mock

from src.move_files import apply_recursively


def test_apply_recursively_is_true():
    with mock.patch.object(builtins, 'input', lambda: 'y'):
        assert apply_recursively()


def test_apply_recursively_is_false():
    with mock.patch.object(builtins, 'input', lambda: 'n'):
        assert not apply_recursively()
