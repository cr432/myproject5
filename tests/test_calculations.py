"""test_calculations.py"""
from decimal import Decimal
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import AddCommand

def test_add_calculation():
    """testing add calculation"""
    a = Decimal('2')
    b = Decimal('3')
    command = AddCommand()
    calculation = Calculation(a, b, command)

    Calculations.clear_history()
    Calculations.add_calculation(calculation)

    history = Calculations.get_history()
    assert len(history) == 1
    assert history[0] == calculation

def test_clear_history():
    """testing clear history"""
    Calculations.clear_history()
    history = Calculations.get_history()
    assert len(history) == 0
