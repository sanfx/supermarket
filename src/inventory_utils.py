"""This module contains function realted to supermarket inventory.
"""
import yaml

def get_products(inventory_file):
	"""Function to read yaml file.

	Args:
		inventory_file (str) : name of the inentory file containing list of 
		products.
	
	Returns:
		(dict): products found in the inventory file.
	"""
	stream = open(inventory_file, 'r')
	return yaml.load(stream)


if __name__ == '__main__':
	# For testing
	print get_products('products.yaml')
