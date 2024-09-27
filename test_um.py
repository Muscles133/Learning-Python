import pytest
from um import count


def test_whitespace():
    assert count("um um um um") == 4
    assert count("um um ") == 2
    assert count(" um ") == 1

def test_insideword():
    assert count("yummy") == 0
    assert count("yum") == 0
    assert count("yummy yum Yum um") == 1

def test_case():
    assert count("Um") == 1
    assert count("um") == 1
    assert count("uM") == 1
    assert count("UM") == 1


