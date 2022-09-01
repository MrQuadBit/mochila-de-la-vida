def getItemsByPriority(priority=HIGH, LIST=ITEMS):
	priority_items = []
	for item in LIST:
		if item["priority"] == priority:
			priority_items.append(item)
	return priority_items

def getItemsBySizeSlots(size_slots=THREE, LIST=ITEMS):
	size_slots_items = []
	for item in LIST:
		if item["slots"] == size_slots:
			size_slots_items.append(item)
	return size_slots_items