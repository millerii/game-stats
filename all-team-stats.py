#!/usr/bin/env python3

import csv
import os


def ReadFile():
	path = os.path.dirname(os.path.abspath(__file__))
	path = os.path.join(path, "")
	rows = []

	with open(path + "IIHF_WC-stats.csv", encoding="utf8") as file:
		csvreader = csv.reader(file)
		for row in csvreader:
			rows.append(row)
	
	return rows

def ReadStats(rows):
	teams = {}
	
	for i in rows:
		if i[0].startswith("["): # Tilaston vuosijako-merkki
			continue

		if i[0] not in teams:
			teams[i[0]] = 0,0,0 # Alusta kotijoukkueen nimi '0,0,0' tuloksella ensimmäisellä kerralla
		if i[1] not in teams:
			teams[i[1]] = 0,0,0 # Alusta vierasjoukkueen nimi '0,0,0' tuloksella ensimmäisellä kerralla

		if i[2] > i[3]:
			teams[i[0]] = teams[i[0]][0] + 1, teams[i[0]][1], teams[i[0]][2] # Koti voitto
			teams[i[1]] = teams[i[1]][0], teams[i[1]][1] + 1, teams[i[1]][2] # Vieras häviö
		elif i[3] > i[2]:
			teams[i[1]] = teams[i[1]][0] + 1, teams[i[1]][1], teams[i[1]][2] # Vieras voitto
			teams[i[0]] = teams[i[0]][0], teams[i[0]][1] + 1, teams[i[0]][2] # Koti häviö
		else:
			teams[i[0]] = teams[i[0]][0], teams[i[0]][1], teams[i[0]][2] + 1 # Tasapeli
			teams[i[1]] = teams[i[1]][0], teams[i[1]][1], teams[i[1]][2] + 1 # Tasapeli

	return teams

def ShowStats(teams):
	print(f"{'Team':<14}{'(Win, Loss, Tie)':<18} Win   /  Tie")
	print("---------------------------------------------------")

	for w in sorted(teams, key=teams.get, reverse=True):
		Win_ratio = teams[w][0] / (teams[w][0] + teams[w][1] + teams[w][2]) * 100
		Tie_ratio = teams[w][2] / (teams[w][0] + teams[w][1] + teams[w][2]) * 100
		print(f"{w:<15} {str(teams[w]):<15} {round(Win_ratio, 1):<4} % / {round(Tie_ratio, 1):<4} %")


teams = ReadStats(ReadFile())
ShowStats(teams)
