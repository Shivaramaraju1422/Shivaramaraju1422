"""
Tests for ex_0_4.py
Updated for GitHub: October 2022
"""
import pytest
from src import ex_0_4

def test___int_sum___exists():
    assert hasattr(ex_0_4, 'int_sum')


def test___odd_sum___exists():
    assert hasattr(ex_0_4, 'odd_sum')


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (2, 3),
        (3, 6),
        (4, 10),
        (5, 15),
    ]
)
def test___int_sum___returns_correct_value(test_input, expected):
    assert ex_0_4.int_sum(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (2, 4),
        (3, 9),
        (4, 16),
        (5, 25),
    ]
)
def test___odd_sum___returns_correct_value(test_input, expected):
    assert ex_0_4.odd_sum(test_input) == expected
