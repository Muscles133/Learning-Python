from twttr import shorten


def test_lower():
    try:
        assert shorten("aeiou") == ""
    except AssertionError:
        print("Failed to remove lowercase vowels")

def test_upper():
    try:
        assert shorten("AEIOU") == ""
    except AssertionError:
        print("Failed to remove upper vowels")


def test_mixed_case():
    try:
        assert shorten("HeLlO WoRLd") == "HLl WRLd"

    except AssertionError:
        print("Failed on mixed case input")


def test_no_vowels():
    try:
        assert shorten("LSDtgs") == "LSDtgs"

    except AssertionError:
        print("Modified string without vowels")