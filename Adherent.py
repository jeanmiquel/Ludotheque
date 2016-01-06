import datetime
import sqlite3

import BDD

class Adherent :


    #setters 
    @staticmethod
    def setNom(idAdherent, nomAdherent) : 
      BDD.cur.execute("""UPDATE Adherent SET nomAdherent= ? WHERE idAdherent = ?""",
      (nomAdherent, idAdherent))
      BDD.conn.commit()
      
    @staticmethod
    def setPrenom(idAdherent, prenomAdherent) : 
      BDD.cur.execute("""UPDATE Adherent SET prenomAdherent= ? WHERE idAdherent = ?""",
      (prenomAdherent, idAdherent))
      BDD.conn.commit()
      
    @staticmethod
    def setNaissance(idAdherent, dateNaissance):
      BDD.cur.execute("""UPDATE Adherent SET dateNaissance= ? WHERE idAdherent = ?""",
      (dateNaissance, idAdherent))
      BDD.conn.commit()

    @staticmethod
    def setPseudo(idAdherent, pseudoAdh) :
      BDD.cur.execute("""UPDATE Adherent SET pseudoAdherent = ? WHERE idAdherent = ?""",
      (pseudoAdherent, idAdherent))
      BDD.conn.commit()

    @staticmethod
    def setMotDePasse(idAdherent, motDePasseAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET motDePasseAdherent = ? WHERE idAdherent = ?""",(motDePasseAdherent,idAdherent))
      BDD.conn.commit()

    @staticmethod
    def setNumeroTelephone(idAdherent, numeroTelAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET numeroTelAdherent = ? WHERE idAdherent = ?""",(numeroTelAdherent,idAdherent))
      BDD.conn.commit()

    @staticmethod
    def setMail(idAdherent, adressMailAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET adresseMailAdherent = ? WHERE idAdherent = ?""",(adresseMailAdherent,idAdherent))
      BDD.conn.commit()

    @staticmethod    
    def setAdresse(idAdherent, adresseAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET adresseAdherent = ? WHERE idAdherent = ?""",
      (adresseAdherent, idAdherent))
      BDD.conn.commit()
    
    @staticmethod    
    def setAdresse(idAdherent, codePostalAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET codePostalAdherent = ? WHERE idAdherent = ?""",
      (codePostalAdherent, idAdherent))
      BDD.conn.commit()
      
    @staticmethod    
    def setAdresse(idAdherent, villeAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET villeAdherent = ? WHERE idAdherent = ?""",
      (villeAdherent, idAdherent))
      BDD.conn.commit()
      

    @staticmethod
    def setDatePaiement(idAdherent, datePaiementAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET datePaiementAdherent= ? WHERE idAdherent = ?""",(datePaiementAdherent,idAdherent))
      BDD.conn.commit()

    @staticmethod
    def setEmpruntEnCours(idAdherent, idEmprunt):
      BDD.cur.execute(""" UPDATE Adherent SET idEmprunt = ? WHERE idAdherent = ?""",(idEmprunt,idAdherent))
      BDD.conn.commit()

    @staticmethod
    def setReservEnCours(idAdherent, idReservation):
      BDD.cur.execute(""" UPDATE Adherent SET idReservation = ? WHERE idAdherent = ?""",(idReservation,idAdherent))
      BDD.conn.commit()

    @staticmethod
    def setNbreRetards(idAdherent, nombreRetardAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET nombreRetardAdherent = ? WHERE idAdherent = ?""",(nombreRetardAdherent,idAdherent))
      BDD.conn.commit()

    @staticmethod   
    def setNbreJoursRetards(idAdherent, nombreJourRetardAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET nombreJourRetardAdherent = ? WHERE idAdherent = ?""",(nombreJourRetardAdherent,idAdherent))
      BDD.conn.commit()

    @staticmethod
    def setAdministrateur( idAdherent,estAdminAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET estAdminAdherent = ? WHERE idAdherent = ?""",(estAdminAdherent,idAdherent))
      BDD.conn.commit()

    @staticmethod
    def setNbReservAnnulees(idAdherent, reservationAnnuleAdherent):
      BDD.cur.execute(""" UPDATE Adherent SET reservationAnnuleAdherent = ? WHERE idAdherent = ?""",(reservationAnnuleAdherent,idAdherent))
      BDD.conn.commit()

  #getters 
    @staticmethod
    def getInfo(idAdherent) : #Saisir tout d'un coup
      """0 Id, 1 Nom, 2 Prenom, 3 Date de naissance, 4 Adresse, 5 Code postal, 6 Ville, 7 Numero de telephone, 8 Pseudo, 9 Mot de passe, 10 Adresse Mail, 11 Statut admin, 12 Date de paiement, 13 Nombre de retards, 14 Nombre de jours de retards cumules, 15 Nombre de reservations annulees, 16 Emprunt en cours, 17 Reservation en cours"""
      BDD.cur.execute("""SELECT
      idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent, pseudoAdherent, motDePasseAdherent, adresseMailAdherent, estAdminAdherent, datePaiementAdherent, nombreRetardAdherent, nombreJourRetardAdherent, reservationAnnuleAdherent, idEmprunt, idReservation
      FROM Adherent Where idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()

    @staticmethod
    def getId(nomAdherent) :
        BDD.cur.execute(""" SELECT idAdherent FROM Adherent WHERE nomAdherent = ?""",(nomAdherent,))
        a= BDD.cur.fetchone()
        if a!=None:
            return a[0]
        else:
            return a

    @staticmethod
    def getNom(idAdherent) : 
      BDD.cur.execute("""SELECT nomAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod
    def getPrenom(idAdherent) : 
      BDD.cur.execute("""SELECT prenomAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod
    def getNaissance(idAdherent) : 
      BDD.cur.execute("""SELECT dateNaissanceAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod
    def getPseudo(idAdherent) : 
      BDD.cur.execute("""SELECT pseudoAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod
    def getMotDePasse(idAdherent) : 
        BDD.cur.execute("""SELECT motDePasseAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
        return BDD.cur.fetchone()[0]

    @staticmethod
    def getNumTelephone(idAdherent) : 
      BDD.cur.execute("""SELECT numeroTelAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod
    def getMail(idAdherent) : 
      BDD.cur.execute("""SELECT adresseMailAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]
    
    @staticmethod
    def getAdresse(idAdherent) : 
      BDD.cur.execute("""SELECT adresseAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]
      
    @staticmethod
    def getCodePostal(idAdherent) : 
      BDD.cur.execute("""SELECT codePostalAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]
      
    @staticmethod
    def getVille(idAdherent) : 
      BDD.cur.execute("""SELECT villeAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod
    def getDatePaiement(idAdherent) : 
      BDD.cur.execute("""SELECT datePaiementAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]
    
    @staticmethod  
    def getEmpruntEnCours(idAdherent) : 
      BDD.cur.execute("""SELECT idEmprunt FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod 
    def getReservEnCours(idAdherent) : 
      BDD.cur.execute("""SELECT idReservation FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod  
    def getNbreRetards(idAdherent) : 
      BDD.cur.execute("""SELECT nombreRetardAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod  
    def getNbJoursRetards(idAdherent) : 
      BDD.cur.execute("""SELECT nombreJourRetardAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod  
    def getEstAdministrateur(idAdherent) : 
      BDD.cur.execute("""SELECT estAdminAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]

    @staticmethod
    def getNbReservAnnulees(idAdherent) : 
      BDD.cur.execute("""SELECT reservationAnnuleAdherent FROM Adherent WHERE idAdherent = ?""",(idAdherent,))
      return BDD.cur.fetchone()[0]
      
    @staticmethod
    def getAge(idAdherent):
      return ((datetime.date.today() - Adherent.getNaissance(idAdherent)).year)
      
#Fonctions usuelles:

    @staticmethod
    def aUnEmpruntEnCours(idAdherent):
      return(Adherent.getEmpruntEnCours(idAdherent) != None)
      
    @staticmethod
    def aUneReservationEnCours(idAdherent):
      return(Adherent.getReservEnCours(idAdherent) != None)

    @staticmethod
    def estAJour(idAdherent):
      annee = datetime.timedelta(days=365)
      dateFinAbonnement = Adherent.getDatePaiement(idAdherent) + annee
      return(datetime.date.today() < dateFinAbonnement)

    @staticmethod
    def getAllAdherent():
      BDD.cur.execute("""SELECT * FROM Adherent""")
      return BDD.cur.fetchall()
      
    @staticmethod
    def getAdherentByName(nomAdherent):
      nomAdherents = nomAdherent + "%"
      BDD.cur.execute("""SELECT * FROM Adherent WHERE nomAdherent LIKE nomAdherents""")
      return BDD.cur.fetchall()
      
    @staticmethod
    def getAllEmpruntAdherent(idAdherent):
      BDD.cur.execute("""SELECT * FROM Emprunt WHERE idAdherent =?""",(idAdherent,))
      return BDD.cur.fetchall()
      
    @staticmethod
    def getAllReservationAdherent(idAdherent):
      BDD.cur.execute("""SELECT * FROM Reservation WHERE idAdherent =?""",(idAdherent,))
      return BDD.cur.fetchall()

    @staticmethod
    def ajoutRetard(idAdherent):
        BDD.cur.execute("""UPDATE Adherent SET nombreRetardAdherent = ?
                        WHERE idAdherent = ?""",(Adherent.getNbreRetards(idAdherent)+1,
                                                 idAdherent))
        BDD.conn.commit()

    @staticmethod
    def ajoutJourRetard(idAdherent, joursRetards):
        BDD.cur.execute("""UPDATE Adherent SET nombreJourRetardAdherent = ?
                        WHERE idAdherent = ?""",(Adherent.getNbJoursRetards(idAdherent)+joursRetards,
                                                 idAdherent))
        BDD.conn.commit()
        
    @staticmethod
    def ajoutReservAnnule(idAdherent):
        BDD.cur.execute("""UPDATE Adherent SET reservationAnnuleAdherent = ?
                    WHERE idAdherent = ?""",(Adherent.getNbReservAnnulees(idAdherent)+1,
                                             idAdherent))
        BDD.conn.commit()
        
    @staticmethod
    def retardEnPlus(idAdherent, joursRetards):
      Adherent.ajoutJourRetard(idAdherent, joursRetards)
      Adherent.ajoutRetard(idAdherent)


    @staticmethod
    def supprimerAdherent(idAdherent):
        BDD.cursor.execute("""DELETE FROM Adherent WHERE idAdherent= ?""",(idAdherent,))
        BDD.conn.commit()

    @staticmethod
    def ajoutAdherent(nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent,  pseudoAdherent, adresseMailAdherent):
        BDD.cur.execute("""SELECT MAX(idAdherent) FROM Adherent""")
        f = BDD.cur.fetchone()[0]
        if (f==None):
            idAdherent = 1
        else:
            idAdherent =f+1
        BDD.cur.execute("""INSERT INTO Adherent(idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent,
            villeAdherent, numeroTelAdherent, pseudoAdherent, motDePasseAdherent, adresseMailAdherent, estAdminAdherent, datePaiementAdherent, nombreRetardAdherent, nombreJourRetardAdherent, reservationAnnuleAdherent, idEmprunt, idReservation) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
          (idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent,  pseudoAdherent, prenomAdherent+"."+nomAdherent, adresseMailAdherent, False, datetime.datetime.now(), 0,0, 0, None,None))
        BDD.conn.commit()
        
        #cur.execute("""INSERT INTO Adherent(idAdherent, nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent,
        #villeAdherent, numeroTelAdherent, pseudoAdherent, motDePasseAdherent, adresseMailAdherent, estAdminAdherent, datePaiementAdherent, nombreRetardAdherent, nombreJourRetardAdherent, reservationAnnuleAdherent, idEmprunt, idReservation) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        #(0, "Istrateur", "Admin", datetime.date(1,1,1), "", 34000, "Montpellier", "0000000000",  "Admin", "Admin", "", True, datetime.date.today(), 0, 0, 0, 0, 0))
        
            
    @staticmethod
    def compareMDP(idAdherent, motDePasse):
      return(motDePasse == Adherent.getMotDePasse(idAdherent))
    
    @staticmethod
    def reinitialiserMDPAdherent(idAdherent):
        BDD.cur.execute("""UPDATE Adherent SET motDePasseAdherent = ? WHERE idAdherent = ?""",(Adherent.getPrenomAdh(idAdherent)+"."+Adherent.getNomAdh(idAdherent),idAdherent))
        BDD.conn.commit()
        
    @staticmethod
    def pseudoExisteDeja(pseudo):
      BDD.cur.execute("""SELECT pseudoAdherent FROM Adherent""")
      pseudosExistants = BDD.cur.fetchall()
      return(pseudo in pseudosExistants)
