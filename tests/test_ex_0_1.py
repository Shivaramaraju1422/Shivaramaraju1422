"""
Tests for ex_0_1.py
Created: October 2022
"""
import subprocess
from src import ex_0_1
def test_output():
    result = subprocess.run(['python', 'src/ex_0_0.py'], capture_output=True)
    assert result.stdout.decode() == 'Hello World!\n'


def test_greeting_variable_exists():
    assert 'greeting' in vars(ex_0_1)
    assert ex_0_1.greeting == 'Hello World!'
