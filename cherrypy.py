import cherrypy
import sqlite3 
 

class WebManager(object):
	"""
	Exposes web services
	"""
	@cherrypy.expose
	def index(self):
		"""
		Accessible à localhost:8080
			Vous aurez le choix de la base de données dont vous voulez voir les informations
			Ainsi que du service que vous voulez (Connaitre le nombre d'entrées ou toutes les montrer)
		"""
		return """

		<script type='text/javascript'>
			function redirect() { 
				var method = document.getElementById('truc').value; 
				var base = document.getElementById('base').value; 
				if(method == 'Index' && base == 'Equipements') document.location.href='/index_equip';
				else if(method == 'Index' && base == 'Installations') document.location.href='/index_insta'; 
				else if(method == 'Index' && base == 'Activités') document.location.href='/index_act'; 
				else if(method == 'Tout voir' && base == 'Installations') document.location.href='/show_insta'; 
				else if(method == 'Tout voir' && base == 'Equipements') document.location.href='/show_insta'; 
				else if(method == 'Tout voir' && base == 'Activités') document.location.href='/show_act';
			}

			function rechercherActVilles() {
				var ville = document.getElementById('search_ville').value;
				var activity = document.getElementById('search_activity').value;
				document.location.href='/research_acts/?ville='+ville+'&act='+activity;
					
			}
		</script>
		<h1>Bienvenue sur la page principale</h1><br/>
		<h2>Sélectionnez une option et une base de donnée:<br/>
		<form method='POST'>
			<select id='truc'>
				<option>Index</option>
				<option>Tout voir</option>
			</select>
			<select id='base'>
				<option>Equipements</option>
				<option>Installations</option>
				<option>Activités</option>
			</select>
			<input type='button' value='Go !' onclick='redirect()'/> <br/>
			<p>Vous pouvez également chercher toutes les données par ville: </p>
			<a href='/show_villes'>Rechercher par ville</a>
		</form>
		<form>
			<label for='search_ville'>Rechercher une ville: </label> 
			<input type='text' id='search_ville' placeholder='Ex: Nantes'>
			<label for='search_activity'>Rechercher une activité à pratiquer: </label> 

			<input type='text' id='search_activity' placeholder='Ex: Football'>
			<input type='button' value='Go !' onclick='rechercherActVilles()'>
		</form>	
			"""

	@cherrypy.expose
	def index_equip(self):
		"""
		Exposes the number of inputs in table equipement at localhost:8080/index_equip
		"""	
		conn1 = sqlite3.connect('DataBases/SportEnLoireAtlantique.db')
		c1 = conn1.cursor()
		res = 0
		for row in c1.execute('''SELECT * FROM equipement ORDER BY ComInsee'''):
		 	res = res + 1
		return "There are {0} items".format(res)

	@cherrypy.expose
	def index_insta(self):
		"""
		Exposes the number of inputs in table installation at localhost:8080/index_insta
		"""	
		conn1 = sqlite3.connect('DataBases/SportEnLoireAtlantique.db')
		c1 = conn1.cursor()
		res = 0
		for row in c1.execute('''SELECT * FROM installations ORDER BY ComInsee'''):
		 	res = res + 1
		return "There are {0} items".format(res)	
	
	@cherrypy.expose
	def index_act(self):
		"""
		Exposes the number of inputs in table activity at localhost:8080/index_act
		"""	
		conn1 = sqlite3.connect('DataBases/SportEnLoireAtlantique.db')
		c1 = conn1.cursor()
		res = 0
		for row in c1.execute('''SELECT * FROM activities ORDER BY ComInsee'''):
		 	res = res + 1
		return "There are {0} items".format(res)			
	 
	@cherrypy.expose
	def show_equip(self):
		"""
		Exposes entries in table equipement
		"""
		conn1 = sqlite3.connect('DataBases/SportEnLoireAtlantique.db')
		c1 = conn1.cursor()
		res = """<table border='1'>
			<tr>
				<td>Ville</td>
				<td>Code postal</td>
				<td>ID Equipement</td>
				<td>Date de màj</td>
				<td>Fiche Equipement</td>
			</tr>	
		"""
		for row in c1.execute('''SELECT * FROM equipement ORDER BY ComInsee'''):
			res = res + """<tr>
								<td>"""+str(row[0]) + "</td>< td>"+str(row[1])+"</td> <td>"+str(row[2])+"</td><td>"+str(row[3])+"</td></td>"+str(row[4]) +"</td></tr>"""
		res = res + "</table>"

		return res;

	@cherrypy.expose
	def show_insta(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		conn1 = sqlite3.connect('DataBases/SportEnLoireAtlantique.db')
		c1 = conn1.cursor()
		res = "<table border='1' style='width:100%'> <tr><td>Numéro Insee</td> <td>Nom de la ville</td> <td>Code Postal</td></tr>"
		for row in c1.execute('''SELECT * FROM installations ORDER BY ComInsee'''):
			res = res + "<tr><td>"+str(row[0]) + "</td><td>"+ str(row[1]) + "</td><td>"+ str(row[2])+"</td></tr>"
		res = res + "</table>"

		return res;		
	 
	@cherrypy.expose
	def show_act(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		conn1 = sqlite3.connect('DataBases/SportEnLoireAtlantique.db')
		c1 = conn1.cursor()
		res = "<table border='1' style='width:100%'>"
		for row in c1.execute('''SELECT * FROM activities ORDER BY ComInsee'''):
			res = res + "<tr><td>"+str(row) + "</td></tr>"
		res = res + "</table>"

		return res;		

	@cherrypy.expose
	def show_villes(self):
		"""
		Exposes the service at localhost:8080/show_villes/
		"""

		conn1 = sqlite3.connect('DataBases/SportEnLoireAtlantique.db')
		c1 = conn1.cursor()
		res = "<ul>";
		some_list = list()
		for row in c1.execute('''SELECT ComLib FROM installations ORDER BY ComLib'''):
			if row not in some_list:
				res = res + """
					<input type="hidden" id="ville" value="""+str(row[0])+""">
					<li>
					<p  onclick="
						var ville = document.getElementById('ville').value;
						alert(ville);
						document.location.href='/show_act_ville/?ville='+ville;
					">""" +str(row[0])+"</p></li>"
				some_list.append(row)
		res = res + "</ul>"		
		return res;	

	@cherrypy.expose
	def show_act_ville(self, ville):
		conn1 = sqlite3.connect('DataBases/SportEnLoireAtlantique.db')
		c1 = conn1.cursor()
		res = "Activités disponnibles pour "+str(ville)+" :<br/><ul>"
		for row in c1.execute("SELECT ActLib FROM activities WHERE ActLib = '"+str(ville)+"'"):
			res = res + "<li>" + str(row[0]) + "</li>"
		res = res + "</ul>"	
		return res;

	@cherrypy.expose
	def research_acts(self, ville, act):
		"""
		Exposes the researched activities in the researched city at localhost:8080/research_acts/?ville=&act= 
		"""
		conn1 = sqlite3.connect("DataBases/SportEnLoireAtlantique.db")	
		c1 = conn1.cursor()

		res = """<table border='1'>
			<tr>
				<td>Ville</td>
				<td>Code postal de la ville</td>
				<td>Nom de l'activité</td>
			</tr>			
		"""
		for row in c1.execute("SELECT ComInsee, ComLib, ActLib FROM activities where ComLib='"+str(ville)+"'AND ActLib='"+str(act)+"' ORDER BY ComInsee"):
			res = res + "<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td><td>"+str(row[2])+"</td></tr>"
		return res;	




	 
	 
cherrypy.quickstart(WebManager()) 