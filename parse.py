import json

json_data = open('activite.json')
data = json.load(json_data)
#print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
realData = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

for truc in realData:
	s = ""
	if(truc != "\""):
		s += (truc)
	print (s)		