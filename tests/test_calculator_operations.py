"""test_calculator_operations.py"""
from decimal import Decimal
from calculator import Calculator

def test_addition():
    "testing addition"
    assert Calculator.add(Decimal('2'), Decimal('2')) == Decimal('4')

def test_subtraction():
    "testing subtraction"
    assert Calculator.subtract(Decimal('2'), Decimal('2')) == Decimal('0')

def test_divide():
    "testing division"
    assert Calculator.divide(Decimal('2'), Decimal('2')) == Decimal('1')

def test_multiply():
    "testing multiplication"
    assert Calculator.multiply(Decimal('2'), Decimal('2')) == Decimal('4')

def test_menu():
    "testing menu"
    assert Calculator.menu(Decimal('0'), Decimal('0')) == Decimal('0')  # Modify based on your menu command behavior
