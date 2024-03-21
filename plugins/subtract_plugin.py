# plugins/subtract_plugin.py
from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
import logging

# Set up logging
logger = logging.getLogger(__name__)

class SubtractPlugin(CommandPlugin):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        logger.info("Executing subtraction plugin.")
        return a - b
