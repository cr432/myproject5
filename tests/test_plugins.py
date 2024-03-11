"""test_plugins.py"""
from decimal import Decimal
from importlib import import_module
import os
import inspect

from plugins.plugin_interface import CommandPlugin

def test_plugins():
    """testing"""
    plugins = []

    # Load plugins from the 'plugins' directory
    plugins_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'plugins')
    for file_name in os.listdir(plugins_directory):
        if file_name.endswith('_plugin.py'):
            module_name = file_name[:-3]  # Remove '.py' extension
            module = import_module(f'plugins.{module_name}')
            for _, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, CommandPlugin) and obj != CommandPlugin:
                    plugins.append(obj())

    assert len(plugins) > 0
    for plugin in plugins:
        result = plugin.execute(Decimal('2'), Decimal('3'))
        assert isinstance(result, (Decimal, int))  # Check for Decimal or int
