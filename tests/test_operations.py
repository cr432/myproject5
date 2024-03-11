""" test_operations.py """
from decimal import Decimal
from calculator.operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    """testing add command"""
    add_command = AddCommand()
    result = add_command.execute(Decimal('2'), Decimal('3'))
    assert result == Decimal('5')

def test_subtract_command():
    """testing subtract command"""
    subtract_command = SubtractCommand()
    result = subtract_command.execute(Decimal('5'), Decimal('3'))
    assert result == Decimal('2')

def test_multiply_command():
    """testing multiply command"""
    multiply_command = MultiplyCommand()
    result = multiply_command.execute(Decimal('2'), Decimal('3'))
    assert result == Decimal('6')

def test_divide_command():
    """testing divide command"""
    divide_command = DivideCommand()
    result = divide_command.execute(Decimal('6'), Decimal('2'))
    assert result == Decimal('3')
