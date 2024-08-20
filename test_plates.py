import pytest
from plates import is_valid


"""

platelength = len(s)  # tells me the length of the plate
    if platelength >= 2 and platelength <= 6:  # lets the correct length pass through
        if is_num_alph(s):  # filters out plates that do not contain numbers or letters
            if first_2_letters(s):  # first 2 are letters
                if first_number_used(s):  # 0 can't be the first number
                    if not alph_after_num(s):  # no letters after numbers

"""



def test_platelength():
    assert is_valid("as") == True
    assert is_valid("asx123") == True
    assert is_valid("a") == False
    assert is_valid("sd34567") == False
    assert is_valid("sd3456") == True

def test_nopunct():
    punct_list = {".", "?", "-", "(", ")", ":", ";", "_", "=", "!", "{", "}", ","}
    for punt in punct_list:
        assert is_valid(f"as1{punt}") == False
    assert is_valid("asx123") == True
    
def test_nofirstzero():
    assert is_valid("as12") == True
    assert is_valid("as01") == False

def test_firsttwoletters():
    assert is_valid("as12") == True
    assert is_valid("12asd") == False

def test_noletafternum():
    assert is_valid("as12a") == False
    assert is_valid("as4fr") == False
    assert is_valid("as1234") == True

def test_alphafirst():
    assert is_valid("GGd122") == True
    assert is_valid("GG") == True
    assert is_valid("10fst") == False
    assert is_valid("4563") == False
    assert is_valid("88") == False

