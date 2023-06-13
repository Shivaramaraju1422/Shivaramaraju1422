"""
Tests for Exercise Set 0_0
Updated: October 2022
"""
import subprocess

def test_ex_0_0(capsys):
    result = subprocess.run(['python', 'src/ex_0_0.py'], capture_output=True)
    assert result.stdout.decode() == 'Hello World!\n'
