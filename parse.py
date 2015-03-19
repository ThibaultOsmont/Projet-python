import json
import sqlite3
from Activite import Activite
from installation import Installation
from equipement import Equipement

json_data = open('activite.json')
data = json.load(json_data)
#print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
#realData = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
conn1 = sqlite3.connect('activity.db')
c1 = conn1.cursor()
c1.execute('''CREATE TABLE IF NOT EXISTS activity
             (ActCode text, ActLib text, ComInsee text, ComLib text,EquActivitePraticable text,
             EquActivitePratique text, EquActiviteSalleSpe text, EquNbEquIdentique text, EquipementId text)''')

for activity_data in data["data"]:
	
	values = [activity_data["ActCode"],
				activity_data["ActLib"],
				activity_data["ComInsee"],
				activity_data["ComLib"],
				activity_data["EquActivitePraticable"],
				activity_data["EquActivitePratique"],
				activity_data["EquActiviteSalleSpe"],
				activity_data["EquNbEquIdentique"],
				activity_data["EquipementId"]
		]
#activity_data["ActCode"], activity_data["ActLib"], activity_data["ComInsee"], activity_data["ComLib"], activity_data["EquActivitePraticable"], activity_data["EquActivitePratique"], activity_data["EquActivitePratique"],activity_data["EquActivitePratique"], activity_data["EquActiviteSalleSpe"], activity_data["EquActiviteSalleSpe"], 	activity_data["EquNbEquIdentique"], activity_data["EquipementId"]
	c1.execute('''INSERT INTO activity VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', values)
conn1.commit()
conn1.close()

json_data_2 = open('installations.json')
data2 = json.load(json_data_2)

conn2 = sqlite3.connect('installations.db')
c2 = conn2.cursor()
c2.execute('''CREATE TABLE IF NOT EXISTS installations
             (ComInsee text, ComLib text, InsAccessibiliteAucun text, InsAccessibiliteHandiMoteur text,InsAccessibiliteHandiSens text,
             InsCodePostal text, InsDateMaj text, InsEmpriseFonciere text, InsGardiennee text, InsLibelleVoie text)''')

for installation_data in data2["data"]:
	val = [installation_data["ComInsee"], 
				installation_data["ComLib"],
				installation_data["InsAccessibiliteAucun"],
				installation_data["InsAccessibiliteHandiMoteur"],
				installation_data["InsAccessibiliteHandiSens"],
				installation_data["InsCodePostal"],
				installation_data["InsDateMaj"],
				installation_data["InsEmpriseFonciere"],
				installation_data["InsGardiennee"],
				installation_data["InsLibelleVoie"]
	]
	c2.execute('''INSERT INTO installations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', val)
conn2.commit()
conn2.close()

json_data_3 = open('equipement_fixed.json')
data3 = json.load(json_data_3)

conn3 = sqlite3.connect('equipement.db')
c3 = conn3.cursor()
c3.execute('''CREATE TABLE IF NOT EXISTS equipement
             (ComInsee text, ComLib text, EquipementId text, AnneeServiceLib text, EquipementFiche text)''')

for equipement_data in data3["data"]:
	vals = [
			equipement_data["ComInsee"],
			equipement_data["ComLib"],
			equipement_data["EquipementId"],
			equipement_data["AnneeServiceLib"],
			equipement_data["EquipementFiche"]
	]
	c3.execute('''INSERT INTO equipement VALUES (?, ?, ?, ?, ?)''', vals)
conn3.commit()
conn3.close()	