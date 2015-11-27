import datetime
import sqlite3

conn = sqlite3.connect("P:\Ludotheque-master\Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS `Adherent` (
                    `idAdherent` int(6) NOT NULL,
                    `nomAdherent` varchar(25) NOT NULL,
                    `prenomAdherent` varchar(25) NOT NULL,
                    `dateNaissanceAdherent` date NOT NULL,
                    `adresseAdherent` varchar(30) NOT NULL,
                    `codePostalAdherent` varchar(10) NOT NULL,
                    `villeAdherent` varchar(10) NOT NULL,
                    `numeroTelAdherent` int(10) NOT NULL,
                    `pseudoAdherent` varchar(20) NOT NULL,
                    `motDePasseAdherent` varchar(26) NOT NULL,
                    `adressMailAdherent` varchar(50) NOT NULL,
                    `estAdminAdherent` tinyint(1) NOT NULL,
                    `datePaiementAdherent` date NOT NULL,
                    `nombreRetardAdherent` int(3) NOT NULL,
                    `nombreJourRetardAdherent` int(3) NOT NULL,
                    `reservationAnnuleAdherent` int(3) NOT NULL,
                    `idEmprunt` int(11) NOT NULL,
                    `idReservation` int(11) NOT NULL,
                    PRIMARY KEY (`idAdherent`))""")
conn.commit()


class Adherent :
    
    def __init__(self):

#setters ?



    def setNomAdherent(self,idAdherent, nomAdherent) : 
      cur.execute("""UPDATE Adherent SET nomAdherent= ? WHERE idAdherent = ?""",
      (nomAdherent, idAdherent))
      conn.commit()

    def setPseudo(self,idAdherent, pseudoAdh) :
      cur.execute("""UPDATE Adherent SET pseudoAdherent = ? WHERE idAdherent = ?""",
      (pseudoAdherent, idAdherent))
      conn.commit()

    def setMotDePasse(self,idAdherent, motDePasseAdherent):
      cur.execute(""" UPDATE Adherent SET motDePasseAdherent = ? WHERE idAdherent = ?""",(motDePasseAdherent,idAdherent))
      conn.commit()

    def setNumeroTel(self,idAdherent, numeroTelAdherent):
      cur.execute(""" UPDATE Adherent SET numeroTelAdherent = ? WHERE idAdherent = ?""",(numeroTelAdherent,idAdherent))
      conn.commit()

    def setMail(self,idAdherent, adressMailAdherent):
      cur.execute(""" UPDATE Adherent SET adresseMailAdherent = ? WHERE idAdherent = ?""",(adresseMailAdherent,idAdherent))
      conn.commit()
      
    def setAdresse(self,idAdherent, adresseAdherent):
      cur.execute(""" UPDATE Adherent SET adresseAdherent = ? WHERE idAdherent = ?""",(adresseAdherent,idAdherent))
      conn.commit()

    def setDatePaiement(self,idAdherent, datePaiementAdherent):
      cur.execute(""" UPDATE Adherent SET datePaiementAdherent= ? WHERE idAdherent = ?""",(datePaiementAdherent,idAdherent))
      conn.commit()

    def setEmpruntEnCours(self,idAdherent, idEmprunt):
      cur.execute(""" UPDATE Adherent SET idEmprunt = ? WHERE idAdherent = ?""",(idEmprunt,idAdherent))
      conn.commit()

    def setReservEnCours(self,idAdherent, idReservation):
      cur.execute(""" UPDATE Adherent SET idReservation = ? WHERE idAdherent = ?""",(idReservation,idAdherent))
      conn.commit()

    def setNbreRetards(self,idAdherent, nombreRetardAdherent):
      cur.execute(""" UPDATE Adherent SET nombreRetardAdherent = ? WHERE idAdherent = ?""",(nombreRetardAdherent,idAdherent))
      conn.commit()
      
    def setNbreJoursRetards(self,idAdherent, nombreJourRetardAdherent):
      cur.execute(""" UPDATE Adherent SET nombreJourRetardAdherent = ? WHERE idAdherent = ?""",(nombreJourRetardAdherent,idAdherent))
      conn.commit()

    def setAdmin(self, idAdherent,estAdminAdherent):
      cur.execute(""" UPDATE Adherent SET estAdminAdherent = ? WHERE idAdherent = ?""",(estAdminAdherent,idAdherent))
      conn.commit()

    def setNbreReservAnnulees(self,idAdherent, reservationAnnuleAdherent):
      cur.execute(""" UPDATE Adherent SET reservationAnnuleAdherent = ? WHERE idAdherent = ?""",(reservationAnnuleAdherent,idAdherent))
      conn.commit()

#getters ?

    def getInfoAdh(self,idAdherent) : #Saisir tout d'un coup
      """0 Id, 1 Nom, 2 Prenom, 3 Date de naissance, 4 Adresse, 5 Code postal, 6 Ville, 7 Numero de telephone, 8 Pseudo, 9 Mot de passe, 10 Adresse Mail, 11 Statut admin, 12 Date de paiement, 13 Nombre de retards, 14 Nombre de jours de retards cumules, 15 Nombre de reservations annulees, 16 Emprunt en cours, 17 Reservation en cours"""
      cur.execute("""SELECT
      idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent, pseudoAdherent, motDePasseAdherent, adresseMailAdherent, estAdminAdherent, datePaiementAdherent, nombreRetardAdherent, nombreJourRetardAdherent, reservationAnnuleAdherent, idEmprunt, idReservation
      FROM Adherent Where idAdherent = ?""",(idAdherent))
      return cur.fetchone()

    def getIdAdh(self,nomdAdherent) :
      cur.execute(""" SELECT idAdherent FROM Adherent WHERE nomJeu = ?""",(nomAdherent))

    def getNomAdh(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[1]

    def getPrenomAdh(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[2]

    def getNaissance(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[3]

    def getPseudo(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[8]

    def getPassword(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[9]

    def getNumTel(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[7]

    def getMail(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[10]

    def getAdresse(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[4]

    def getDatePaiement(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[12]
      
    def getEmpruntEnCours(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[16]
      
    def getReservEnCours(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[17]
      
    def getNbreRetards(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[13]
      
    def getNbreJoursRetards(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[14]
      
    def getEstAdmin(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[11]
      
    def getNbreReservAnnulees(self,idAdherent) : 
      return self.getInfoAdh(idAdherent)[15]
      
#Fonctions usuelles:


    def retirerAdh(self,idAdherent):
      cursor.execute("""DELETE FROM Adherent WHERE idAdherent""",(idAdherent))
      return self

    def ajoutAdherent(self, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent,  pseudoAdherent, motDePasseAdherent, adresseMailAdherent):
      cur.execute("""SELECT MAX(idAdherent) FROM Adherent
      cur.execute("""INSERT INTO Adherent(
      idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent, pseudoAdherent, motDePasseAdherent, adresseMailAdherent, estAdminAdherent, datePaiementAdherent, nombreRetardAdherent, nombreJourRetardAdherent, reservationAnnuleAdherent, idEmprunt, idReservation)
      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
      (idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent,  pseudoAdherent, motDePasseAdherent, adresseMailAdherent, False, datetime.now(), 0, 0, 0,0))
    
