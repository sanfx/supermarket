"""Module containing functions for each state of Cart state.
"""
import os
import json
import copy
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
	print "-: Payment Recipt :-"
	grand_total = []
	new_total = 0
	deal_one_msg = ""
	types_two =  copy.deepcopy(types)
	for item, costs in types.items():
		if len(costs) >= 3:
			costs.pop(costs.index(min(costs)))
			total = sum(costs)
			grand_total.append(total)
			costs = []
			deal_one_msg = "Deal Buy 3 for price of 2: "
			print('Type: {} Total: {}'.format(item, total))
		else:
			new_total -= min(costs) * -1
			grand_total.append(new_total)
			print('Type: {} Total: {}'.format(item, new_total))
	sets_cost = []
	print("{}Grand Total: {}".format(deal_one_msg, sum(grand_total)))
	if len(types.items()) < 3:
	 	return
	deal_two = True
	deal_two_msg = "3 sets: "
	for item , _costs in types_two.items():
		sets_cost.append(sum(_costs))
		if len(_costs) !=3:
			deal_two = False
	if deal_two:
		deal_two_msg = "Deal get 3rd set free: "
		sets_cost.pop(sets_cost.index(min(sets_cost)))
	print("{}Grand Total: £{}".format(deal_two_msg, sum(sets_cost)))