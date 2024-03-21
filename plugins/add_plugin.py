"""plugins/add_plugin.py"""
from decimal import Decimal
import logging
from plugins.plugin_interface import CommandPlugin

# Set up logging
logger = logging.getLogger(__name__)

class AddPlugin(CommandPlugin):
    """class AddPlugin"""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        result = a + b
        logger.info(f'Addition operation: {a} + {b} = {result}')
        return result
