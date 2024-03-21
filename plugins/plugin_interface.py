# plugin_interface.py
from decimal import Decimal
from abc import ABC, abstractmethod
import logging

# Set up logging
logger = logging.getLogger(__name__)

class CommandPlugin(ABC):
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        logger.info("Executing plugin command.")
