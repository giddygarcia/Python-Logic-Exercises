from calculator.calculator import Calculator
import pytest

def test_init():
    calc = Calculator()
    assert calc.memory == 0

def test_add():
    calc = Calculator()
    calc.add(4)
    assert calc.memory == 4

def test_subtract():
    calc = Calculator(10)
    calc.subtract(4)
    assert calc.memory == 6

def test_multiply():
    calc = Calculator(4)
    calc.multiply(-4)
    assert calc.memory == -16

def test_divide():
    calc = Calculator(16)
    calc.divide(4)
    assert calc.memory == 4

def test_divide_by_zero():
    calc = Calculator(4)
    with pytest.raises(ValueError):
        calc.divide(0)


def test_root_square():
    calc = Calculator(4)
    calc.root(2)
    assert calc.memory == 2

def test_root_n():
    calc = Calculator(256)
    calc.root(4)
    assert calc.memory == 4

def test_root_zero():
    calc = Calculator(4)
    with pytest.raises(ValueError):
        calc.root(0)

def test_root_negative():
    calc = Calculator(-16)
    with pytest.raises(ValueError):
        calc.root(2)


def test_reset():
    calc = Calculator(100)
    assert calc.reset() == 0
    assert calc.memory == 0


def test_working_memory():
    # series of tests across operands with memory reset in between
    calc = Calculator()
    calc.add(5)
    calc.multiply(4)
    calc.subtract(4)
    calc.root(4)
    assert calc.memory == 2

    assert calc.reset() == 0
    assert calc.memory == 0

    calc.add(10)
    calc.subtract(1)
    calc.divide(3)
    assert calc.memory == 3