"""This module contains function related to supermarket inventory.
"""
import os
import yaml
import logging

logging.basicConfig(level=logging.DEBUG)

def get_products():
    """Function to read inventory file.
    
    Returns:
        (dict): products found in the inventory file.
    """
    try:
        inventory_file = os.path.join(os.getenv("HOME"), "products.yaml")
        stream = open(inventory_file, 'r')
        return yaml.load(stream)
    except IOError, error:
        logging.error(error)
        exit()


if __name__ == '__main__':
    # For testing
    print get_products()
