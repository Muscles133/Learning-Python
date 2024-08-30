import pytest
from fuel import convert, gauge


def test_zero():
    with pytest.raises(ZeroDivisionError, match="y cannot be zero"):
        convert("5/0")

def test_greater():
    with pytest.raises(ValueError):
        convert("10/5")
        convert("5/0")

def test_overfull():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_result():
    assert convert("5/10") == 50
    assert convert("2/10") == 20


def test_full():
    assert gauge(99) == "F"

def test_empty():
    assert gauge(1) == "E"

def test_half():
    assert gauge(50) == "50%"
