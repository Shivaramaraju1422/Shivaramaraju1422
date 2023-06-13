"""
Tests for ex_0_3.py
"""
from src import ex_0_3


def test_format_name_exists():
    # Assert that format_name exists and is a function (callable)
    assert hasattr(ex_0_3, 'format_name')
    assert hasattr(ex_0_3.format_name, '__call__')


def test___format_name___correct_return():
    first_name = 'addison'
    last_name = 'bellamy'
    expected = 'Addison Bellamy'
    actual = ex_0_3.format_name(first_name, last_name)

    assert actual == expected
