import pytest
from calculator1 import calculate

def test_addition():
    assert calculate("add", 3, 2) == 5

def test_subtraction():
    assert calculate("subtract", 5, 3) == 2

def test_multiplication():
    assert calculate("multiply", 4, 2) == 8

def test_division():
    assert calculate("divide", 10, 2) == 5
