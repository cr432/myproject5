# main.py
from decimal import Decimal, InvalidOperation
import logging
from calculator import Calculator
from plugins.plugin_interface import CommandPlugin
from importlib import import_module
import os
import inspect
from multiprocessing import Pool

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler and set its log level to INFO
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Create a console handler and set its log level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Define the log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Set the format for both handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def load_plugins():
    plugins = []

    # Load plugins from the 'plugins' directory
    plugins_directory = os.path.join(os.path.dirname(__file__), 'plugins')
    for file_name in os.listdir(plugins_directory):
        if file_name.endswith('_plugin.py'):
            module_name = file_name[:-3]  # Remove '.py' extension
            module = import_module(f'plugins.{module_name}')
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, CommandPlugin) and obj != CommandPlugin:
                    plugins.append(obj())

    return plugins

def execute_plugin(plugin, a, b):
    return plugin.execute(a, b)

def main():
    logger.info('Application started')
    
    calculator = Calculator()
    plugins = load_plugins()

    while True:
        command = input("Enter command (add/subtract/multiply/divide/menu/exit): ").lower()
        logger.info(f'User input: {command}')

        if command == 'exit':
            break

        if command == 'menu':
            # Display menu options without performing any calculations
            logger.info("Displaying menu options")
            print("Available Commands:")
            print("add - Addition")
            print("subtract - Subtraction")
            print("multiply - Multiplication")
            print("divide - Division")
            continue  # Skip the rest of the loop and start over

        if command in ['add', 'subtract', 'multiply', 'divide']:
            a = input("Enter first number: ")
            b = input("Enter second number: ")

            try:
                a_decimal, b_decimal = map(Decimal, [a, b])

                # Dynamically call the corresponding plugin based on user input
                plugin_module_name = f'{command}_plugin'
                plugin_class_name = command.capitalize() + 'Plugin'

                # Import the module dynamically
                module = import_module(f'plugins.{plugin_module_name}')

                # Get the class dynamically
                plugin_class = getattr(module, plugin_class_name)

                # Create an instance and execute using multiprocessing
                with Pool() as pool:
                    result = pool.apply(execute_plugin, args=(plugin_class(), a_decimal, b_decimal))
                
                logger.info(f'{command} command executed successfully')
                logger.info(f"{a_decimal} {command} {b_decimal} = {result}")

                print(f"The result is: {result}")

            except InvalidOperation:
                logger.error(f'Invalid number input: {a} or {b} is not a valid number.')
                print(f"Invalid number input: {a} or {b} is not a valid number.")
            except ZeroDivisionError as e:
                logger.error('Error: Division by zero.')
                print(str(e))
            except ValueError:
                logger.error('Invalid input. Please enter valid numbers.')
                print("Invalid input. Please enter valid numbers.")

    logger.info('Application exited')


if __name__ == '__main__':
    main()
