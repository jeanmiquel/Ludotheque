import datetime
import sqlite3

conn = sqlite3.connect("C:\Users\david.ringayen\Desktop\Ludotheque-master\ludotheque.db")
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
                    PRIMARY KEY (`idAdherent`)
                    FOREIGN KEY (`idEmprunt`) REFERENCES Emprunt(`idEmprunt`),
                    FOREIGN KEY (`idReservation`) REFERENCES Reservation(`idReservation`))""")
conn.commit()


class Adherent :


    #setters 
    @staticmethod
    def setNom(idAdherent, nomAdherent) : 
      cur.execute("""UPDATE Adherent SET nomAdherent= ? WHERE idAdherent = ?""",
      (nomAdherent, idAdherent))
      conn.commit()

    @staticmethod
    def setPseudo(idAdherent, pseudoAdh) :
      cur.execute("""UPDATE Adherent SET pseudoAdherent = ? WHERE idAdherent = ?""",
      (pseudoAdherent, idAdherent))
      conn.commit()

    @staticmethod
    def setMotDePasse(idAdherent, motDePasseAdherent):
      cur.execute(""" UPDATE Adherent SET motDePasseAdherent = ? WHERE idAdherent = ?""",(motDePasseAdherent,idAdherent))
      conn.commit()

    @staticmethod
    def setNumeroTelephone(idAdherent, numeroTelAdherent):
      cur.execute(""" UPDATE Adherent SET numeroTelAdherent = ? WHERE idAdherent = ?""",(numeroTelAdherent,idAdherent))
      conn.commit()

    @staticmethod
    def setMail(idAdherent, adressMailAdherent):
      cur.execute(""" UPDATE Adherent SET adresseMailAdherent = ? WHERE idAdherent = ?""",(adresseMailAdherent,idAdherent))
      conn.commit()

    @staticmethod    
    def setAdresse(idAdherent, adresseAdherent):
      cur.execute(""" UPDATE Adherent SET adresseAdherent = ? WHERE idAdherent = ?""",(adresseAdherent,idAdherent))
      conn.commit()

    @staticmethod
    def setDatePaiement(idAdherent, datePaiementAdherent):
      cur.execute(""" UPDATE Adherent SET datePaiementAdherent= ? WHERE idAdherent = ?""",(datePaiementAdherent,idAdherent))
      conn.commit()

    @staticmethod
    def setEmpruntEnCours(idAdherent, idEmprunt):
      cur.execute(""" UPDATE Adherent SET idEmprunt = ? WHERE idAdherent = ?""",(idEmprunt,idAdherent))
      conn.commit()

    @staticmethod
    def setReservEnCours(idAdherent, idReservation):
      cur.execute(""" UPDATE Adherent SET idReservation = ? WHERE idAdherent = ?""",(idReservation,idAdherent))
      conn.commit()

    @staticmethod
    def setNbreRetards(idAdherent, nombreRetardAdherent):
      cur.execute(""" UPDATE Adherent SET nombreRetardAdherent = ? WHERE idAdherent = ?""",(nombreRetardAdherent,idAdherent))
      conn.commit()

    @staticmethod   
    def setNbreJoursRetards(idAdherent, nombreJourRetardAdherent):
      cur.execute(""" UPDATE Adherent SET nombreJourRetardAdherent = ? WHERE idAdherent = ?""",(nombreJourRetardAdherent,idAdherent))
      conn.commit()

    @staticmethod
    def setAdministrateur( idAdherent,estAdminAdherent):
      cur.execute(""" UPDATE Adherent SET estAdminAdherent = ? WHERE idAdherent = ?""",(estAdminAdherent,idAdherent))
      conn.commit()

    @staticmethod
    def setNbReservAnnulees(idAdherent, reservationAnnuleAdherent):
      cur.execute(""" UPDATE Adherent SET reservationAnnuleAdherent = ? WHERE idAdherent = ?""",(reservationAnnuleAdherent,idAdherent))
      conn.commit()

  #getters 
    @staticmethod
    def getInfo(idAdherent) : #Saisir tout d'un coup
      """0 Id, 1 Nom, 2 Prenom, 3 Date de naissance, 4 Adresse, 5 Code postal, 6 Ville, 7 Numero de telephone, 8 Pseudo, 9 Mot de passe, 10 Adresse Mail, 11 Statut admin, 12 Date de paiement, 13 Nombre de retards, 14 Nombre de jours de retards cumules, 15 Nombre de reservations annulees, 16 Emprunt en cours, 17 Reservation en cours"""
      cur.execute("""SELECT
      idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent, pseudoAdherent, motDePasseAdherent, adresseMailAdherent, estAdminAdherent, datePaiementAdherent, nombreRetardAdherent, nombreJourRetardAdherent, reservationAnnuleAdherent, idEmprunt, idReservation
      FROM Adherent Where idAdherent = ?""",(idAdherent,))
      return cur.fetchone()

    @staticmethod
    def getId(nomdAdherent) :
      cur.execute(""" SELECT idAdherent FROM Adherent WHERE nomJeu = ?""",(nomAdherent,))

    @staticmethod
    def getNom(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[1]

    @staticmethod
    def getPrenom(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[2]

    @staticmethod
    def getNaissance(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[3]

    @staticmethod
    def getPseudo(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[8]

    @staticmethod
    def getPassword(idAdherent) : 
        return Adherent.getInfoAdh(idAdherent)[9]

    @staticmethod
    def getNumTelephone(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[7]

    @staticmethod
    def getMail(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[10]
    
    @staticmethod
    def getAdresse(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[4]

    @staticmethod
    def getDatePaiement(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[12]
    
    @staticmethod  
    def getEmpruntEnCours(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[16]

    @staticmethod 
    def getReservEnCours(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[17]

    @staticmethod  
    def getNbreRetards(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[13]

    @staticmethod  
    def getNbJoursRetards(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[14]

    @staticmethod  
    def getEstAdministrateur(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[11]

    @staticmethod
    def getNbReservAnnulees(idAdherent) : 
      return Adherent.getInfoAdh(idAdherent)[15]
      
#Fonctions usuelles:

    @staticmethod
    def retirerAdh(idAdherent):
        cursor.execute("""DELETE FROM Adherent WHERE idAdherent""",(idAdherent))
        conn.commit()

    @staticmethod
    def ajoutAdherent(nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent,  pseudoAdherent, adresseMailAdherent):
        cur.execute("""SELECT MAX(idAdherent) FROM Adherent""")
        f = cur.fetchone()[0]
        if (f==None):
            idAdherent = 1
        else:
            idAdherent =f+1
            cur.execute("""INSERT INTO Adherent(idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent,
            villeAdherent, numeroTelAdherent, pseudoAdherent, motDePasseAdherent, adresseMailAdherent, estAdminAdherent, datePaiementAdherent, nombreRetardAdherent, nombreJourRetardAdherent, reservationAnnuleAdherent, idEmprunt, idReservation) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
          (idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent,  pseudoAdherent, prenomAdherent+"."+nomAdherent, adresseMailAdherent, False, datetime.datetime.now(), 0,0, 0, 0,0))
            conn.commit()
            
    @staticmethod
    def reinitialiserMDPAdherent(idAdherent):
        cur.execute("""UPDATE Adherent SET motDePasseAdherent = ? WHERE idAdherent = ?""",(Adherent.getPrenomAdh(idAdherent)+"."+Adherent.getNomAdh(idAdherent),idAdherent))
        conn.commit()
