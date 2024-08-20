import pytest
from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_hey():
    assert value("hey") == 20
    assert value("HEY") == 20

def test_other():
    assert value("go away") == 100
    assert value("GO AWAY") == 100

def test_punct():
    assert value(".?-:;(),}{][)(!_") == 100

def test_nums():
    assert value("123894123098467091234") == 100
