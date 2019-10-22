import os
import csv
from bs4 import BeautifulSoup
from pathlib import Path

path = 'Datasets-originales/'

for archivo in os.listdir(path):
	print(archivo)

	fh = open(path+archivo, "r", encoding="utf8")
	lines = fh.readlines()
	fh.close()

	lines = filter(lambda x: not x.isspace(), lines)
	fh = open(path+archivo, "w", encoding="utf8")
	fh.write("".join(lines))
	fh.close()
	
	data = BeautifulSoup(open(path+archivo, encoding="utf8"), 'html.parser')
	tabla = data.select_one("table")
	cabeceras = [th.text for th in tabla.select("tr th")]
	archivo_excel = archivo.split(".")[0]+".csv"

	with open("Datasets-convertidos/"+archivo_excel, "w", encoding="utf8") as f:
	    wr = csv.writer(f)
	    wr.writerow(cabeceras)
	    wr.writerows([[td.text for td in row.find_all("td")] for row in tabla.select("tr + tr")])


path = 'Datasets-convertidos/'

for archivo in os.listdir(path):
	print(archivo)

	fh = open(path+archivo, "r", encoding="utf8")
	lines = fh.readlines()
	fh.close()

	lines = filter(lambda x: not x.isspace(), lines)
	fh = open(path+archivo, "w", encoding="utf8")
	fh.write("".join(lines))
	fh.close()