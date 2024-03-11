"""test_calculation.py"""
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import Command

class MockCommand(Command):
    """class MockCommand"""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a + b

def test_create_calculation():
    """testing create calculation"""
    a = Decimal('2')
    b = Decimal('3')
    command = MockCommand()
    calculation = Calculation.create(a, b, command)
    assert calculation.a == a
    assert calculation.b == b
    assert calculation.command == command

def test_perform_calculation():
    """testing perform calculation"""
    a = Decimal('4')
    b = Decimal('5')
    command = MockCommand()
    calculation = Calculation(a, b, command)
    result = calculation.perform()
    assert result == a + b

def test_repr_calculation():
    """testing repr calculation"""
    a = Decimal('6')
    b = Decimal('7')
    command = MockCommand()
    calculation = Calculation(a, b, command)
    repr_str = repr(calculation)
    assert f"Calculation({a}, {b}, MockCommand)" == repr_str
