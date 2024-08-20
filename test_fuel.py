import pytest
from fuel import convert, gauge


def test_zero():
    assert convert("5/0") == 0


