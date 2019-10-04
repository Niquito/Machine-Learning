import pandas
from pandas.io.json import json_normalize  

def juntarEstadisticas(data):

	nombre = data.iloc[0]["name"]
	data = json_normalize(data["rounds"],"matches",
				meta = ["name"],
				errors="ignore")

	cantidad_fechas = data['name'].nunique()
	goles_locales = data["score1"].sum()
	goles_visitantes = data["score2"].sum()
	total_goles = goles_locales + goles_visitantes
	total_partidos = data.shape[0]
	E_goles_fecha = total_goles / cantidad_fechas
	E_goles_partido = total_goles / total_partidos

	d = [nombre, cantidad_fechas, goles_locales, goles_visitantes, total_goles, total_partidos, E_goles_partido, E_goles_fecha]

	return d

data_es = pandas.read_json('dataset_es.json')
data_en = pandas.read_json('dataset_en.json')
data_de = pandas.read_json('dataset_de.json')
data_it = pandas.read_json('dataset_it.json')

data = [juntarEstadisticas(data_es), juntarEstadisticas(data_en), juntarEstadisticas(data_de), juntarEstadisticas(data_it)]

df = pandas.DataFrame(data, columns = ["Liga", "Cantidad de Fechas", "GL", "GV", "T. Goles", "T. Partidos", "EGF", "EGP"])

print(df)
