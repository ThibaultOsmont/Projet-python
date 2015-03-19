import cherrypy
import json
import sqlite3 
 

class WebManager(object):
	"""
	Exposes web services
	"""
	@cherrypy.expose
	def index(self):
		"""
		Exposes the service at localhost:8080/
		"""
		return "<script type='text/javascript'>function redirect(){ var method = document.getElementById('truc').value; var base = document.getElementById('base').value; if(method == 'Index' && base == 'Equipements') {alert('ducon'); document.location.href='/index_equip';} else if(method == 'Index' && base == 'Installations') document.location.href='/index_insta'; else if(method == 'Index' && base == 'Activités') document.location.href='/index_act'; else if(method == 'show_all' && base == 'Installations') document.location.href='/show_insta'; else if(method == 'show_all' && base == 'Equipements') document.location.href='/show_insta'; else if(method == 'show_all' && base == 'Activités') document.location.href='/show_act';}</script><h1>Bienvenue sur la page principale</h1><br/><h2>Sélectionnez une optionn et une base de donnée:<br/><form method='POST'><select id='truc'><option>Index</option><option>show_all</option></select><select id='base'><option>Equipements</option><option>Installations</option><option>Activités</option></select><input type='button' value='Go !' onclick='redirect()'/></form>"

	@cherrypy.expose
	def index_equip(self):
		"""
		Exposes the numbur of inputs in table equipement
		"""	
		conn1 = sqlite3.connect('equipement.db')
		c1 = conn1.cursor()
		res = 0
		for row in c1.execute('''SELECT * FROM equipement ORDER BY ComInsee'''):
		 	res = res + 1
		return "There are {0} items".format(res)

	@cherrypy.expose
	def index_insta(self):
		"""
		Exposes the numbur of inputs in table installation
		"""	
		conn1 = sqlite3.connect('installation.db')
		c1 = conn1.cursor()
		res = 0
		for row in c1.execute('''SELECT * FROM installation ORDER BY ComInsee'''):
		 	res = res + 1
		return "There are {0} items".format(res)	
	
	@cherrypy.expose
	def index_act(self):
		"""
		Exposes the numbur of inputs in table activity
		"""	
		conn1 = sqlite3.connect('activity.db')
		c1 = conn1.cursor()
		res = 0
		for row in c1.execute('''SELECT * FROM activity ORDER BY ComInsee'''):
		 	res = res + 1
		return "There are {0} items".format(res)			
	 
	@cherrypy.expose
	def show_equip(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		conn1 = sqlite3.connect('equipement.db')
		c1 = conn1.cursor()
		res = "<table border='1' style='width:100%'>"
		for row in c1.execute('''SELECT * FROM equipement ORDER BY ComInsee'''):
			res = res + "<tr><td>"+str(row) + "<td></tr>"
		res = res + "</table>"

		return res;

	@cherrypy.expose
	def show_insta(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		conn1 = sqlite3.connect('installations.db')
		c1 = conn1.cursor()
		res = "<table border='1' style='width:100%'>"
		for row in c1.execute('''SELECT * FROM installations ORDER BY ComInsee'''):
			res = res + "<tr><td>"+str(row) + "<td></tr>"
		res = res + "</table>"

		return res;		
	 
	@cherrypy.expose
	def show_act(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		conn1 = sqlite3.connect('activity.db')
		c1 = conn1.cursor()
		res = "<table border='1' style='width:100%'>"
		for row in c1.execute('''SELECT * FROM activity ORDER BY ComInsee'''):
			res = res + "<tr><td>"+str(row) + "<td></tr>"
		res = res + "</table>"

		return res;		

	@cherrypy.expose
	def show(self, id):
		"""
		Exposes the service at localhost:8080/show/[id]/
		"""
		try:
			item = data[int(id)]
		except (IndexError, IOError):
			return "Invalid ID"
		 
		return json.dumps(item)
	 
	 
cherrypy.quickstart(WebManager()) 