import datetime
import sqlite3
import Jeu

import BDD

BDD.cur.execute("""CREATE TABLE IF NOT EXISTS `Extension`
    (`idExtension` int(6) NOT NULL, 
     `idJeu` int(6) NOT NULL, 
     `nomExtension` varchar(20) NOT NULL, 
     `nbreTotalExtension` int(3) NOT NULL,
     PRIMARY KEY (`idExtension`)
     FOREIGN KEY (`idJeu`) REFERENCES Jeu(`idJeu`))""")
BDD.conn.commit()
    
class Extension:

###SETTERS###

    @staticmethod
    def setNomExtension(idExtension, nomExtension) :       
            BDD.cur.execute("""UPDATE Extension SET nomExtension = ? WHERE idExtension = ?""",
                            (nomExtension, idExtension))
            BDD.conn.commit()
    
    @staticmethod
    def setNbreTotalExtension(idExtension, nbreTotalExtension) :       
            BDD.cur.execute("""UPDATE Extension SET nbreTotalExtension = ? WHERE idExtension = ?""",
                            (nbreTotalExtension, idExtension))
            BDD.conn.commit()

###GETTERS###

    @staticmethod
    def getIdExtension(nomExtension):
        BDD.cur.execute("""SELECT idExtension  FROM Extension WHERE nomExtension = ?""",
                            (nomExtension,))
        return BDD.cur.fetchone()[0]
    
    @staticmethod
    def getNomExtension(idExtension):
        BDD.cur.execute("""SELECT nomExtension FROM Extension WHERE idExtension = ?""",
                            (idExtension,))
        return BDD.cur.fetchone()[0]
    
    @staticmethod         
    def getNbreTotalExtension(idExtension) :
        BDD.cur.execute("""SELECT nbreTotalExtension  FROM Extension WHERE idExtension = ?""",
                            (idExtension,))
        return BDD.cur.fetchone()[0]
    
    @staticmethod    
    def getIdJeu(idExtension) :
        BDD.cur.execute("""SELECT idJeu  FROM Extension WHERE idExtension = ?""",
                            (idExtension,))
        return BDD.cur.fetchone()[0]

#Fonctions usuelles:

    @staticmethod
    def afficherTableExtension():
        BDD.cur.execute("""SELECT * FROM Extension""")
        return BDD.cur.fetchall()

    @staticmethod
    def ajoutExtension(idJeu, nomExtension, nbreTotalExtension):
        BDD.cur.execute("""SELECT MAX(idExtension) FROM Extension""")
        f = BDD.cur.fetchone()[0]
        if (f==None):
            idExtension = 1
        else:
            idExtension =f+1
        BDD.cur.execute("""INSERT INTO Extension(idExtension, idJeu, nomExtension, nbreTotalExtension)
                    VALUES(?, ?, ?, ?)""",
                    (idExtension, idJeu, nomExtension, nbreTotalExtension))
        BDD.conn.commit()
                    
    @staticmethod
    def supprimerExtension(idExtension):
        BDD.cur.execute("""DELETE FROM Extension WHERE idExtension = ?""",(idExtension,))
        BDD.conn.commit()
