import pandas
from pandas.io.json import json_normalize  

data = pandas.read_json('dataset_it.json')

data = json_normalize(data["rounds"],"matches",
				meta = ["name"],
				errors="ignore")

#del data["team1.code"]
#del data["team2.code"]
#del data["team1.name"]
data = data.drop(["team1.code", "team1.key", "team2.code", "team2.key"], axis=1)

#print(data.shape)
#print(data.ndim)
cantidad_fechas = data['name'].nunique()
goles_locales = data["score1"].sum()
goles_visitantes = data["score2"].sum()
total_goles = goles_locales + goles_visitantes
total_partidos = data.shape[0]

E_goles_fecha = total_goles / cantidad_fechas
E_goles_partido = total_goles / total_partidos

print(cantidad_fechas)
print(E_goles_fecha)

print(total_partidos)
print(E_goles_partido)

print("---")


print(data["score1"].describe())
print(goles_locales)

print(data["score2"].describe())
print(goles_visitantes)
print("---")

data = data.rename(columns={"date": "Fecha"})
data = data.rename(columns={"score1": "L"})
data = data.rename(columns={"score2": "V"})
data = data.rename(columns={"name": "Jornada"})
data = data.rename(columns={"team1.name": "Local"})
data = data.rename(columns={"team2.name": "Visitante"})

#print(data[data["Jornada"] == "5^ Giornata"].head(20))