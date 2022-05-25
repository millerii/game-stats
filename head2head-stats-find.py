#!usr/bin/env/ python3

import csv
import os
from sys import exit

path = os.path.dirname(os.path.abspath(__file__))+"\\"
rows = []
with open(path + "IIHF_WC-stats.csv", encoding="utf8") as file:
	csvreader = csv.reader(file)
	for row in csvreader:
		rows.append(row)

pari1 = {'team': "Kanada", 'home_win': 0, 'away_win': 0}
pari2 = {'team': "Suomi", 'home_win': 0, 'away_win': 0}
tasapeli = 0
GameInList = False

pari1['team'], pari2['team'] = input("Syötä kaksi joukkuetta: ").split()
print()

# Tarkista löytyykö kisapari tietokannasta
for line in rows:
	if line[0].startswith("["): # Tilaston vuosijakaja
		print(line[0])
		
	if pari1['team'] in line and pari2['team'] in line:
		GameInList = True
		print(line)

# Jos otteluparia ei löydy, lopeta
if not GameInList:
	print("Otteluparia ei löytynyt")
	exit()

for i in rows:
	if i[0].startswith("["): # Tilaston vuosijako-merkki
		continue

	if pari1['team'] == i[0] and pari2['team'] == i[1]:
		if i[2] > i[3]:
			pari1['home_win'] += 1
		elif i[3] > i[2]:
			pari2['away_win'] += 1
		else:
			tasapeli += 1

	elif pari1['team'] == i[1] and pari2['team'] == i[0]:
		if i[2] < i[3]:
			pari1['away_win'] += 1
		elif i[3] < i[2]:
			pari2['home_win'] += 1
		else:
			tasapeli += 1

print()
print("Pelatut ottelut:", pari1['team'], "-", pari2['team'])
print(pari1['team'], "voitti", pari1['home_win'] + pari1['away_win'], "peliä,", "josta kotivoittoja", pari1['home_win'])
print(pari2['team'], "voitti", pari2['home_win'] + pari2['away_win'], "peliä,", "josta vierasvoittoja", pari2['away_win'],)
print(tasapeli, " tasapeli(ä)")
