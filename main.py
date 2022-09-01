"""Mochila de la vida"""
from mochila_config import *
from mochila_items import ITEMS
from mochila_texts import *

def instructions():
	print(introduction_text)
	size_bag = int(input(f"{size_text}-> "))
	weather_bag = int(input(f"{weather_text}-> "))
	location_bag = int(input(f"{location_text}-> "))
	return (mappingInput(size_bag, weather_bag, location_bag))

def mappingInput(size, weather, location):
	#Mapping for SIZE
	if size == 1:
		size = S
	elif size == 2:
		size = M
	else:
		size = L

	#Mapping for WEATHER
	if weather == 1:
		weather = RAINY
	elif weather == 2:
		weather = CLOUDY
	else:
		weather = SUNNY

	#Mapping for LOCATION
	if location == 1:
		location = COAST
	elif location == 2:
		location = CENTER
	else:
		location = MOUNTAINS
	return (size, weather, location)

def getItemsByWeatherAndLocation(weather, location):
	resulting_items = []
	for item in ITEMS:
		if (weather in item["weather"]) and (location in item["location"]):
			resulting_items.append(item)
	return resulting_items

def thereAreEnoughItemsToFillTheBag(size_bag, items):
	total_slots = 0
	for item in ITEMS:
		total_slots += item["slots"]
	return True if total_slots >= size_bag else False

def fillBagBySize(size_bag, items):
	if not thereAreEnoughItemsToFillTheBag(size_bag, items):
		print("Ooops!!! :c sorry")
		exit(-1)

	import time
	import random
	random.seed(int(time.time()))
	life_bag = []

	while size_bag >= 1:
		random_item = random.choice(items)
		if random_item["slots"] <= size_bag:
			life_bag.append(random_item)
			items.pop(items.index(random_item))
			size_bag -= random_item["slots"]
	return life_bag

def showBag(bag, size, weather, location):
	print(f"Para la tu situación ubicación = {location} y clima = {weather}")
	print(f"Con una mochila {size} estos son los objetos que se recomiendan:")
	for item in bag:
		print(f"\t-{item['name']} ( {item['slots']} )")

def main():
	size_bag, weather_bag, location_bag = instructions()
	custom_items = getItemsByWeatherAndLocation(weather_bag, location_bag)
	life_bag = fillBagBySize(size_bag, custom_items)
	showBag(life_bag, size_bag, weather_bag, location_bag)

if __name__ == '__main__':
	main()
