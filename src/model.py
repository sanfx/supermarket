"""This module contains the model for shopping cart.
"""
import json
import copy
import os


class ShoppingCart(object):
	"""Provides methods to interact with shopping cart."""
	cart_items_file = "user.json"

	def __init__(self):
		super(ShoppingCart, self).__init__()
		self.items = {}
		self.data = {}
		self.data["items"] = []

	def _serialize(self):
		"""Serialize cart items.
		"""
		for _, item in self.items.iteritems():
			self.data['items'].append(item)
		if os.path.isfile(self.cart_items_file):
			os.remove(self.cart_items_file)
		with open(self.cart_items_file, "a") as fh:
			json.dump(self.data, fh, sort_keys=True, indent=4)

	def _deserialize(self):
		if os.path.isfile(self.cart_items_file):
			with open(self.cart_items_file, "r") as jsn:
				read_data = json.load(jsn)
				for item in read_data["items"]:
					yield item

	def add(self, new_items):
		"""Adds the items to shopping cart.

		Args:
			new_items (dict) : item along with meta data.
		"""
		old_items = []
		for item in self._deserialize():
			if item not in new_items.values():
				old_items.append(item)

		for old in old_items:
			new_items[old["itemcode"]] = old

		self.items = new_items

		if new_items:
			self.items.update(new_items)
			self._serialize()

	def remove(self, itemcodes):
		"""Remove an item from the shopping cart.
		"""
		keep_items = {}
		print "recieved: ", itemcodes
		for item in self._deserialize():
			if item["itemcode"] not in itemcodes:
				keep_items[item["itemcode"]] = item
	
		self.items = keep_items
		self._serialize()


	def list(self):
		"""Lists items added in the cart.
		"""
		print "[\tWilko Shopping Cart\t\t]"
		items = list(self._deserialize())
		if not items:
			print "Cart Empty !"
			return
		for item in items:
			print item



	def checkout(self):
		"""Checkout cart and print recipt.
		"""
		pass

		