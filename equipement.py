class Equipement(object):
	
	def __init__(self, cominsee):
		self.comInsee = cominsee

	def getComInsee(self):
		return self.comInsee

	def getComLib(self):
		return self.comLib		

	def getEquipementId(self):
		return self.equipementId

	def	getAnneeServiceLib(self):
		return self.anneServiceLib

	def getEquipementFiche(self):
		return self.equipementFiche	

	def setComInsee(self, new):
		self.comInsee = new

	def setComLib(self, new):
		self.comLib = new	

	def setEquipementId(self, new):
		self.equipementId = new

	def	setAnneeServiceLib(self, new):
		self.anneeServiceLib = new

	def setEquipementFiche(self, new):
		self.equipementFiche	= new	