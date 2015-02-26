import json
from Activite import Activite
from installation import Installation

json_data = open('activite.json')
data = json.load(json_data)
#print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
#realData = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

for activity_data in data["data"]:

	activity = Activite(activity_data["ActCode"])
	activity.setActLib(activity_data["ActLib"])
	activity.setComInsee(activity_data["ComInsee"])
	activity.setLib(activity_data["ComLib"])
	activity.setEquActivitePraticable(activity_data["EquActivitePraticable"])
	activity.setEquActivitePratique(activity_data["EquActivitePratique"])
	activity.setEquActiviteSalleSpe(activity_data["EquActiviteSalleSpe"])
	activity.setEquNbEquIdentique(activity_data["EquNbEquIdentique"])
	activity.setEquipementId(activity_data["EquipementId"])

json_data_2 = open('installations.json')
data2 = json.load(json_data_2)

for installation_data in data2["data"]:
	insta = Installation(installation_data["ComInsee"])
	insta.setComLib(installation_data["ComLib"])
	insta.setInsAccessibiliteAucun(installation_data["InsAccessibiliteAucun"])
	insta.setInsAccessibiliteHandiMoteur(installation_data["InsAccessibiliteHandiMoteur"])
	insta.setInsAccessibiliteHandiSens(installation_data["InsAccessibiliteHandiSens"])
	insta.setInsCodePostal(installation_data["InsCodePostal"])
	insta.setInsDateMaj(installation_data["InsDateMaj"])
	insta.setInsEmpriseFonciere(installation_data["InsEmpriseFonciere"])
	insta.setInsGardiennee(installation_data["InsGardiennee"])
	insta.setInsLibelleVoie(installation_data["InsLibelleVoie"])
	insta.setInsLieuDit(installation_data["InsLieuDit"])
	insta.setInsMultiCommune(installation_data["InsMultiCommune"])
	insta.setInsNbPlaceParking(installation_data["InsNbPlaceParking"])
	insta.setInsNbPlaceParkingHandi(installation_data["InsNbPlaceParkingHandi"])
	insta.setInsNoVoie(installation_data["InsNoVoie"])
	insta.setInsNumeroInstall(installation_data["InsNumeroInstall"])
	insta.setInsPartLibelle(installation_data["InsPartLibelle"])
	insta.setInsTransportAutre(installation_data["InsTransportAutre"])
	insta.setInsTransportBateau(installation_data["InsTransportBateau"])
	insta.setInsTransportBus(installation_data["InsTransportBus"])
	insta.setInsTransportMetro(installation_data["InsTransportMetro"])
	insta.setInsTransportTrain(installation_data["InsTransportTrain"])
	insta.setLatitude(installation_data["Latitude"])
	insta.setLongitude(installation_data["Longitude"])
	insta.setNb_Equipements(installation_data["Nb_Equipements"])
	insta.setNb_FicheEquipement(installation_data["Nb_FicheEquipement"])
	insta.setl(installation_data["_l"])
	insta.setGeo(installation_data["geo"])