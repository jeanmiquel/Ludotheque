import sqlite3
import datetime
from Jeu import Jeu

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
                                `dateRenduEmprunt` date NOT NULL,
                                `dureePrevueEmprunt` int(3) NOT NULL,
                                PRIMARY KEY (`idEmprunt`),
                                FOREIGN KEY (`idAdherent`) REFERENCES Adherent(`idAdherent`),
                                FOREIGN KEY (`idExtension`) REFERENCES Extension(`idExtension`),
                                FOREIGN KEY (`idJeu`) REFERENCES Jeu(`idJeu`)
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
        def setDateRenduEmprunt(idEmprunt, dateRenduEmprunt) :    
                cur.execute("""UPDATE Emprunt SET dateRenduEmprunt = ? WHERE idEmprunt = ?""",
                                (dateRenduEmprunt, idEmprunt))
                conn.commit()
        
        @staticmethod
        def setDureePrevue(idEmprunt, dureePrevueEmprunt) :  
                cur.execute("""UPDATE Emprunt SET dureePrevueEmprunt = ? WHERE idEmprunt = ?""",
                                (dureePrevue, idEmprunt))
                conn.commit()


        #getters ?
        
        @staticmethod 
        def getIdEmprunt(idAdherent):
                cur.execute("""SELECT idEmprunt FROM Emprunt WHERE idAdherent =?""",(idAdherent,))
                return cur.fetchone()[0]
        
        @staticmethod 
        def getDateDebutEmprunt(idEmprunt):
                cur.execute("""SELECT dateDebutEmprunt FROM Emprunt WHERE idEmprunt = ?""",
                                (idEmprunt,))
                return cur.fetchone()[0]
                
        @staticmethod 
        def getDateRenduEmprunt(idEmprunt):
                cur.execute("""SELECT dateRenduEmprunt FROM Emprunt WHERE idEmprunt = ?""",
                                (idEmprunt,))
                return cur.fetchone()[0]
        
        @staticmethod  
        def getDateFinEmprunt(idEmprunt):
                dateFin = Emprunt.getDateDebutEmprunt(idEmprunt).day + Emprunt.getDureePrevue(idEmprunt)
                return dateFin
        
        @staticmethod 
        def getIdJeuEmprunt(idEmprunt):
                cur.execute("""SELECT idJeu FROM Emprunt WHERE idEmprunt = ?""",(idEmprunt,))
                return cur.fetchone()[0]
        
        @staticmethod
        def getIdAdherentEmprunt(idEmprunt):
                cur.execute("""SELECT idAdherent FROM Emprunt WHERE idEmprunt =?""",(idEmprunt,))
                return cur.fetchone()[0]
        
        @staticmethod
        def getIdExtensionEmprunt(idEmprunt):
                cur.execute("""SELECT idExtension FROM Emprunt WHERE idEmprunt = ?""",(idEmprunt,))
                return cur.fetchone()[0]
        
        @staticmethod
        def getDureePrevue(idEmprunt):
                cur.execute("""SELECT dureePrevueEmprunt FROM Emprunt WHERE idEmprunt = ?""",
                                (idEmprunt))
                return cur.fetchone()[0]

        #Fonctions usuelles:
        
        @staticmethod
        def ajoutEmprunt(idJeu, idAdherent, idExtension, dateDebutEmprunt, dureePrevueEmprunt = 7):
          cur.execute("""SELECT MAX(idEmprunt) FROM Emprunt""")
          f = cur.fetchone()[0]
          if (f==None):
            idEmprunt = 1
          else:
            idEmprunt =f+1
            cur.execute("""INSERT INTO Emprunt(
                  idEmprunt, idJeu, idAdherent, idExtension, dateDebutEmprunt, dateRenduEmprunt, dureePrevueEmprunt)
                  VALUES(?, ?, ?, ?, ?, ?)""",
                  (idEmprunt, idJeu, idAdherent, idExtension, dateDebutEmprunt, None, dureePrevueEmprunt)) #7 jours d'emprunt
        
        @staticmethod
        def rendre(idEmprunt):
                
                cur.execute("""DELETE FROM Emprunt WHERE idEmprunt = ?""",
                        (idEmprunt,))
                conn.commit()
                
        
        @staticmethod
        def estEnRetard(idEmprunt):
                return(self.getDateRenduEmprunt(idEmprunt) > self.getDateFinEmprunt(idEmprunt))
                        
