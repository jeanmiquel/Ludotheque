import sqlite3
import datetime
import Extension


conn = sqlite3.connect("ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS `Jeu` (
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
conn.commit()


class Jeu :

        #setters ?
        
        @staticmethod
        def setNomJeu(idJeu, nomJeu) :          
                anneeJeu = self.getAnneeJeu()
                cur.execute("""UPDATE Jeu SET nomJeu = ? WHERE idJeu = ?""",
                                (nomJeu, idJeu))
                conn.commit()
        
        @staticmethod
        def setAnneeJeu(idJeu,anneeJeu) :
                cur.execute("""UPDATE Jeu SET anneeJeu = ? WHERE idJeu = ?""",
                                (anneeJeu, idJeu))
                conn.commit()
        
        @staticmethod
        def setAgeJeu(idJeu, ageJeu):
                cur.execute("""UPDATE Jeu SET AgeJEu =? WHERE idJeu =?""",
                                    (ageJeu, idJeu))
                conn.commit()
                
        @staticmethod
        def setNbJoueurJeu(idJeu,nbJoueurJeu):
                cur.execute(""" UPDATE Jeu SET nbJoueurJeu = ? WHERE idJeu = ?""",(nbJoueurJeu,idJeu))
                conn.commit()

        @staticmethod
        def setQuantiteJeu(idJeu,quantiteJeu) :
                cur.execute("""UPDATE Jeu SET quantiteJeu = ? WHERE idJeu = ?""",(quantiteJeu, idJeu))
                conn.commit()
                
        @staticmethod
        def setAuteurJeu(idJeu,auteurJeu) :
                cur.execute("""UPDATE Jeu SET auteurJeu = ? WHERE idJeu = ?""",(auteurJeu, idJeu))
                conn.commit()
                
        @staticmethod
        def setIllustrateurJeu(idJeu,illustrateurJeu) :
                cur.execute("""UPDATE Jeu SET illustrateurJeu = ? WHERE idJeu = ?""",(illustrateurJeu, idJeu))
                conn.commit()
        
        @staticmethod
        def setEditeurJeu(idJeu,editeurJeu) :
                cur.execute("""UPDATE Jeu SET editeurJeu = ? WHERE idJeu = ?""",(editeurJeu, idJeu))
                conn.commit()
        
        @staticmethod
        def setEmpruntable(idJeu, booleen):
                cur.execute("""UPDATE Jeu SET estEmpruntableJeu = ? WHERE idJeu = ?""",(booleen, idJeu))
                conn.commit()
        
        @staticmethod
        def setSynopsisJeu(idJeu, synopsisJeu):
                cur.execute("""UPDATE Jeu SET synopsisJeu = ? WHERE idJeu = ?""",(synopsisJeu, idJeu))
                conn.commit()
 


        #getter
        
        @staticmethod
        def afficherTableJeu():
                cur.execute("""SELECT * FROM Jeu""")
                return cur.fetchall()
        
        @staticmethod
        def getInfoJeu(idJeu) :                         
                cur.execute("""SELECT * FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return cur.fetchone()

        @staticmethod
        def getIdJeu(nomJeu) : 
                cur.execute("""SELECT idJeu FROM Jeu WHERE nomJeu = ?""",(nomJeu,))
                return cur.fetchone()[0]

        @staticmethod
        def getNomJeu(idJeu) :

                cur.execute("""SELECT nomJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return cur.fetchone()[0]

        @staticmethod
        def getAnneeJeu(idJeu) :        
                cur.execute("""SELECT anneeJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return cur.fetchone()[0]
        
        @staticmethod
        def getNbJoueurJeu(idJeu) :
                cur.execute("""SELECT nbJoueurJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return cur.fetchone()[0]

        @staticmethod
        def getQuantiteJeu(idJeu):
                cur.execute("""SELECT quantiteJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return cur.fetchone()[0]
                
        @staticmethod
        def getAuteurJeu(idJeu):
                cur.execute("""SELECT auteurJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return cur.fetchone()[0]
                
        @staticmethod
        def getIllustrateurJeu(idJeu):
                cur.execute("""SELECT illustrateurJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return cur.fetchone()[0]
        
        @staticmethod
        def getEditeurJeu(idJeu):
                cur.execute("""SELECT editeurJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return cur.fetchone()[0]
        
        @staticmethod
        def estEmpruntable(idJeu):
                cur.execute("""SELECT estEmpruntableJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return cur.fetchone()[0]
        
        @staticmethod
        def getSynopsisJeu(idJeu):
                cur.execute("""SELECT synopsisJeu FROM Jeu WHERE idJeu = ?""",(idJeu,))
                return cur.fetchone()[0]

        #Fonctions usuelles:
        @staticmethod
        def ajoutJeu():
            cur.execute("""SELECT MAX(idJeu) FROM Jeu""")
            f = cur.fetchone()[0]
            if (f==None):
                idJeu = 1
            else:
                idJeu =f+1
            cur.execute("""INSERT INTO Jeu(
                    idJeu, nomJeu, anneeJeu, nbJoueurJeu, ageJeu,
                    quantiteJeu, auteurJeu, illustrateurJeu, editeurJeu, estEmpruntableJeu, synopsisJeu)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                    (idJeu, nomJeu, anneeJeu,nbJoueurJeu, ageJeu,
                    quantiteJeu, auteurJeu, illustrateurJeu, editeurJeu, estEmpruntableJeu, synopsisJeu))
            conn.commit()
                                
        @staticmethod
        def ajoutExemplaire(idJeu):
                Jeu.setQuantiteJeu(idJeu,Jeu.getQuantiteJeu(idJeu)+1)
                conn.commit()
                
        @staticmethod
        def retraitExemplaire(idJeu):
                Jeu.setQuantiteJeu(idJeu,max(Jeu.getQuantiteJeu(idJeu)-1,0))
                conn.commit()
        
        @staticmethod
        def changeEmpruntable(idJeu):
                Jeu.setEmpruntable(idJeu,not Jeu.estEmpruntable(idJeu))
                conn.commit()
        
        @staticmethod
        def supprimerJeu(idJeu):
                cur.execute("""DELETE FROM Jeu WHERE idJeu =?""",(idJeu,))
                conn.commit()

