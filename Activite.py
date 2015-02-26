class Activite(object):

	def __init__(self, ActCode):
		self.ActCode = ActCode

	def getActCode(self):
		return self.ActCode	

	def getActLib(self):
		return self.ActLib	

	def getActNivLib(self):
		return self.ActNivLib	

	def getComInsee(self):
		return self.ComInsee	

	def getLib(self):
		return self.ComLib	

	def getEquActivitePraticable(self):
		return self.EquActivitePraticable	

	def getEquActivitePratique(self):
		return self.EquActivitePratique	

	def getEquActiviteSalleSpe(self):
		return self.EquActiviteSalleSpe	

	def getEquNbEquIdentique(self):
		return self.EquNbEquIdentique	

	def getEquipementId(self):
		return self.EquipementId	

	def setActCode(self, newAC):
		self.ActCode	= newAC

	def setActLib(self, newAL):
		self.ActLib = newAL	

	def getActNivLib(self, newAL):
		self.ActNivLib	= newAL	

	def setComInsee(self, newCI):
		self.ComInsee = newCI	

	def setLib(self, newCL):
		self.ComLib = newCL	

	def setEquActivitePraticable(self, newEAP):
		self.EquActivitePraticable = newEAP	

	def setEquActivitePratique(self, newEAP):
		self.EquActivitePratique = newEAP

	def setEquActiviteSalleSpe(self, newEAS):
		self.EquActiviteSalleSpe = newEAS

	def setEquNbEquIdentique(self, newENI):
		self.EquNbEquIdentique = newENI	

	def setEquipementId(self, newEI):
		self.EquipementId = newEI			

	def __repr__(self):
		return "{} - {} - {} - {} - {} - {} - {} - {} - {}".format(self.ActCode, self.ActLib, self.ComInsee, self.ComLib, self.EquActivitePraticable, self.EquActivitePratique, self.EquActiviteSalleSpe, self.EquNbEquIdentique, self.EquipementId)