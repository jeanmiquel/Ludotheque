import sqlite3

BD = sqlite3.connect(':memory:')

cursor = BD.cursor()
#idjeu int > varchar pour concatener le nom et l annee pour une id simple
cursor.execute("""
CREATE TABLE IF NOT EXISTS `Jeu` (
`idJeu` varchar(54) NOT NULL,
`nomJeu` varchar(50) NOT NULL,
`anneeJeu` int(4) NOT NULL,
`nbJoueurJeu` varchar(5) NOT NULL,
`quantiteJeu` int(3) NOT NULL,
`editeurJeu` varchar(20) NOT NULL,
`estEmpruntableJeu` tinyint(1) NOT NULL,
`synopsisJeu` varchar(200) NOT NULL,
PRIMARY KEY (`idJeu`))""")



class Jeu :
    
	def __init__(self, nomJeu : str, anneeJeu : int, dataBase = BD):
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
 

	#getters ?
	def getInfoJeu(self) :                  	#Saisir tout d'un coup
    	"""0 Id, 1 Nom, 2 Année, 3 NbJoueur, 4 Quantité, 5 Editeur, 6 Empruntable, 7 Synospis"""
    	self.cursor.execute("""SELECT
	idJeu, nomJeu, anneeJeu, nbJoueurJeu,
	quantiteJeu, editeurJeu, estEmpruntableJeu, synopsisJeu
	FROM Jeu Where idJeu = ?""",(self.idJeu,))
    	return self.cursor.fetchone()
    
	def getIdJeu(self) : return str(self.idJeu) #L'id est accessible dans les attributs

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

