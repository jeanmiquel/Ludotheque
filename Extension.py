import datetime
import sqlite3
from Jeu import Jeu
from Adherent import Adherent

conn = sqlite3.connect("C:\Users\Jean\Desktop\LUDOTHEQUE\Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Extension (
 idExtension int(6) NOT NULL, 
 idJeu int(6) NOT NULL, 
 nomExtension varchar(20) NOT NULL, 
 nbreTotalExtension int(3) NOT NULL
 PRIMARY KEY (idExtension),
 FOREIGN KEY (idJeu))""")

class Extension:

 def __init__(self, nomExtension, nbreTotalExtension, database = conn):
      self.cursor = dataBase.cursor()
    		self.Table = "Extension"

    		self.cursor.execute("""INSERT INTO Extension(
		idExtension, idJeu, nomExtension, nbreTotalExtension)
		VALUES(?, ?, ?, ?)""",
    (self.idExtension, self.idJeu, self.nomExtension, self.nbreTotalExtension)
    
 def setIdExtension(self, idExtension) :       
    		self.cursor.execute("""UPDATE Extension SET idExtension = ? WHERE idExtension = ?""",
                        	(idExtension, self.idExtension))
    		self.idExtension = idExtension
    		return self
   	 
	def setNomExtension(self, nomExtension) :       
    		self.cursor.execute("""UPDATE Extension SET nomExtension = ? WHERE idExtension = ?""",
                        	(nomExtension, self.idExtension))
    		return self

	def setNbreTotalExtension(self, nbreTotalExtension) :       
    		self.cursor.execute("""UPDATE Extension SET nbreTotalExtension = ? WHERE idExtension = ?""",
                        	(nbreTotalExtension, self.idExtension))
    		return self

def getIdExtension(self):
		self.cursor.execute("""SELECT idExtension = ? FROM Extension WHERE idExtension = ?""",
                        	(idExtension, self.idExtension))
                return cursor.fetchone()
        def getNomExtension(self):
		self.cursor.execute("""SELECT nomExtension = ? FROM Extension WHERE idExtension = ?""",
                        	(nomExtension, self.idExtension))
                return cursor.fetchone()
                
