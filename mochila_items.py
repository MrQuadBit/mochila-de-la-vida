#https://www.gob.mx/profeco/documentos/mochila-de-emergencia-y-botiquin-de-primeros-auxilios?state=published
#https://twitter.com/GobCDMX/status/1419341679505514501?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1419341679505514501%7Ctwgr%5E569222854469afcadf9174a11451a891af1e9dbb%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fd-39464250872953548564.ampproject.net%2F2207281718002%2Fframe.html

from mochila_config import *
ITEMS = [
	{
		"name":"Linterna",
		"slots":1,
		"weather":[CLOUDY],
		"location":[CENTER,MOUNTAINS],
		"priority":2
	},
	{
		"name":"Radio",
		"slots":1,
		"weather":[SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":3
	},
	{
		"name":"Agua",
		"slots":2,
		"weather":[RAINY, CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":3
	},
	{
		"name":"Comida",
		"slots":3,
		"weather":[RAINY, CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":3
	},
	{
		"name":"Ropa",
		"size":2,
		"weather":[RAINY, CLOUDY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":1
	},
	{
		"name":"Encendedor",
		"size":1,
		"weather":[CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":2
	},
	{
		"name":"Papel de baño",
		"size":3,
		"weather":[CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":2
	},
	{
		"name":"Silbato",
		"size":1,
		"weather":[RAINY, CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":2
	},
	{
		"name":"Documentos",
		"size":1,
		"weather":[RAINY, CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":3
	},
	{
		"name":"Llaves",
		"size":1,
		"weather":[RAINY, CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":1
	},
	{
		"name":"Botiquín de primeros auxilios",
		"size":3,
		"weather":[RAINY, CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":3
	},
	{
		"name":"Dinero",
		"size":1,
		"weather":[RAINY, CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":2
	},
	{
		"name":"Directorio Telefónico",
		"size":2,
		"weather":[CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":2
	},
	{
		"name":"Medicamentos",
		"size":2,
		"weather":[RAINY, CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":3
	},
	{
		"name":"Plumma y Libreta",
		"size":2,
		"weather":[CLOUDY, SUNNY],
		"location":[COAST,CENTER],
		"priority":2
	},
	{
		"name":"Cobija",
		"size":2,
		"weather":[CLOUDY, SUNNY],
		"location":[COAST,MOUNTAINS],
		"priority":2
	},
	{
		"name":"Comida para mascota",
		"size":1,
		"weather":[RAINY, CLOUDY, SUNNY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":2
	},
	{
		"name":"Protector solar",
		"size":1,
		"weather":[SUNNY],
		"location":[COAST,CENTER],
		"priority":2
	},
	{
		"name":"Cuchillo",
		"size":1,
		"weather":[CLOUDY, SUNNY],
		"location":[MOUNTAINS],
		"priority":2
	},
	{
		"name":"Celular",
		"size":1,
		"weather":[SUNNY],
		"location":[CENTER],
		"priority":3
	},
	{
		"name":"Paragüas",
		"size":3,
		"weather":[RAINY],
		"location":[COAST,CENTER,MOUNTAINS],
		"priority":3
	},

]