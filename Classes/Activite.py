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

	def getEquActivitePratique(self):
		return self.EquActivitePratique	

	def getEquipementId(self):
		return self.EquipementId	

	def setActCode(self, nouv):
		self.ActCode	= nouv

	def setActLib(self, nouv):
		self.ActLib	= nouv

	def setActNivLib(self, nouv):
		self.ActNivLib = nouv

	def setComInsee(self, nouv):
		self.ComInsee = nouv

	def setLib(self, nouv):
		self.ComLib = nouv

	def setEquActivitePratique(self, nouv):
		self.EquActivitePratique	= nouv

	def setEquipementId(self, nouv):
		self.EquipementId= nouv	