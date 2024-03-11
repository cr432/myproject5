"""test_plugin_interface.py"""
from decimal import Decimal
from plugins.plugin_interface import CommandPlugin

class MockPlugin(CommandPlugin):
    """class MockPlugin"""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a + b

def test_plugin_interface():
    """testing plugin interface"""
    plugin = MockPlugin()
    result = plugin.execute(Decimal('2'), Decimal('3'))
    assert result == Decimal('5')
