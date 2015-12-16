import sqlite3
import datetime
import Extension

import BDD

BDD.cur.execute("""CREATE TABLE IF NOT EXISTS `Jeu` (
`idJeu` int(6) NOT NULL,
`nomJeu` varchar(50) NOT NULL,
`anneeJeu` int(4) NOT NULL,
`ageJeu` int(2) NOT NULL,
`nbJoueurJeu` varchar(5) NOT NULL,
`quantiteJeu` int(3) NOT NULL,
`auteurJeu` varchar(20) NOT NULL,
`illustrateurJeu` varchar(20) NOT NULL,
`editeurJeu` varchar(20) NOT NULL,
`estEmpruntableJeu` tinyint(1) NOT NULL,
`synopsisJeu` varchar(200) NOT NULL,
PRIMARY KEY (`idJeu`))""")
BDD.conn.commit()


class Jeu :

        #setters ?
        
        @staticmethod
        def setNomJeu(idJeu, nomJeu) :          
                anneeJeu = self.getAnneeJeu()
                BDD.cur.execute("""UPDATE Jeu SET nomJeu = ? WHERE idJeu = ?""",
                                (nomJeu, idJeu))
                BDD.conn.commit()
        
        @staticmethod
        def setAnneeJeu(idJeu,anneeJeu) :
                BDD.cur.execute("""UPDATE Jeu SET anneeJeu = ? WHERE idJeu = ?""",
                                (anneeJeu, idJeu))
                BDD.conn.commit()
        
        @staticmethod
        def setAgeJeu(idJeu, ageJeu):
                BDD.cur.execute("""UPDATE Jeu SET AgeJEu =? WHERE idJeu =?""",
                                    (ageJeu, idJeu))
                BDD.conn.commit()
                
        @staticmethod
        def setNbJoueurJeu(idJeu,nbJoueurJeu):
                BDD.cur.execute(""" UPDATE Jeu SET nbJoueurJeu = ? WHERE idJeu = ?""",(nbJoueurJeu,idJeu))
                BDD.conn.commit()

        @staticmethod
        def setQuantiteJeu(idJeu,quantiteJeu) :
                BDD.cur.execute("""UPDATE Jeu SET quantiteJeu = ? WHERE idJeu = ?""",(quantiteJeu, idJeu))
                BDD.conn.commit()
                
        @staticmethod
        def setAuteurJeu(idJeu,auteurJeu) :
                BDD.cur.execute("""UPDATE Jeu SET auteurJeu = ? WHERE idJeu = ?""",(auteurJeu, idJeu))
                BDD.conn.commit()
                
        @staticmethod
        def setIllustrateurJeu(idJeu,illustrateurJeu) :
                BDD.cur.execute("""UPDATE Jeu SET illustrateurJeu = ? WHERE idJeu = ?""",(illustrateurJeu, idJeu))
                BDD.conn.commit()
        
        @staticmethod
        def setEditeurJeu(idJeu,editeurJeu) :
                BDD.cur.execute("""UPDATE Jeu SET editeurJeu = ? WHERE idJeu = ?""",(editeurJeu, idJeu))
                BDD.conn.commit()
        
        @staticmethod
        def setEmpruntable(idJeu, booleen):
                BDD.cur.execute("""UPDATE Jeu SET estEmpruntableJeu = ? WHERE idJeu = ?""",(booleen, idJeu))
                BDD.conn.commit()
        
        @staticmethod
        def setSynopsisJeu(idJeu, synopsisJeu):
                BDD.cur.execute("""UPDATE Jeu SET synopsisJeu = ? WHERE idJeu = ?""",(synopsisJeu, idJeu))
                BDD.conn.commit()
 


        #getter
        
        
        
        @staticmethod
        def getInfoJeu(idJeu) :                         
                BDD.cur.execute("""SELECT * FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return BDD.cur.fetchone()

        @staticmethod
        def getIdJeu(nomJeu) : 
                BDD.cur.execute("""SELECT idJeu FROM Jeu WHERE nomJeu = ?""",(nomJeu,))
                return BDD.cur.fetchone()[0]

        @staticmethod
        def getNomJeu(idJeu) :

                BDD.cur.execute("""SELECT nomJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return BDD.cur.fetchone()[0]

        @staticmethod
        def getAnneeJeu(idJeu) :        
                BDD.cur.execute("""SELECT anneeJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return BDD.cur.fetchone()[0]
        
        @staticmethod
        def getNbJoueurJeu(idJeu) :
                BDD.cur.execute("""SELECT nbJoueurJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return BDD.cur.fetchone()[0]

        @staticmethod
        def getQuantiteJeu(idJeu):
                BDD.cur.execute("""SELECT quantiteJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return BDD.cur.fetchone()[0]
                
        @staticmethod
        def getAuteurJeu(idJeu):
                BDD.cur.execute("""SELECT auteurJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return BDD.cur.fetchone()[0]
                
        @staticmethod
        def getIllustrateurJeu(idJeu):
                BDD.cur.execute("""SELECT illustrateurJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return BDD.cur.fetchone()[0]
        
        @staticmethod
        def getEditeurJeu(idJeu):
                BDD.cur.execute("""SELECT editeurJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return BDD.cur.fetchone()[0]
        
        @staticmethod
        def estEmpruntable(idJeu):
                BDD.cur.execute("""SELECT estEmpruntableJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return BDD.cur.fetchone()[0]
        
        @staticmethod
        def getSynopsisJeu(idJeu):
                BDD.cur.execute("""SELECT synopsisJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return BDD.cur.fetchone()[0]

        #Fonctions usuelles:
        
        @staticmethod
        def getAllJeu():
                BDD.cur.execute("""SELECT * FROM Jeu""")
                return BDD.cur.fetchall()
        
        @staticmethod
        def ajoutJeu():
            BDD.cur.execute("""SELECT MAX(idJeu) FROM Jeu""")
            f = BDD.cur.fetchone()[0]
            if (f==None):
                idJeu = 1
            else:
                idJeu =f+1
            BDD.cur.execute("""INSERT INTO Jeu(
                    idJeu, nomJeu, anneeJeu, nbJoueurJeu, ageJeu,
                    quantiteJeu, auteurJeu, illustrateurJeu, editeurJeu, estEmpruntableJeu, synopsisJeu)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                    (idJeu, nomJeu, anneeJeu,nbJoueurJeu, ageJeu,
                    quantiteJeu, auteurJeu, illustrateurJeu, editeurJeu, estEmpruntableJeu, synopsisJeu))
            BDD.conn.commit()
                                
        @staticmethod
        def ajoutExemplaire(idJeu):
                Jeu.setQuantiteJeu(idJeu,Jeu.getQuantiteJeu(idJeu)+1)
                BDD.conn.commit()
                
        @staticmethod
        def retraitExemplaire(idJeu):
                Jeu.setQuantiteJeu(idJeu,max(Jeu.getQuantiteJeu(idJeu)-1,0))
                BDD.conn.commit()
        
        @staticmethod
        def changeEmpruntable(idJeu):
                Jeu.setEmpruntable(idJeu,not Jeu.estEmpruntable(idJeu))
                BDD.conn.commit()
        
        @staticmethod
        def supprimerJeu(idJeu):
                BDD.cur.execute("""DELETE FROM Jeu WHERE idJeu =?""",(idJeu,))
                BDD.conn.commit()
