#-*- coding: utf-8 -*-
import sqlite3
import datetime
from Jeu import Jeu
from Adherent import Adherent
from Extension import Extension
from datetime import timedelta

import BDD


BDD.cur.execute("""CREATE TABLE IF NOT EXISTS `Emprunt` (
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
BDD.conn.commit()



class Emprunt :

        #setters ?
        @staticmethod
        def setDateDebutEmprunt(idEmprunt, dateDebutEmprunt) :    
                BDD.cur.execute("""UPDATE Emprunt SET dateDebutEmprunt = ? WHERE idEmprunt = ?""",
                                (dateDebutEmprunt, idEmprunt))
                BDD.conn.commit()
                
        @staticmethod
        def setDateRenduEmprunt(idEmprunt, dateRenduEmprunt) :    
                BDD.cur.execute("""UPDATE Emprunt SET dateRenduEmprunt = ? WHERE idEmprunt = ?""",
                                (dateRenduEmprunt, idEmprunt))
                BDD.conn.commit()
        
        @staticmethod
        def setDureePrevue(idEmprunt, dureePrevueEmprunt) :  
                BDD.cur.execute("""UPDATE Emprunt SET dureePrevueEmprunt = ? WHERE idEmprunt = ?""",
                                (dureePrevue, idEmprunt))
                BDD.conn.commit()


        #getters ?
        
        
        @staticmethod 
        def getIdEmprunt(idAdherent):
                BDD.cur.execute("""SELECT idEmprunt FROM Emprunt WHERE idAdherent =?""",(idAdherent,))
                return BDD.cur.fetchone()[0]
        
        @staticmethod 
        def getDateDebutEmprunt(idEmprunt):
                BDD.cur.execute("""SELECT dateDebutEmprunt FROM Emprunt WHERE idEmprunt = ?""",
                                (idEmprunt,))
                return BDD.cur.fetchone()[0]
                
        @staticmethod 
        def getDateRenduEmprunt(idEmprunt):
                BDD.cur.execute("""SELECT dateRenduEmprunt FROM Emprunt WHERE idEmprunt = ?""",
                                (idEmprunt,))
                return BDD.cur.fetchone()[0]
        
        @staticmethod  
        def getDateFinEmprunt(idEmprunt):
                return datetime.date(int(Emprunt.getDateDebutEmprunt(idEmprunt)[0:4]),int(Emprunt.getDateDebutEmprunt(idEmprunt)[5:7]),
                                     int(Emprunt.getDateDebutEmprunt(idEmprunt)[8:10])) + timedelta(Emprunt.getDureePrevue(idEmprunt))
 
        
        @staticmethod 
        def getIdJeuEmprunt(idEmprunt):
                BDD.cur.execute("""SELECT idJeu FROM Emprunt WHERE idEmprunt = ?""",(idEmprunt,))
                return BDD.cur.fetchone()[0]
        
        @staticmethod
        def getIdAdherentEmprunt(idEmprunt):
                BDD.cur.execute("""SELECT idAdherent FROM Emprunt WHERE idEmprunt =?""",(idEmprunt,))
                return BDD.cur.fetchone()[0]
        
        @staticmethod
        def getIdExtensionEmprunt(idEmprunt):
                BDD.cur.execute("""SELECT idExtension FROM Emprunt WHERE idEmprunt = ?""",(idEmprunt,))
                return BDD.cur.fetchone()[0]
        
        @staticmethod
        def getDureePrevue(idEmprunt):
                BDD.cur.execute("""SELECT dureePrevueEmprunt FROM Emprunt WHERE idEmprunt = ?""",
                                (idEmprunt,))
                return BDD.cur.fetchone()[0]

        #Fonctions usuelles:
        
        @staticmethod
        def aUneExtension(idEmprunt):
          return(Emprunt.getIdExtensionEmprunt(idEmprunt) != None)
          
        @staticmethod
        def empruntsEnCours():
          BDD.cur.execute("""SELECT * FROM Emprunt WHERE dateRenduEmprunt = ?""",(None,))
          return BDD.cur.fetchall()

        @staticmethod
        def EnCours():
          BDD.cur.execute("""SELECT * FROM Emprunt WHERE dateRenduEmprunt = ?""",(None,))
          return BDD.cur.fetchall()
        
        @staticmethod
        def getAllEmprunts():
          BDD.cur.execute("""SELECT * FROM Emprunt""")
          return BDD.cur.fetchall()
        
        @staticmethod
        def emprunterJeu(idJeu, idAdherent, dateDebutEmprunt, dureePrevueEmprunt):
          BDD.cur.execute("""SELECT MAX(idEmprunt) FROM Emprunt""")
          f = BDD.cur.fetchone()[0]
          if (f==None):
            idEmprunt = 1
          else:
            idEmprunt =f+1
          BDD.cur.execute("""INSERT INTO Emprunt(
                  idEmprunt, idJeu, idAdherent, idExtension, dateDebutEmprunt, dateRenduEmprunt, dureePrevueEmprunt)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""",
                  (idEmprunt, idJeu, idAdherent, 0, dateDebutEmprunt, 0, dureePrevueEmprunt)) 
          BDD.conn.commit() 
          
        @staticmethod
        def emprunterExtensionAvecJeu(idAdherent, idExtension, dateDebutEmprunt, dureePrevueEmprunt):
                idJeuExt = Extension.getIdJeu(idExtension) #on rcupre l'id du jeu correspondant l'extension
                BDD.cur.execute("""SELECT MAX(idEmprunt) FROM Emprunt""")
                f = BDD.cur.fetchone()[0]
                if (f==None):
                  idEmprunt = 1
                else:
                  idEmprunt =f+1
                BDD.cur.execute("""INSERT INTO Emprunt(
                          idEmprunt, idJeu, idAdherent, idExtension, dateDebutEmprunt, dateRenduEmprunt, dureePrevueEmprunt)
                          VALUES(?, ?, ?, ?, ?, ?, ?)""",
                          (idEmprunt, idJeuExt, idAdherent, idExtension, dateDebutEmprunt, 0, dureePrevueEmprunt)) 
                BDD.conn.commit() 
        
        @staticmethod
        def emprunterExtensionSansJeu(idAdherent, idExtension, dateDebutEmprunt, dureePrevueEmprunt):
                BDD.cur.execute("""SELECT MAX(idEmprunt) FROM Emprunt""")
                f = BDD.cur.fetchone()[0]
                if (f==None):
                  idEmprunt = 1
                else:
                  idEmprunt =f+1
                BDD.cur.execute("""INSERT INTO Emprunt(
                          idEmprunt, idJeu, idAdherent, idExtension, dateDebutEmprunt, dateRenduEmprunt, dureePrevueEmprunt)
                          VALUES(?, ?, ?, ?, ?, ?, ?)""",
                          (idEmprunt, 0, idAdherent, idExtension, dateDebutEmprunt, 0,dureePrevueEmprunt))
                          
                BDD.conn.commit() 
        
        @staticmethod
        def getJourRetard(idEmprunt):
                jourRetard = (datetime.date(int(Emprunt.getDateRenduEmprunt(idEmprunt)[0:4]),
                                        int(Emprunt.getDateRenduEmprunt(idEmprunt)[5:7]),
                                        int(Emprunt.getDateRenduEmprunt(idEmprunt)[8:10]))
                              + timedelta(Emprunt.getDureePrevue(idEmprunt))
                              - Emprunt.getDateFinEmprunt(idEmprunt)).days
                return jourRetard
        
        @staticmethod
        def estEnRetard(idEmprunt):
                return(datetime.date(int(Emprunt.getDateRenduEmprunt(idEmprunt)[0:4]),int(Emprunt.getDateRenduEmprunt(idEmprunt)[5:7]),int(Emprunt.getDateRenduEmprunt(idEmprunt)[8:10])) + timedelta(Emprunt.getDureePrevue(idEmprunt))
  > Emprunt.getDateFinEmprunt(idEmprunt))
                        
        @staticmethod
        def rendre(idEmprunt, date):
                Emprunt.setDateRenduEmprunt(idEmprunt, date)
                if (Emprunt.estEnRetard(idEmprunt)):
                        Adherent.ajoutRetard(Emprunt.getIdAdherentEmprunt(idEmprunt)) 
                        Adherent.ajoutJourRetard(Emprunt.getIdAdherentEmprunt(idEmprunt),Emprunt.getJourRetard(idEmprunt))

