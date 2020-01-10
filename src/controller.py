"""Module containing functions for each state of Cart state.
"""
import os
import json
import getpass

cart_items_file = os.path.join(os.getenv("HOME"), "user.json")

def read_user_cart_file():
	"""Reads items added by user to his shopping cart.

	Yields:
		(dict) : item with cost and itemcode
	"""
	if os.path.isfile(cart_items_file):
		with open(cart_items_file, "r") as jsn:
			read_data = json.load(jsn)
			for item in read_data["items"]:
				yield item


def merge_items(new_items):
	"""Provides merged old data from disk with new data

	Args:
		new_items (dict) : new item to added to cart

	Returns:
		new_items (dict) : new items with items already in cart
	"""
	old_items = []
	for item in read_user_cart_file():
		if item not in new_items.values():
			old_items.append(item)

	for old in old_items:
		new_items[old["itemcode"]] = old
	return new_items


def print_recipts(types):
	"""Prints the recipts with deals applied.

	Args
		types (list) : items purchased with cost
	"""
	grand_total = []
	for item, costs in types.items():
		# costs.pop(costs.index(min(costs)))
		total = sum(sorted(costs[1:])) if len(costs) >= 3 else sum(costs)
		print(u'type: {} total: {}'.format(item, total))
		grand_total.append(total)
		print("Deal 1 Grand Total: {}".format(sum(grand_total)))
		sets_cost = []
		if len(types.items()) < 3:
			exit()
		for item , costs in types.items():
			sets_cost.append(sum(costs))
		sets_cost.pop(sets_cost.index(min(sets_cost)))
		print("Deal 2 Grand Total: {}".format(sum(sets_cost)))