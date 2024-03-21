# calculations.py
from typing import List
import logging

from calculator.calculation import Calculation

# Set up logging
logger = logging.getLogger(__name__)

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        logger.info(f'Adding calculation to history: {calculation}')
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire history of calculations."""
        logger.info('Retrieving entire history of calculations')
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        logger.info('Clearing the history of calculations')
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        logger.info('Retrieving the latest calculation')
        if cls.history:
            latest_calculation = cls.history[-1]
            logger.info(f'Latest calculation: {latest_calculation}')
            return latest_calculation
        logger.info('No calculations found in history')
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        logger.info(f'Finding calculations by operation name: {operation_name}')
        calculations = [calc for calc in cls.history if calc.command.__class__.__name__ == operation_name]
        logger.info(f'Found {len(calculations)} calculations with operation name {operation_name}')
        return calculations
