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

team = input("Syötä joukkue: ")
stats = {'games': 0, 'home_win': 0, 'away_win': 0, 'home_loss':0, 'away_loss':0}
home_tie = 0
away_tie = 0

for i in rows:
	if i[0].startswith("["): # Tilaston vuosijako-merkki
		continue

	if team == i[0]:
		if i[2] > i[3]:
			stats['home_win'] += 1
		elif i[3] > i[2]:
			stats['home_loss'] += 1
		else:
			home_tie += 1

	elif team == i[1]:
		if i[2] < i[3]:
			stats['away_win'] += 1
		elif i[3] < i[2]:
			stats['away_loss'] += 1
		else:
			away_tie += 1

print()
wins = stats['home_win'] + stats['away_win']
loss = stats['home_loss'] + stats['away_loss']
games = wins + loss + home_tie + away_tie
print(team, "pelannut yhteensä", games, "peliä")
print(wins, "voittoa,", "josta kotivoittoja", stats['home_win'], "ja vierasvoittoja", stats['away_win'])
print("Häviöt:", stats['home_loss'], "kotipelissä ja", stats['away_loss'], "vieraspelissä")
print("Tasapelit:", home_tie, "kotipelissä,", away_tie, "vieraspelissä")
