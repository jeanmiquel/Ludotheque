import datetime
import sqlite3

conn = sqlite3.connect("C:\Users\Jean\Desktop\LUDOTHEQUE\Ludotheque.db")
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
                    `idReservation int(11) NOT NULL,
                    PRIMARY KEY (`idAdherent`)
                    )""")
conn.commit()


class Adherent :
    
    def __init__(self, nomAdherent, prenomAdherent, pseudoAdherent, motDePasseAdherent, adresseMailAdherent, dataBase = conn):
      self.cursor = dataBase.cursor()
      self.Table = "Adherent"
      self.cursor.execute("""INSERT INTO Adherent(
      idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent, pseudoAdherent, motDePasseAdherent, adresseMailAdherent, estAdminAdherent, datePaiementAdherent, nombreRetardAdherent, nombreJourRetardAdherent, reservationAnnuleAdherent, idEmprunt, idReservation)
      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
      (self.idAdherent, nomAdherent, prenomAdherent, "", "", 0, "", 0,  pseudoAdherent, motDePasseAdherent, adresseMailAdherent, False, datetime.now(), 0, 0, 0,0))


#setters ?

    def setIdAdh(self, idAdh) : 
      self.cursor.execute("""UPDATE Adherent SET idAdherent = ? WHERE idAdherent = ?""",
      (idAdherent, self.idAdherent))
      self.idAdherent = idAdherent
      return self

    def setNomAdherent(self, nomAdherent) : 
      self.cursor.execute("""UPDATE Adherent SET nomAdherent= ? WHERE idAdherent = ?""",
      (nomAdherent, self.idAdherent))
      return self

    def setPseudo(self, pseudoAdh) :
      self.cursor.execute("""UPDATE Adherent SET pseudoAdherent = ? WHERE idAdherent = ?""",
      (pseudoAdherent, self.idAdherent))
      return self

    def setMotDePasse(self, motDePasseAdherent):
      self.cursor.execute(""" UPDATE Adherent SET motDePasseAdherent = ? WHERE idAdherent = ?""",(motDePasseAdherent,self.idAdherent))
      return self

    def setNumeroTel(self, numeroTelAdherent):
      self.cursor.execute(""" UPDATE Adherent SET numeroTelAdherent = ? WHERE idAdherent = ?""",(numeroTelAdherent,self.idAdherent))
      return self

    def setMail(self, adressMailAdherent):
      self.cursor.execute(""" UPDATE Adherent SET adresseMailAdherent = ? WHERE idAdherent = ?""",(adresseMailAdherent,self.idAdherent))
      return self
      
    def setAdresse(self, adresseAdherent):
      self.cursor.execute(""" UPDATE Adherent SET adresseAdherent = ? WHERE idAdherent = ?""",(adresseAdherent,self.idAdherent))
      return self

    def setDatePaiement(self, datePaiementAdherent):
      self.cursor.execute(""" UPDATE Adherent SET datePaiementAdherent= ? WHERE idAdherent = ?""",(datePaiementAdherent,self.idAdherent))
      return self

    def setEmpruntEnCours(self, idEmprunt):
      self.cursor.execute(""" UPDATE Adherent SET idEmprunt = ? WHERE idAdherent = ?""",(idEmprunt,self.idAdherent))
      return self

    def setReservEnCours(self, idReservation):
      self.cursor.execute(""" UPDATE Adherent SET idReservation = ? WHERE idAdherent = ?""",(idReservation,self.idAdherent))
      return self

    def setNbreRetards(self, nombreRetardAdherent):
      self.cursor.execute(""" UPDATE Adherent SET nombreRetardAdherent = ? WHERE idAdherent = ?""",(nombreRetardAdherent,self.idAdherent))
      return self
      
    def setNbreJoursRetards(self, nombreJourRetardAdherent):
      self.cursor.execute(""" UPDATE Adherent SET nombreJourRetardAdherent = ? WHERE idAdherent = ?""",(nombreJourRetardAdherent,self.idAdherent))
      return self

    def setAdmin(self, estAdminAdherent):
      self.cursor.execute(""" UPDATE Adherent SET estAdminAdherent = ? WHERE idAdherent = ?""",(estAdminAdherent,self.idAdherent))
      return self

    def setNbreReservAnnulees(self, reservationAnnuleAdherent):
      self.cursor.execute(""" UPDATE Adherent SET reservationAnnuleAdherent = ? WHERE idAdherent = ?""",(reservationAnnuleAdherent,self.idAdherent))
      return self

#getters ?

    def getInfoAdh(self) : #Saisir tout d'un coup
      """0 Id, 1 Nom, 2 Prenom, 3 Date de naissance, 4 Adresse, 5 Code postal, 6 Ville, 7 Numero de telephone, 8 Pseudo, 9 Mot de passe, 10 Adresse Mail, 11 Statut admin, 12 Date de paiement, 13 Nombre de retards, 14 Nombre de jours de retards cumules, 15 Nombre de reservations annulees, 16 Emprunt en cours, 17 Reservation en cours"""
      self.cursor.execute("""SELECT
      idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent, pseudoAdherent, motDePasseAdherent, adresseMailAdherent, estAdminAdherent, datePaiementAdherent, nombreRetardAdherent, nombreJourRetardAdherent, reservationAnnuleAdherent, idEmprunt, idReservation
      FROM Adherent Where idAdherent = ?""",(self.idAdherent))
      return self.cursor.fetchone()

    def getIdAdh(self) :
      return self.idAdherent #L'id est accessible dans les attributs

    def getNomAdh(self) : 
      return self.getInfoAdh()[1]

    def getPseudo(self) : 
      return self.getInfoAdh()[2]

    def getPassword(self) : 
      return self.getInfoAdh()[3]

    def getNumTel(self) : 
      return self.getInfoAdh()[4]

    def getMail(self) : 
      return self.getInfoAdh()[5]

    def getNomAdresse(self) : 
      return self.getInfoAdh()[6]

    def getDateAbonnement(self) : 
      return self.getInfoAdh()[7]
      
    def getEmpruntEnCours(self) : 
      return self.getInfoAdh()[8]
      
    def getReservEnCours(self) : 
      return self.getInfoAdh()[9]
      
    def getNbreRetards(self) : 
      return self.getInfoAdh()[10]
      
    def getNbreJoursRetards(self) : 
      return self.getInfoAdh()[11]
      
    def getEstAdmin(self) : 
      return self.getInfoAdh()[12]
      
    def getNbreReservAnnulees(self) : 
      return self.getInfoAdh()[13]
      
#Fonctions usuelles:


    def retirerAdh(self):
      cursor.execute("""DELETE FROM Adherent WHERE idAdherent""",(self.idAdherent))
      return self
