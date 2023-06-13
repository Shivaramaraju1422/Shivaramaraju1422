"""
Tests for ex_0_5.py
Updated for GitHub: October 2022
"""
import pytest
from src import ex_0_5


def test___ground_cover___exists():
    assert hasattr(ex_0_5, 'ground_cover')
    assert hasattr(ex_0_5.ground_cover, '__call__')


def test___depth___exists():
    assert hasattr(ex_0_5, 'depth')
    assert hasattr(ex_0_5.depth, '__call__')


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('SN00', 0),
        ('SN10', 1),
        ('SN20', 2),
    ]
)
def test___ground_cover___exists(test_input, expected):
    assert ex_0_5.ground_cover(test_input) == expected


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('SN00', 0),
        ('SN11', 1),
        ('SN22', 2),
    ]
)
def test___depth___exists(test_input, expected):
    assert ex_0_5.depth(test_input) == expected
