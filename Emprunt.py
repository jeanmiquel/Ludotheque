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

        #setters ?
        @staticmethod
        def setDateDebutEmprunt(idEmprunt, dateDebutEmprunt) :    
                cur.execute("""UPDATE Emprunt SET dateDebutEmprunt = ? WHERE idEmprunt = ?""",
                                (dateDebutEmprunt, idEmprunt))
                conn.commit()
        
        @staticmethod
        def setDureePrevue(idEmprunt, dureePrevueEmprunt) :  
                cur.execute("""UPDATE Emprunt SET dureePrevueEmprunt = ? WHERE idEmprunt = ?""",
                                (dureePrevue, idEmprunt))
                conn.commit()


        #getters ?
        
        @staticmethod 
        def getIdEmprunt(idAdherent):
                cur.execute("""SELECT idEmprunt FROM Emprunt WHERE idAdherent =?""",(idAdherent))
                return cur.fetchone()[0]
        
        @staticmethod 
        def getDateDebutEmprunt(idEmprunt):
                cur.execute("""SELECT dateDebutEmprunt FROM Emprunt WHERE idEmprunt = ?""",
                                (idEmprunt))
                return cur.fetchone()[0]
        
        @staticmethod  
        def getDateFinEmprunt(idEmprunt):
                dateFin = Emprunt.getDateDebutEmprunt(idEmprunt).day + Emprunt.getDureePrevue(idEmprunt))
                return dateFin
        
        @staticmethod 
        def getIdJeuEmprunt(idEmprunt):
                cur.execute("""SELECT idJeu FROM Emprunt WHERE idEmprunt = ?""",(idEmprunt))
                return cur.fetchone()[0]
        
        @staticmethod
        def getIdAdherentEmprunt(idEmprunt):
                cur.execute("""SELECT idAdherent FROM Emprunt WHERE idEmprunt =?""",(idEmprunt))
                return cur.fetchone()[0]
        
        @staticmethod
        def getIdExtensionEmprunt(idEmprunt):
                cur.execute("""SELECT idExtension FROM Emprunt WHERE idEmprunt = ?""",(idEmprunt))
                return cur.fetchone()[0]
        
        @staticmethod
        def getDureePrevue(idEmprunt):
                cur.execute("""SELECT dureePrevueEmprunt FROM Emprunt WHERE idEmprunt = ?""",
                                (idEmprunt))
                return cur.fetchone()[0]

        #Fonctions usuelles:
        
        @staticmethod
        def ajout(idJeu, idAdherent, idExtension):
          cur.execute("""SELECT MAX(idEmprunt) FROM Emprunt""")
          f = cur.fetchone()[0]
          if (f==None):
            idEmprunt = 1
          else:
            idEmprunt =f+1
            cur.execute("""INSERT INTO Emprunt(
                  idEmprunt, idJeu, idAdherent, idExtension, dateDebutEmprunt, dureePrevueEmprunt)
                  VALUES(?, ?, ?, ?, ?, ?)""",
                  (idEmprunt, idJeu, idAdherent, idExtension, datetime.now(), 7)) #7 jours d'emprunt : a faire
        
        @staticmethod
        def rendre(idEmprunt):
                cur.execute("""DELETE FROM Emprunt WHERE idEmprunt = ?""",
                        (idEmprunt))
                conn.commit()
        
        @staticmethod
        def estEnRetard(idEmprunt):
                return(datetime.now() > Emprunt.getDateFinEmprunt(idEmprunt))
                        
