import pytest
from twttr import shorten


def test_lower():
    assert shorten("aeiou") == ""

def test_upper():
    assert shorten("AEIOU") == ""

def test_mixed_case():
    assert shorten("HeLlO WoRLd") == "HLl WRLd"

def test_no_vowels():
    assert shorten("LSDtgs") == "LSDtgs"

def test_punct():
    assert shorten(".?-:;(),}{][)(!_") == ".?-:;(),}{][)(!_"

def test_nums():
    assert shorten("123123aaaaaaad") == "123123d"
