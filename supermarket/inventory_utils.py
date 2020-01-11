"""This module contains function realted to supermarket inventory.
"""
import os
import yaml
import logging

logging.basicConfig(level=logging.DEBUG)

def get_products():
	"""Function to read yaml file.

	Args:
		inventory_file (str) : name of the inentory file containing list of 
		products.
	
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
	print get_products('products.yaml')
