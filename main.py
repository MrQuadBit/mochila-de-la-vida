"""Mochila de la vida"""
from mochila_config import *
from mochila_items import ITEMS
from mochila_texts import *

def instructions():
	print(introduction_text)
	size_bag = int(input(f"{size_text}-> "))
	weather_bag = int(input(f"{weather_text}-> "))
	location_bag = int(input(f"{location_text}-> "))

	return (size_bag, weather_bag, location_bag)

def main():
	size_bag, weather_bag, location_bag = instructions()
	print(size_bag, weather_bag, location_bag)
if __name__ == '__main__':
	main()
