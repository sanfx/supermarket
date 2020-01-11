"""This module contains the model for shopping cart.
"""
import os
import copy
import json

from collections import defaultdict

# Local Imports
from controller import (
	cart_items_file,
	read_user_cart_file, 
	merge_items,
	print_recipts
	)


class ShoppingCart(object):
	"""Provides methods to interact with shopping cart."""

	def __init__(self):
		super(ShoppingCart, self).__init__()
		self._items = {}
		self._data = {}
		self._data["items"] = []

	def _serialize(self):
		"""Serialize cart items.
		"""
		for _, item in self._items.iteritems():
			self._data['items'].append(item)
		if os.path.isfile(cart_items_file):
			os.remove(cart_items_file)
		with open(cart_items_file, "a") as fh:
			json.dump(self._data, fh, sort_keys=True, indent=4)

	def add(self, new_items):
		"""Adds the items to shopping cart.

		Args:
			new_items (dict) : item along with meta data.
		"""
		self._items = merge_items(new_items)

		if new_items:
			self._items.update(new_items)
			self._serialize()

	def remove(self, itemcodes):
		"""Remove an item from the shopping cart.

		Args:
			itemcodes list(int) : list of itemcodes to remove from cart.
		"""
		keep_items = {}
		print "Removing: ", itemcodes
		for item in read_user_cart_file():
			if item["itemcode"] not in itemcodes:
				keep_items[item["itemcode"]] = item
		self._items = keep_items
		self._serialize()

	def list(self):
		"""Lists items added in the cart.
		"""
		print "[\tWilko Shopping Cart\t\t]"
		items = list(read_user_cart_file())
		if not items:
			print "Cart Empty !"
			exit()
		for item in items:
			print item

	def checkout(self):
		"""Checkout cart and print recipt.

		Returns:
			list(type, costs) : checkout items with cost.
		"""
		cart_items = list(read_user_cart_file())
		if not cart_items:
			print "Cart is empty !"
			exit() 
		types = defaultdict(list)
		for datum in cart_items:
			types[datum[u'type']].append(datum[u'cost'])
		return types







		