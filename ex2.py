import sqlite3



def ajouteUtilisateur(pseudo,mdp,spublickey,sprivatekey,epublickey,eprivatekey):
	
	connexion=sqlite3.connect("basededonnee.db")
	# curseur=connexion.cursor()
	connexion.execute('''CREATE TABLE IF NOT EXISTS UTILISATEUR(pseudo TEXT,mdp TEXT,
				spublickey TEXT,sprivatekey TEXT,epublickey TEXT,eprivatekey TEXT)''' )
	donnees=(pseudo,mdp,spublickey,sprivatekey,epublickey,eprivatekey)
	connexion.execute("INSERT INTO UTILISATEUR (pseudo,mdp,spublickey,sprivatekey,epublickey,eprivatekey) VALUES (?,?,?,?,?,?)",donnees)
	connexion.commit()
	connexion.close()