import sqlite3
import datetime

conn = sqlite3.connect("P:\Ludotheque-master\Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS `Emprunt` (
                                `idEmprunt` int(6) NOT NULL,
                                `idAdherent` int(6) NOT NULL,
                                `idJeu` int(6) NOT NULL,
                                `idExtension` int(6) NOT NULL,
                                `dateDebutEmprunt` date NOT NULL,
                                `dureePrevueEmprunt` int(3) NOT NULL,
                                PRIMARY KEY (`idEmprunt`),
                                FOREIGN KEY (`idAdherent`),
                                FOREIGN KEY (`idExtension`),
                                FOREIGN KEY (`idJeu`)
                                )""")
conn.commit()



class Emprunt :
    
        def __init__(self):
                cur.execute("""INSERT INTO Emprunt(
                idEmprunt, idJeu, idAdherent, idExtension, dateDebutEmprunt, dureePrevueEmprunt)
                VALUES(?, ?, ?, ?, ?, ?)""",
                (0, 0, 0, 0, datetime.now(), 7)) #7 jours d'emprunt

        #setters ?
        def setIdEmprunt(self, idEmprunt) :       
                cur.execute("""UPDATE Emprunt SET idEmprunt = ? WHERE idEmprunt = ?""",
                                (idEmprunt, idEmprunt))
                conn.commit()
         
        def setDateDebutEmprunt(self,idEmprunt, dateDebutEmprunt) :    
                cur.execute("""UPDATE Emprunt SET dateDebutEmprunt = ? WHERE idEmprunt = ?""",
                                (dateDebutEmprunt, idEmprunt))
                conn.commit()

        def setDureePrevue(self,idEmprunt, dureePrevueEmprunt) :  
                cur.execute("""UPDATE Emprunt SET dureePrevueEmprunt = ? WHERE idEmprunt = ?""",
                                (dureePrevue, idEmprunt))
                conn.commit()


        #getters ?
          
        def getDateDebutEmprunt(self, idEmprunt):
                cur.execute("""SELECT dateDebutEmprunt FROM Emprunt WHERE idEmprunt = ?""",
                                (idEmprunt))
                return cur.fetchone()[0]
          
        def getDureePrevue(self, idEmprunt):
                cur.execute("""SELECT dureePrevueEmprunt FROM Emprunt WHERE idEmprunt = ?""",
                                (idEmprunt))
                return cur.fetchone()[0]

        #Fonctions usuelles:

        def rendre(self, idEmprunt):
                cur.execute("""DELETE FROM Emprunt WHERE idEmprunt = ?""",
                        (idEmprunt))
                conn.commit()
                        
