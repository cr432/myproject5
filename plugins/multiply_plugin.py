# plugins/multiply_plugin.py
from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
import logging

# Set up logging
logger = logging.getLogger(__name__)

class MultiplyPlugin(CommandPlugin):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        logger.info("Performing multiplication operation.")
        return a * b
