"""
Tests for ex_0_2.py
Created for GitHub: October 2022
"""
import subprocess
from src import ex_0_2

def test_output():
    result = subprocess.run(['python', 'src/ex_0_2.py'], capture_output=True)
    assert result.stdout.decode() == 'Addison Bellamy\n'


def test_first_name():
    assert 'first_name' in vars(ex_0_2)
    assert ex_0_2.first_name == 'addison'


def test_last_name():
    assert 'last_name' in vars(ex_0_2)
    assert ex_0_2.last_name == 'bellamy'


def test_full_name_title():
    assert 'full_name_title' in vars(ex_0_2)
    assert ex_0_2.full_name_title == 'Addison Bellamy'
