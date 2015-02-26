class Installation(object):

	def __init__(self, ComInsee):
		self.ComInsee = ComInsee

	def getComInsee(self):
		return self.ComInsee

	def getComLib(self):
		return self.ComLib

	def getInsAccessibiliteAucun(self):
		return self.InsAccessibiliteAucun	

	def getInsAccessibiliteHandiMoteur(self):
		return self.InsAccessibiliteHandiMoteur

	def getInsAccessibiliteHandiSens(self):
		return self.InsAccessibiliteHandiSens

	def getInsCodePostal(self):
		return self.InsCodePostal

	def getInsDateMaj(self):
		return self.InsDateMaj

	def getInsEmpriseFonciere(self):
		return self.InsEmpriseFonciere

	def getInsGardiennee(self):
		return self.InsGardiennee

	def getInsLibelleVoie(self):
		return self.InsLibelleVoie

	def getInsLieuDit(self):
		return self.InsLieuDit

	def getInsMultiCommune(self):
		return self.InsMultiCommune

	def getInsNbPlaceParking(self):
		return self.InsNbPlaceParking

	def getInsNbPlaceParkingHandi(self):
		return self.InsNbPlaceParkingHandi

	def getInsNoVoie(self):
		return self.InsNoVoie

	def getInsNumeroInstall(self):
		return self.InsNumeroInstall

	def getInsPartLibelle(self):
		return self.InsPartLibelle

	def getInsTransportAutre(self):
		return self.InsTransportAutre

	def getInsTransportBateau(self):
		return self.InsTransportBateau

	def getInsTransportBus(self):
		return self.InsTransportBus

	def getInsTransportMetro(self):
		return self.InsTransportMetro

	def getInsTransportTrain(self):
		return self.InsTransportTrain

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

	def setComInsee(self, new):
		self.ComInsee = new

	def setComLib(self, new):
		self.ComLib = new

	def setInsAccessibiliteAucun(self, new):
		self.InsAccessibiliteAucun	= new

	def setInsAccessibiliteHandiMoteur(self, new):
		self.InsAccessibiliteHandiMoteur = new

	def setInsAccessibiliteHandiSens(self, new):
		self.InsAccessibiliteHandiSens = new

	def setInsCodePostal(self, new):
		self.InsCodePostal = new

	def setInsDateMaj(self, new):
		self.InsDateMaj = new

	def setInsEmpriseFonciere(self, new):
		self.InsEmpriseFonciere = new

	def setInsGardiennee(self, new):
		self.InsGardiennee = new

	def setInsLibelleVoie(self, new):
		self.InsLibelleVoie = new

	def setInsLieuDit(self, new):
		self.InsLieuDit = new

	def setInsMultiCommune(self, new):
		self.InsMultiCommune = new

	def setInsNbPlaceParking(self, new):
		self.InsNbPlaceParking = new

	def setInsNbPlaceParkingHandi(self, new):
		self.InsNbPlaceParkingHandi = new

	def setInsNoVoie(self, new):
		self.InsNoVoie = new

	def setInsNumeroInstall(self, new):
		self.InsNumeroInstall = new

	def setInsPartLibelle(self, new):
		self.InsPartLibelle = new

	def setInsTransportAutre(self, new):
		self.InsTransportAutre = new

	def setInsTransportBateau(self, new):
		self.InsTransportBateau = new

	def setInsTransportBus(self, new):
		self.InsTransportBus = new

	def setInsTransportMetro(self, new):
		self.InsTransportMetro = new

	def setInsTransportTrain(self, new):
		self.InsTransportTrain = new

	def setLatitude(self, new):
		self.Latitude = new

	def setLongitude(self, new):
		self.Longitude = new

	def setNb_Equipements(self, new):
		self.Nb_Equipements = new

	def setNb_FicheEquipement(self, new):
		self.Nb_FicheEquipement = new

	def setl(self, new):
		self._l = new

	def setGeo(self, new):
		self.geo = new

	def __repr__(self):
		return "{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(self.ComInsee,
																																						self.ComLib,
																																						self.InsAccessibiliteAucun,	
																																						self.InsAccessibiliteHandiMoteur,
																																						self.InsAccessibiliteHandiSens,
																																						self.InsCodePostal,
																																						self.InsDateMaj,
																																						self.InsEmpriseFonciere,
																																						self.InsGardiennee,
																																						self.InsLibelleVoie,
																																						self.InsLieuDit,
																																						self.InsMultiCommune,
																																						self.InsNbPlaceParking,
																																						self.InsNbPlaceParkingHandi,
																																						self.InsNoVoie,
																																						self.InsNumeroInstall,
																																						self.InsPartLibelle,
																																						self.InsTransportAutre,
																																						self.InsTransportBateau,
																																						self.InsTransportBus,
																																						self.InsTransportMetro,
																																						self.InsTransportTrain,
																																						self.Latitude,
																																						self.Longitude,
																																						self.Nb_Equipements,
																																						self.Nb_FicheEquipement,
																																						self._l,
																																						self.geo)