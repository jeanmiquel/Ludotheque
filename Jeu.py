import sqlite3
import datetime
import Extension


conn = sqlite3.connect("P:\Ludotheque-master\Ludotheque.db")
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
`editeurJeu` varchar(20) NOT NULL,
`estEmpruntableJeu` tinyint(1) NOT NULL,
`synopsisJeu` varchar(200) NOT NULL,
PRIMARY KEY (`idJeu`))""")
conn.commit()


class Jeu :
    
        def __init__(self, nomJeu, anneeJeu, ageJeu):
                cur.execute("""INSERT INTO Jeu(
                idJeu, nomJeu, anneeJeu, nbJoueurJeu, ageJeu,
                quantiteJeu, editeurJeu, estEmpruntableJeu, synopsisJeu)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                (1000, nomJeu, anneeJeu,
                                " ", 0, ageJeu, " ", False, " "))

        #setters ?
        def setIdJeu(self, idJeu) :            
                cur.execute("""UPDATE Jeu SET idJeu = ? WHERE idJeu = ?""",
                                (idJeu, idJeu))
                idJeu = idJeu
                conn.commit()
         
        def setNomJeu(self, idJeu, nomJeu) :          
                anneeJeu = self.getAnneeJeu()
                cur.execute("""UPDATE Jeu SET nomJeu = ? WHERE idJeu = ?""",
                                (nomJeu, idJeu))
                conn.commit()

        def setAnneeJeu(self, idJeu,anneeJeu) :
                cur.execute("""UPDATE Jeu SET anneeJeu = ? WHERE idJeu = ?""",
                                (anneeJeu, idJeu))
                conn.commit()

        def setAgeJeu(self, idJeu, ageJeu):
                cur.execute("""UPDATE Jeu SET AgeJEu =? WHERE idJeu =?""",
                                    (ageJeu, idJeu))
                conn.commit()
                

        def setNbJoueurJeu(self, idJeu,nbJoueurJeu):
                cur.execute(""" UPDATE Jeu SET nbJoueurJeu = ? WHERE idJeu = ?""",(nbJoueurJeu,idJeu))
                conn.commit()

        def setQuantiteJeu(self, idJeu,quantiteJeu) :
                cur.execute("""UPDATE Jeu SET quantiteJeu = ? WHERE idJeu = ?""",(quantiteJeu, idJeu))
                conn.commit()

        def setEditeurJeu(self, idJeu,editeurJeu) :
                cur.execute("""UPDATE Jeu SET editeurJeu = ? WHERE idJeu = ?""",(editeurJeu, idJeu))
                conn.commit()

        def setEmpruntable(self,idJeu, booleen):
                cur.execute("""UPDATE Jeu SET estEmpruntableJeu = ? WHERE idJeu = ?""",(booleen, idJeu))
                conn.commit()

        def setSynopsisJeu(self,idJeu, synopsisJeu):
                cur.execute("""UPDATE Jeu SET synopsisJeu = ? WHERE idJeu = ?""",(synopsisJeu, idJeu))
                conn.commit()
 


        #getter
        
        def getInfoJeu(self,idJeu) :                         
                """0 Id, 1 Nom, 2 Annee, 3 NbJoueur, 4 Quantite, 5 Editeur, 6 Empruntable, 7 Synospis"""
                cur.execute("""SELECT
                idJeu, nomJeu, anneeJeu, nbJoueurJeu,
                quantiteJeu, editeurJeu, estEmpruntableJeu, synopsisJeu
                FROM Jeu Where idJeu = ?""",(idJeu))
                return cur.fetchone()[0]
    
        def getIdJeu(self,nomJeu) : 
                cur.execute("""SELECT idJeu FROM Jeu WHERE nomJeu = ?""",(nomJeu))
                return cur.fetchone()[0]

        def getNomJeu(self,idJeu) :

                cur.execute("""SELECT nomJeu FROM Jeu WHERE idJeu = ?""",(idJeu))
                return cur.fetchone()[0]

        def getAnneeJeu(self,idJeu) :        
                cur.execute("""SELECT anneeJeu FROM Jeu WHERE idJeu = ?""",(idJeu))
                return cur.fetchone()[0]
        
        def getNbJoueurJeu(self,idJeu) :
                cur.execute("""SELECT nbJoueurJeu FROM Jeu WHERE idJeu = ?""",(idJeu))
                return cur.fetchone()[0]

        def getQuantiteJeu(self,idJeu):
                cur.execute("""SELECT quantiteJeu FROM Jeu WHERE idJeu = ?""",(idJeu))
                return cur.fetchone()[0]

        def getEditeurJeu(self,idJeu):
                cur.execute("""SELECT editeurJeu FROM Jeu WHERE idJeu = ?""",(idJeu))
                return cur.fetchone()[0]

        def estEmpruntable(self,idJeu):
                cur.execute("""SELECT estEmpruntableJeu FROM Jeu WHERE idJeu = ?""",(idJeu))
                return cur.fetchone()[0]

        def getSynopsisJeu(self,idJeu):
                cur.execute("""SELECT synopsisJeu FROM Jeu WHERE idJeu = ?""",(idJeu))
                return cur.fetchone()[0]

        #Fonctions usuelles:

        def ajoutExemplaire(self,idJeu):
                self.setQuantiteJeu(self.getQuantiteJeu(idJeu)+1,idJeu)
                conn.commit()
                

        def retraitExemplaire(self,idJeu):
                self.setQuantiteJeu(max(self.getQuantiteJeu(idJeu)-1,0),idJeu)
                conn.commit()

        def changeEmpruntable(self,idJeu):
                self.setEmpruntable(not self.estEmpruntable(idJeu),idJeu)
                conn.commit()
    
        def supprimerJeu(self,idJeu):
                cur.execute("""DELETE FROM Jeu WHERE idJeu""",(idJeu))
                conn.commit()

