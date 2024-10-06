import pytest
from seasons import get_mins, min_to_word


# def test_correct():
#     assert get_mins("1985-03-27") == 20777760

def test_bad_input():
    with pytest.raises(ValueError):
        get_mins("cat to dog")

def test_bad_format():
    with pytest.raises(ValueError):
        get_mins("January 1, 1999")

def test_words():
    assert min_to_word(1) == "One minutes"
    assert min_to_word(127) == "One hundred twenty-seven minutes"


def test_no_and():
    assert min_to_word(127) != "One hundred and twenty-seven minutes"

def test_bad_format():
    with pytest.raises(ValueError):
        min_to_word("poop")

def test_future():
    with pytest.raises(ValueError):
        get_mins("January 1, 2050")

def test_startupper():
    assert min_to_word(127) != "one hundred twenty-seven minutes"