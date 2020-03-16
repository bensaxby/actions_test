from ..lib import main


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def test_add():
    assert main.add(1, 2) == 3


def test_subtract():
    assert main.subtract(1, 2) == -1
