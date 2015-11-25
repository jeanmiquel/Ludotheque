import datetime
import sqlite3
from Jeu import Jeu
from Adherent import Adherent

conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Extension (
 idExt str(6) NOT NULL, 
 idJeu str(6) NOT NULL, 
 nomExt varchar(20) NOT NULL, 
 nbreTotalExt int(3) NOT NULL)""")

class Extension:

 def __init__(self, nomExt : str, nbreTotalExt : int, database = conn):
      self.cursor = dataBase.cursor()
    		self.Table = "Extension"

    		self.cursor.execute("""INSERT INTO Extension(
		idExt, idJeu, nomExt, nbreTotalExt)
		VALUES(?, ?, ?, ?)""",
    (self.idExt, self.idJeu, self.nomExt, self.nbreTotalExt)
    
 def setIdExt(self, idExt : str) :       
    		self.cursor.execute("""UPDATE Extension SET idExt = ? WHERE idExt = ?""",
                        	(idExt, self.idExt))
    		self.idExt = idExt
    		return self
   	 
	def setNomExt(self, nomExt : str) :       
    		self.cursor.execute("""UPDATE Extension SET nomExt = ? WHERE idExt = ?""",
                        	(nomExt, self.idExt))
    		return self

	def setNbreTotalExt(self, nbreTotalExt : str) :       
    		self.cursor.execute("""UPDATE Extension SET nbreTotalExt = ? WHERE idExt = ?""",
                        	(nbreTotalExt, self.idExt))
    		return self
