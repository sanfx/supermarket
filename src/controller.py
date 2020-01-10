def get_total_cost(items):
	"""Calculate the total cost of items in shopping cart.
	"""
	# deals = {"deal_1": }
	item_types = []
	count = 0
	for itemcode, item in items.iteritems():
		item_types.append(item["type"])
		print len(item_types) 

	print item_types
	return