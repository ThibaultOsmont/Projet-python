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

	def getCodePostal(self):
		return self.InsCodePostal	

	def getLatitude(self):
		return self.Latitude

	def getLongitude(self):
		return self.Longitude

	def getl(self):
		return self._l

	def getGeo(self):
		return self.geo

	def setComInsee(self, nouv):
		self.ComInsee = nouv
	
	def setComLib(self, nouv):
		self.ComLib = nouv

	def setCodePostal(self, nouv):
		self.InsCodePostal = nouv	
	
	def setLatitude(self, nouv):
		self.Latitude = nouv
	
	def setLongitude(self, nouv):
		self.Longitude = nouv

	def setl(self, nouv):
		self._l = nouv
	
	def setGeo(self, nouv):
		self.geo = nouv
	