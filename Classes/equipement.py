class Equipement(object):
	
	def __init__(self, cominsee):
		self.comInsee = cominsee

	def getComInsee(self):
		return self.comInsee

	def getComLib(self):
		return self.comLib		

	def getEquipementId(self):
		return self.equipementId

	def getEquipementFiche(self):
		return self.equipementFiche	

	def setComInsee(self, nouv):
		self.comInsee = nouv

	def setComLib(self, nouv):
		self.comLib = nouv	

	def setEquipementId(self, nouv):
		self.equipementId = nouv

	def setEquipementFiche(self, nouv):
		self.equipementFiche = nouv