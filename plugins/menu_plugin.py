# plugins/menu_plugin.py
from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
import logging

# Set up logging
logger = logging.getLogger(__name__)

class MenuPlugin(CommandPlugin):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        logger.info("Displaying available commands.")
        logger.info("add - Addition")
        logger.info("subtract - Subtraction")
        logger.info("multiply - Multiplication")
        logger.info("divide - Division")
