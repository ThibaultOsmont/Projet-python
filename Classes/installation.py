import codecs
import json
import sqlite3
class Installation(object):

	def __init__(self, ComInsee):
		self.ComInsee = ComInsee

	def getComInsee(self):
		return self.ComInsee

	def getComLib(self):
		return self.ComLib

	def getLatitude(self):
		return self.Latitude

	def getLongitude(self):
		return self.Longitude

	def getNb_Equipements(self):
		return self.Nb_Equipements

	def getNb_FicheEquipement(self):
		return self.Nb_FicheEquipement

	def getl(self):
		return self._l

	def getGeo(self):
		return self.geo

	def setComInsee(self, nouv):
		self.ComInsee = nouv
	
	def setComLib(self, nouv):
		self.ComLib = nouv
	
	def setLatitude(self, nouv):
		self.Latitude = nouv
	
	def setLongitude(self, nouv):
		self.Longitude = nouv
	
	def setNbEquip(self, nouv):
		self.Nb_Equipements = nouv
	
	def setNbFiche(self, nouv):
		self.Nb_FicheEquipement = nouv
	
	def setl(self, nouv):
		self._l = nouv
	
	def setGeo(self, nouv):
		self.geo = nouv
	