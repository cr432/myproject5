"""plugins/divide_plugin.py"""
from decimal import Decimal
import logging
from plugins.plugin_interface import CommandPlugin

# Set up logging
logger = logging.getLogger(__name__)

class DividePlugin(CommandPlugin):
    """class DividePlugin"""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b != 0:
            result = a / b
            logger.info('Division operation: %s / %s = %s', a, b, result)
            return result
        logger.error("Division by zero error")
        raise ZeroDivisionError("Error: Division by zero.")
