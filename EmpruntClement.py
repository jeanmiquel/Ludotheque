from sqlite3 import sqlite3
from datetime import datetime

BD = sqlite3.connect(':memory:')

CREATE TABLE IF NOT EXISTS `Emprunt` (
`idEmprunt` str(6) NOT NULL,
`idAdherent` int(6) NOT NULL,
`idJeu` int(6) NOT NULL,
`idExtension` int(6) NOT NULL,
`dateDebutEmprunt` date NOT NULL,
`dureePrevue` int(3) NOT NULL,
KEY `fk_idAdherent` (`idAdherent`),
KEY `fk_idExtension` (`idExtension`),
KEY `fk_idJeu` (`idJeu`)
)


class Emprunt :
    
	def __init__(self, dataBase = BD):
    		self.cursor = dataBase.cursor()
    		self.Table = "Emprunt"

    		self.cursor.execute("""INSERT INTO Emprunt(
		idEmprunt, idJeu, idAdh, idExt, dateDebutEmprunt, dureePrevue)
		VALUES(?, ?, ?, ?, ?, ?)""",
    (self.idEmprunt, self.idJeu, self.idAdh,
   	date, 14)) #14 jours

	#setters ?
	def setIdEmprunt(self, idEmprunt : str) :       
    		self.cursor.execute("""UPDATE Emprunt SET idEmprunt = ? WHERE idEmprunt = ?""",
                        	(idEmprunt, self.idEmprunt))
    		self.idEmprunt = idEmprunt
    		return self
   	 
	def setDateDebutEmprunt(self, dateDebutEmprunt : date) :    
    		self.cursor.execute("""UPDATE Emprunt SET dateDebutEmprunt = ? WHERE idEmprunt = ?""",
                        	(dateDebutEmprunt, self.idEmprunt))
    		return self

	def setDureePrevue(self, dureePrevue : int) : 	
    		self.cursor.execute("""UPDATE Emprunt SET dureePrevue = ? WHERE idEmprunt = ?""",
                        	(dureePrevue, self.idEmprunt))
    		return self


	#getters ?
	def getInfoJeu(self) :                  	#Saisir tout d'un coup
    		"""0 Id, 1 Nom, 2 Année, 3 NbJoueur, 4 Quantité, 5 Editeur, 6 Empruntable, 7 Synospis"""
    		self.cursor.execute("""SELECT
		idJeu, nomJeu, anneeJeu, nbJoueurJeu,
		quantiteJeu, editeurJeu, estEmpruntableJeu, synopsisJeu
		FROM Jeu Where idJeu = ?""",(self.idJeu,))
    		return self.cursor.fetchone()
    
	def getIdJeu(self) : 
		return str(self.idJeu) #L'id est accessible dans les attributs

	def getNomJeu(self) :                   	#Le nom est stocké dans la BD
    		return self.getInfoJeu()[1]

	def getAnneeJeu(self) :                 	#L'annee est stoké dans la DB
    		return self.getInfoJeu()[2]

	def getNbJoueurJeu(self) :
    		return self.getInfoJeu()[3]

	def getQuantiteJeu(self):
    		return self.getInfoJeu()[4]

	def getEditeurJeu(self):
    		return self.getInfoJeu()[5]

	def estEmpruntable(self):
    		return bool(self.getInfoJeu()[6])

	def getSynopsisJeu(self):
    		return self.getInfoJeu()[7]

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
