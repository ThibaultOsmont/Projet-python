import json
import sqlite3
from Classes.Activite import Activite
from Classes.installation import Installation
from Classes.equipement import Equipement

#Ouverture de la connexion SQL et des fichiers jSON
json_data_act = open('jSON/activite.json')
data_act = json.load(json_data_act)

json_data_insta = open('jSON/installations.json')
data_insta = json.load(json_data_insta)

json_data_equip = open('jSON/equipement_fixed.json')
data_equip = json.load(json_data_equip)

connexion = sqlite3.connect('DataBases/SportEnLoireAtlantique.db')

print("Création de la table activities...")
c1 = connexion.cursor()
c1.execute('''CREATE TABLE IF NOT EXISTS activities
             (ActCode text, ActLib text, 
             ComInsee text, ComLib text,
             EquipementId text)''')

print("OK. Insertion des éléments dans la table activities...")
for activity_data in data_act["data"]:
	myAct = Activite(activity_data["ActCode"])
	myAct.setActLib(activity_data["ActLib"])
	myAct.setComInsee(activity_data["ComInsee"])
	myAct.setComLib(activity_data["ComLib"])
	myAct.setEquipementId(activity_data["EquipementId"])

	values = [
		myAct.getActCode(), 
		myAct.getActLib(), 
		myAct.getComInsee(), 
		myAct.getComLib(), 
		myAct.getEquipementId()
	]

	c1.execute('''INSERT INTO activities VALUES (?, ?, ?, ?, ?)''', values)

print("OK. Création de la table installations...")
c1.execute('''CREATE TABLE IF NOT EXISTS installations
             (ComInsee text, ComLib text, InsCodePostal text,
             	Latitude text, Longitude text)''')

print("OK. Insertion des éléments dans la table installations...")
for installation_data in data_insta["data"]:
	myInsta = Installation(installation_data["ComInsee"])
	myInsta.setComLib(installation_data["ComLib"])
	myInsta.setCodePostal(installation_data["InsCodePostal"])
	myInsta.setLatitude(installation_data["Latitude"])
	myInsta.setLongitude(installation_data["Longitude"])
	myInsta.setl(installation_data["_l"])
	myInsta.setGeo(installation_data["geo"])

	values = [
		myInsta.getComInsee(), 
		myInsta.getComLib(), 
		myInsta.getCodePostal(), 
		myInsta.getLatitude(), 
		myInsta.getLongitude(), 
	]

	c1.execute('''INSERT INTO installations VALUES (?, ?, ?, ?, ?)''', values)

print("OK. Création de la table equipement...")
c1.execute('''CREATE TABLE IF NOT EXISTS equipement
             (ComInsee text, ComLib text, EquipementId text,
              EquipementFiche text)''')

print("OK. Insertion des éléments dans la table equipement...")
for equipement_data in data_equip["data"]:
	myEquip = Equipement(equipement_data["ComInsee"])
	myEquip.setComLib(equipement_data["ComLib"])
	myEquip.setEquipementId(equipement_data["EquipementId"])
	myEquip.setEquipementFiche(equipement_data["EquipementFiche"])

	values = [
		myEquip.getComInsee(), 
		myEquip.getComLib(), 
		myEquip.getEquipementId(), 
		myEquip.getEquipementFiche()
	]

	c1.execute('''INSERT INTO equipement VALUES (?, ?, ?, ?)''', values)

print("OK. Fermeture de la connexion.")
connexion.commit()
connexion.close()	