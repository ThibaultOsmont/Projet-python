class Activite(object):

	def __init__(self, ActCode):
		self.ActCode = ActCode

	def getActCode(self):
		return self.ActCode	

	def getActLib(self):
		return self.ActLib	

	def getComInsee(self):
		return self.ComInsee	

	def getComLib(self):
		return self.ComLib	

	def getEquipementId(self):
		return self.EquipementId	

	def setActCode(self, nouv):
		self.ActCode	= nouv

	def setActLib(self, nouv):
		self.ActLib	= nouv

	def setComInsee(self, nouv):
		self.ComInsee = nouv

	def setComLib(self, nouv):
		self.ComLib = nouv

	def setEquipementId(self, nouv):
		self.EquipementId= nouv	