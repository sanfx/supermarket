# -*- coding: utf-8 -*-

import argparse
import sys
from pprint import pprint

# Local imports
from inventory_utils import get_products
from controller import get_total_cost
from model import ShoppingCart



class Supermarket(object):
	"""Supermarket class containing methods that act as sub commands."""

	def __init__(self, inventory_file):
		super(Supermarket, self).__init__()
		self._products = get_products(inventory_file)
		self._parser = argparse.ArgumentParser(
			description="Supermarket command provides various sub-commands to interact with products in the supermarket.",)
		self._parser.add_argument('command', help='Subcommand to run')
		# parse_args defaults to [1:] for args, but you need to
		# exclude the rest of the args too, or validation will fail
		args = self._parser.parse_args(sys.argv[1:2])
		if not hasattr(self, args.command):
			print 'Unrecognized supermarket command'
			self._parser.print_help()
			exit(1)

		self._cart = ShoppingCart()

		self._cart_items = {} # TODO: serialize cart items to disk
		# use dispatch pattern to invoke method with same name
		getattr(self, args.command)()

	def display(self):
		"""Displays the products in the supermarket.
		"""
		# parser = argparse.ArgumentParser(description="sends the gitlab project to user for testing purpose.")
		print "Welcome to Wilko Supermarket ! "
		display_shelf = {}

		for code, product in self._products.iteritems():
			_type = product["type"] 
			product.update({"itemcode": code})
			if _type not in display_shelf:
				display_shelf[_type] = [product]
			else:
				display_shelf[_type].append(product)

		for product_type, products in display_shelf.iteritems():
			line = "-" * (len(product_type) + 1)
			print line
			print "|{type}|".format(type=product_type.capitalize())
			print line
			for product in products:
				print product

	def add(self):
		"""Command to add items to shopping cart.
		"""
		parser = argparse.ArgumentParser(description='Enter the itemcode displayed to add to your shopping cart.')
		parser.add_argument('itemcodes', nargs='+', help='Enter the item code separated by space.')
		args = parser.parse_args(sys.argv[2:])
		not_found = []

		user_entered_codes = [int(item) for item in args.itemcodes]
		for itemcode, value in self._products.iteritems():
			if itemcode in user_entered_codes:
				print value["name"].capitalize(), value["type"], "£{}".format(value["cost"])
				self._cart_items[itemcode] = value

		if self._cart_items:
			print "Total: ", get_total_cost(self._cart_items)

		for code in user_entered_codes:
			if code not in self._products:
				not_found.append(code)

		if not_found:
			print "Items with following code not found: {}".format(not_found)


	def cart(self):
		"""Command provide a subcommands to interact with shopping cart.
		"""
		if len(sys.argv) == 2:
			self._cart.list()
		else:
			parser = argparse.ArgumentParser(
            description="Interact with shopping cart.")
			parser.add_argument("-a", "--add", nargs="+", 
						help="Enter the item code separated by space.")
			parser.add_argument("-r", "--remove", nargs="+", 
						help="Enter the item code separated by space.")
			args = parser.parse_args(sys.argv[2:])
			if args.add:
				user_entered_codes = [int(item) for item in args.add]
				if user_entered_codes:
					for itemcode, value in self._products.iteritems():
						if itemcode in user_entered_codes:
							value.update({"itemcode": itemcode})
							print value["name"].capitalize(), value["type"], 
							"£{}".format(value["cost"])
							self._cart_items[itemcode] = value
					
					if self._cart_items:
						self._cart.add(self._cart_items)
			if args.remove:
				self._cart.remove([int(item) for item in args.remove])


		# TODO: 
		# shopping cart
		# Checkout and print recipt
		


