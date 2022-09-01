from main import thereAreEnoughItemsToFillTheBag, getItemsByWeatherAndLocation, mappingInput

positions = [[1,1,1],[1,1,2],[1,1,3],[1,2,1],[1,2,2],[1,2,3],[1,3,1],[1,3,2],[1,3,3],[2,1,1],[2,1,2],[2,1,3],[2,2,1],[2,2,2],[2,2,3],[2,3,1],[2,3,2],[2,3,3],[3,1,1],[3,1,2],[3,1,3],[3,2,1],[3,2,2],[3,2,3],[3,3,1],[3,3,2],[3,3,3]]

for pos in positions:
	size, weather, location = pos
	size, weather, location = mappingInput(size, weather, location)
	items = getItemsByWeatherAndLocation(weather, location)
	if not thereAreEnoughItemsToFillTheBag(size, items):
		print(f"Algo salió mal para la combinación size={size} weather={weather} location={location}")
		exit -1
	else:
		print(f"Todo Bien para la combinación size={size} weather={weather} location={location}")