import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_notnumber():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit("poop")

def test_notnumber2():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(3)
        jar.withdraw("poop")


def test_fulljar():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(20)

def test_nocookes():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.withdraw(20)


