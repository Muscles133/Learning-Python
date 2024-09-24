import pytest
from working import convert


def test_uppercase():
    with pytest.raises(ValueError):
        convert("9 am to 5pm")


def test_bad_input():
    with pytest.raises(ValueError):
        convert("cat to dog")


def test_24input():
    with pytest.raises(ValueError):
        convert("9:00 AM to 17:00")
        convert("09:00 to 5PM")
        convert("09:00 to 17:00")


def test_outofrange():
    with pytest.raises(ValueError):
        convert("9:60 AM to 7:60 PM")
        convert("15:25 AM to 17:15 PM")


def test_correct():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12:00 AM") == "00:00 to 00:00"


def test_nightshift():
    assert convert("9 PM to 5:00 AM") == "21:00 to 05:00"


def test_ommit():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
