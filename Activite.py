class Activite(object):

	ActCode
	ActLib
	ComInsee
	ComLib
	EquActivitePraticable
	EquActivitePratique
	EquActiviteSalleSpe
	EquNbEquIdentique
	EquipementId

	def __init__(self, ActCode, ActLib, ActNivLib, ComInsee, ComLib, EquActivitePraticable, EquActivitePratique, EquActiviteSalleSpe, EquNbEquIdentique, EquipementId):
		self.ActCode = ActCode
		self.ActLib = ActLib
		self.ComInsee = ComInsee
		self.ComLib = ComLib
		self.EquActivitePraticable = EquActivitePraticable
		self.EquActivitePratique = EquActivitePratique
		self.EquActiviteSalleSpe = EquActiviteSalleSpe
		self.EquNbEquIdentique = EquNbEquIdentique
		self.EquipementId = EquipementId

	def getActCode(self):
		return self.ActCode	

	def getActLib(self):
		return self.ActLib	

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
		return self.ActCode	= newAC

	def setActLib(self, newAL):
		return self.ActLib = newAL	

	def setComInsee(self, newCI):
		return self.ComInsee = newCI	

	def setLib(self, newCL):
		return self.ComLib = newCL	

	def setEquActivitePraticable(self, newEAP):
		return self.EquActivitePraticable = newEAP	

	def setEquActivitePratique(self, newEAP):
		return self.EquActivitePratique	= newEAP

	def setEquActiviteSalleSpe(self, newEAS):
		return self.EquActiviteSalleSpe	= newEAS

	def setEquNbEquIdentique(self, newENI):
		return self.EquNbEquIdentique = newENI	

	def setEquipementId(self, newEI):
		return self.EquipementId = newEI			