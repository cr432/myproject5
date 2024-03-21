# operations.py
from decimal import Decimal
from abc import ABC, abstractmethod
import logging

# Set up logging
logger = logging.getLogger(__name__)

class Command(ABC):
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        pass

class AddCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        result = a + b
        logger.info(f'Addition operation: {a} + {b} = {result}')
        return result

class SubtractCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        result = a - b
        logger.info(f'Subtraction operation: {a} - {b} = {result}')
        return result

class MultiplyCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        result = a * b
        logger.info(f'Multiplication operation: {a} * {b} = {result}')
        return result

class DivideCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b != 0:
            result = a / b
            logger.info(f'Division operation: {a} / {b} = {result}')
            return result
        else:
            logger.error('Division by zero error')
            raise ZeroDivisionError("Error: Division by zero.")

class MenuCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        logger.info('Displaying menu options')
        print("Available Commands:")
        print("add - Addition")
        print("subtract - Subtraction")
        print("multiply - Multiplication")
        print("divide - Division")
        return 0  # Return 0 or any value, as it won't affect the result
