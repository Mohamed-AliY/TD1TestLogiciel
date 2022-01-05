import unittest
import ex2
import sqlite3

class TestEx2(unittest.TestCase):

	def test_ajouteUtilisateur(self):
		ex2.ajouteUtilisateur("toti","dzxhf215","vdv","gsg","fsv","fsd")
		connexion=sqlite3.connect("basededonnee.db")
		cursor=connexion.execute("SELECT * FROM UTILISATEUR")
		for row in cursor:
			print("pseudo = ", row[0])
			print("mdp = ", row[1])
			print("spublickey = ", row[2])
			print("sprivatekey = ", row[3])
			print("epublickey = ", row[4])
			print("eprivatekey = ", row[5], "\n")

if __name__ == '__main__':
    unittest.main()