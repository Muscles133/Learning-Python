import pytest
from numb3rs import validate


def test_true_numbers():
    assert validate("0.0.0.0") == "True"
    assert validate("255.255.255.255") == "True"
    assert validate("1.2.3.4") == "True"
    assert validate("0.255.0.0") == "True"

def test_too_high():
    assert validate("256.5.5.5") == "False"
    assert validate("5.256.5.5") == "False"
    assert validate("5.5.256.5") == "False"
    assert validate("5.5.5.256") == "False"
    assert validate("256.256.256.256") == "False"

def test_not_number():
    assert validate("a.5.5.5") == "False"
    assert validate("5.b.5.5") == "False"
    assert validate("5.5.c.5") == "False"
    assert validate("5.5.5.d") == "False"
    assert validate("f.g.h.i") == "False"

def test_too_much_input():
    assert validate("0.5.5.5.5") == "False"
    assert validate("5.0.5.5.5") == "False"
    assert validate("5.5.0.5.5") == "False"
    assert validate("5.5.5.0.5") == "False"
    assert validate("0.5.0.5.0.5.0.5") == "False"

def test_too_little_input():
    assert validate("15.20") == "False"
    assert validate("5.6.7") == "False"
    assert validate("66") == "False"
    assert validate("0.66") == "False"




