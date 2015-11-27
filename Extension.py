import datetime
import sqlite3
import Jeu


conn = sqlite3.connect("P:\Ludotheque-master\Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS `Extension`
    (`idExtension` int(6) NOT NULL, 
     `idJeu` int(6) NOT NULL, 
     `nomExtension` varchar(20) NOT NULL, 
     `nbreTotalExtension` int(3) NOT NULL,
     PRIMARY KEY (`idExtension`))""")
conn.commit()
    
class Extension:

     def __init__(self, nomExtension):
                cur.execute("""INSERT INTO Extension(idExtension, idJeu, nomExtension, nbreTotalExtension)
                VALUES(?, ?, ?, ?)""",
                (0, 0, self.nomExtension, 1))
                                    

###SETTERS###
    
     def setIdExtension(self, idExtension):       
            cur.execute("""UPDATE Extension SET idExtension = ? WHERE idExtension = ?""",
                            (idExtension, self.idExtension))
            conn.commit()
 
     def setNomExtension(self,idExtension, nomExtension) :       
            cur.execute("""UPDATE Extension SET nomExtension = ? WHERE idExtension = ?""",
                            (nomExtension, self.idExtension))
            conn.commit()

     def setNbreTotalExtension(self,idExtension, nbreTotalExtension) :       
            cur.execute("""UPDATE Extension SET nbreTotalExtension = ? WHERE idExtension = ?""",
                            (nbreTotalExtension, self.idExtension))
            conn.commit()

###GETTERS###

     def getIdExtension(self,idExtension):
        cur.execute("""SELECT idExtension = ? FROM Extension WHERE idExtension = ?""",
                            (idExtension, self.idExtension))
        return cur.fetchone()
    
     def getNomExtension(self,idExtension):
        cur.execute("""SELECT nomExtension = ? FROM Extension WHERE idExtension = ?""",
                            (nomExtension, self.idExtension))
        return cur.fetchone()
