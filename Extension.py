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
     PRIMARY KEY (`idExtension`)
     FOREIGN KEY (`idJeu`) REFERENCES Jeu(`idJeu`))""")
conn.commit()
    
class Extension:

###SETTERS###

    @staticmethod
    def setNomExtension(idExtension, nomExtension) :       
            cur.execute("""UPDATE Extension SET nomExtension = ? WHERE idExtension = ?""",
                            (nomExtension, idExtension))
            conn.commit()
    
    @staticmethod
    def setNbreTotalExtension(idExtension, nbreTotalExtension) :       
            cur.execute("""UPDATE Extension SET nbreTotalExtension = ? WHERE idExtension = ?""",
                            (nbreTotalExtension, idExtension))
            conn.commit()

###GETTERS###

    @staticmethod
    def getIdExtension(nomExtension):
        cur.execute("""SELECT idExtension  FROM Extension WHERE nomExtension = ?""",
                            (nomExtension,))
        return cur.fetchone()[0]
    
    @staticmethod
    def getNomExtension(idExtension):
        cur.execute("""SELECT nomExtension FROM Extension WHERE idExtension = ?""",
                            (idExtension,))
        return cur.fetchone()[0]
    
    @staticmethod         
    def getNbreTotalExtension(idExtension) :
        cur.execute("""SELECT nbreTotalExtension  FROM Extension WHERE idExtension = ?""",
                            (idExtension,))
        return cur.fetchone()[0]
    
    @staticmethod    
    def getIdJeu(idExtension) :
        cur.execute("""SELECT idJeu  FROM Extension WHERE idExtension = ?""",
                            (idExtension,))
        return cur.fetchone()[0]

#Fonctions usuelles:
    def ajout(idJeu, nomExtension, nbreTotalExtension):
        cur.execute("""SELECT MAX(idExtension) FROM Extension""")
        f = cur.fetchone()[0]
        if (f==None):
            idExtension = 1
        else:
            idExtension =f+1
        cur.execute("""INSERT INTO Extension(idExtension, idJeu, nomExtension, nbreTotalExtension)
                    VALUES(?, ?, ?, ?)""",
                    (idExtension, idJeu, nomExtension, nbreTotalExtension))
