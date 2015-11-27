import sqlite3
import datetime
from Extension import Extension
from Adherent import Adherent

conn = sqlite3.connect("C:\Users\Jean\Desktop\LUDOTHEQUE\Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS `Jeu` (
`idJeu` int(6) NOT NULL,
`nomJeu` varchar(50) NOT NULL,
`anneeJeu` int(4) NOT NULL,
`nbJoueurJeu` varchar(5) NOT NULL,
`quantiteJeu` int(3) NOT NULL,
`editeurJeu` varchar(20) NOT NULL,
`estEmpruntableJeu` tinyint(1) NOT NULL,
`synopsisJeu` varchar(200) NOT NULL,
PRIMARY KEY (`idJeu`)
)""")


class Jeu :
    
	def __init__(self, nomJeu : str, anneeJeu : int, dataBase = conn):
    		self.cursor = dataBase.cursor()
    		self.Table = "Jeu"
    		self.idJeu = str(str(nomJeu) + str(anneeJeu))

    		self.cursor.execute("""INSERT INTO Jeu(
		idJeu, nomJeu, anneeJeu, nbJoueurJeu,
		quantiteJeu, editeurJeu, estEmpruntableJeu, synopsisJeu)
		VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
                        	(self.idJeu, nomJeu, anneeJeu,
                         	" ", 0, " ", False, " "))

	#setters ?
	def setIdJeu(self, idJeu : str) :       	#On modifie l'id du jeu, dans l'objet et dans la BD
    		self.cursor.execute("""UPDATE Jeu SET idJeu = ? WHERE idJeu = ?""",
                        	(idJeu, self.idJeu))
    		self.idJeu = idJeu
    		return self
   	 
	def setNomJeu(self, nomJeu : str) :     	#On modifie le nom du jeu dans la DB et donc son id
    		anneeJeu = self.getAnneeJeu()
    		self.cursor.execute("""UPDATE Jeu SET nomJeu = ? WHERE idJeu = ?""",
                        	(nomJeu, self.idJeu))
    		self.setIdJeu(str(str(nomJeu) + str(anneeJeu)))
    		return self

	def setAnneeJeu(self, anneeJeu : int) : 	#On modifie la date du jeu, et donc son id
    		nomJeu = self.getNomJeu()
    		self.cursor.execute("""UPDATE Jeu SET anneeJeu = ? WHERE idJeu = ?""",
                        	(anneeJeu, self.idJeu))
    		self.setIdJeu(str(str(nomJeu) + str(anneeJeu)))
    		return self

	def setNbJoueurJeu(self, nbJoueurJeu : str):
    		self.cursor.execute(""" UPDATE Jeu SET nbJoueurJeu = ? WHERE idJeu = ?""",(nbJoueurJeu,self.idJeu))
    		return self

	def setQuantiteJeu(self, quantiteJeu : int) :
    		self.cursor.execute("""UPDATE Jeu SET quantiteJeu = ? WHERE idJeu = ?""",(quantiteJeu, self.idJeu))
    		return self

	def setEditeurJeu(self, editeurJeu : str) :
    		self.cursor.execute("""UPDATE Jeu SET editeurJeu = ? WHERE idJeu = ?""",(editeurJeu, self.idJeu))
    		return self

	def setEmpruntable(self, booleen : bool):
    		self.cursor.execute("""UPDATE Jeu SET estEmpruntableJeu = ? WHERE idJeu = ?""",(booleen, self.idJeu))
    		return self

	def setSynopsisJeu(self, synopsisJeu : str):
    		self.cursor.execute("""UPDATE Jeu SET synopsisJeu = ? WHERE idJeu = ?""",(synopsisJeu, self.idJeu))
    		return self
 


	#getter
	
	def getInfoJeu(self) :                  	#Saisir tout d'un coup
    		"""0 Id, 1 Nom, 2 AnnÃ©e, 3 NbJoueur, 4 QuantitÃ©, 5 Editeur, 6 Empruntable, 7 Synospis"""
    		self.cursor.execute("""SELECT
		idJeu, nomJeu, anneeJeu, nbJoueurJeu,
		quantiteJeu, editeurJeu, estEmpruntableJeu, synopsisJeu
		FROM Jeu Where idJeu = ?""",(self.idJeu,))
    		return self.cursor.fetchone()
    
	def getIdJeu(self) : 
		return str(self.idJeu) #L'id est accessible dans les attributs

	def getNomJeu(self) :
                #Le nom est stockÃ© dans la BD
                self.cursor.execute("""SELECT nomJeu FROM WHERE idJeu = ?""",(self.idJeu))
    		return cursor.fetchone()

	def getAnneeJeu(self) :         #L'annee est stokÃ© dans la DB
    		self.cursor.execute("""SELECT anneeJeu FROM WHERE idJeu = ?""",(self.idJeu))
    		return cursor.fetchone()
    	
	def getNbJoueurJeu(self) :
    		self.cursor.execute("""SELECT nbJoueurJeu FROM WHERE idJeu = ?""",(self.idJeu))
    		return cursor.fetchone()

	def getQuantiteJeu(self):
    		self.cursor.execute("""SELECT quantiteJeu FROM WHERE idJeu = ?""",(self.idJeu))
    		return cursor.fetchone()

	def getEditeurJeu(self):
    		self.cursor.execute("""SELECT editeurJeu FROM WHERE idJeu = ?""",(self.idJeu))
    		return cursor.fetchone()

	def estEmpruntable(self):
    		self.cursor.execute("""SELECT estEmpruntableJeu FROM WHERE idJeu = ?""",(self.idJeu))
    		return cursor.fetchone()

	def getSynopsisJeu(self):
    		self.cursor.execute("""SELECT synopsisJeu FROM WHERE idJeu = ?""",(self.idJeu))
    		return cursor.fetchone()

	#Fonctions usuelles:

	def ajoutExemplaire(self):
    		return self.setQuantiteJeu(self.getQuantiteJeu()+1)

	def retraitExemplaire(self):
    		return self.setQuantiteJeu(min(self.getQuantiteJeu()-1,0))

	def changeEmpruntable(self):
    		return self.setEmpruntable(not self.estEmpruntable())
    
	def supprimerJeu(self):
    		cursor.execute("""DELETE FROM Jeu WHERE idJeu""",(self.idJeu,))
    		return self

