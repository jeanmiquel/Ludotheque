import sqlite3
import datetime

conn = sqlite3.connect("C:\Users\Jean\Desktop\LUDOTHEQUE\Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS `Emprunt` (
                                `idEmprunt` str(6) NOT NULL,
                                `idAdherent` int(6) NOT NULL,
                                `idJeu` int(6) NOT NULL,
                                `idExtension` int(6) NOT NULL,
                                `dateDebutEmprunt` date NOT NULL,
                                `dureePrevue` int(3) NOT NULL,
                                PRIMARY KEY (`idEmprunt`),
                                FOREIGN KEY (`idAdherent`),
                                FOREIGN KEY (`idExtension`),
                                FOREIGN KEY (`idJeu`)
                                )""")
conn.commit()



class Emprunt :
    
	def __init__(self, dataBase = conn):
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
	def getIdEmprunt(self):
		 return self.idEmprunt
	  
	def getDateDebutEmprunt(self):
		 return self.dateDebutEmprunt
	  
	def getDureePrevue(self):
		 return self.dureePrevue

	#Fonctions usuelles:

	def rendre(self):
		self.cursor("""DELETE FROM Emprunt WHERE idEmprunt = ?""",
			(self.idEmprunt))
			
