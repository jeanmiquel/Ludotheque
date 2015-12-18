import datetime
import sqlite3
import Jeu
import Adherent
import Emprunt

import BDD

BDD.cur.execute("""CREATE TABLE IF NOT EXISTS Reservation 
  (idReservation int(6) NOT NULL, 
  idAdherent int(6) NOT NULL, 
  idJeu int(6) NOT NULL, 
  idExtension int(6) NOT NULL, 
  dateReservation date NOT NULL, 
  dureeEmpruntPrevue int(3) NOT NULL, 
  PRIMARY KEY (idReservation),
  FOREIGN KEY (idJeu) REFERENCES Jeu(idJeu),
  FOREIGN KEY (idExtension) REFERENCES Extension(idExtension),
  FOREIGN KEY (idAdherent) REFERENCES Adherent(idAdherent))""")
BDD.conn.commit()

class Reservation:
  
  #setters
  
  @staticmethod
  def setDateReserv(idReservation, dateReservation) :    
        BDD.cur.execute("""UPDATE Reservation SET dateReservation = ? WHERE idReservation = ?""",
                          (dateReservation, idReservation))
        BDD.conn.commit()
  
  @staticmethod
  def setDureeEmpruntPrevue(idReservation, dureeEmpruntPrevue) :   
        BDD.cur.execute("""UPDATE Reservation SET dureeEmpruntPrevue = ? WHERE idReservation = ?""",
                          (dureeEmpruntPrevue, idReservation))
        BDD.conn.commit()


  #getters
  
  @staticmethod
  def getIdReserv(idAdherent):
    BDD.cur.execute("""SELECT idReservation FROM Reservation WHERE idAdherent = ?""", (idAdherent,))
    return BDD.cur.fetchone()[0]
  
  @staticmethod
  def getIdJeuReserv(idReservation):
    BDD.cur.execute("""SELECT idJeu FROM Reservation WHERE idReservation = ?""",(idReservation,))
    return BDD.cur.fetchone()[0]
  
  @staticmethod
  def getIdAdhReserv(idReservation):
    BDD.cur.execute("""SELECT idAdherent FROM Reservation WHERE idReservation = ?""",(idReservation,))
    return BDD.cur.fetchone()[0]
  
  @staticmethod
  def getIdExtensionReserv(idReservation):
    BDD.cur.execute("""SELECT idExtension FROM Reservation WHERE idReservation = ?""",(idReservation,))
    return BDD.cur.fetchone()[0]
  
  @staticmethod
  def getDateReserv(idReservation):
    BDD.cur.execute("""SELECT dateReservation FROM Reservation WHERE idReservation = ? """, (idReservation,))
    return BDD.cur.fetchone()[0]
  
  @staticmethod
  def getDureeEmpruntPrevue(idReservation):
    BDD.cur.execute("""SELECT dureeEmpruntPrevue FROM Reservation WHERE idReservation =?""",(idReservation,))
    return BDD.cur.fetchone()[0]
    
  #Fonctions usuelles:
  
  @staticmethod
  def aUnJeu(idReservation):
    return(Reservation.getIdJeuReserv(idReservation) != None)
  
  @staticmethod
  def aUneExtension(idReservation):
    return(Reservation.getIdExtensionReserv(idReservation) != None)
  
  @staticmethod
  def getAllReservations():
    BDD.cur.execute("""SELECT * FROM Reservation""")
    return BDD.cur.fetchall()
  
  
  @staticmethod
  def reserverJeu(idAdherent, idJeu, dateReservation, dureeEmpruntPrevue):
    BDD.cur.execute("""SELECT MAX(idReservation) FROM Reservation""")
    f = BDD.cur.fetchone()[0]
    if (f==None):
      idReservation = 1
    else:
      idReservation =f+1
    BDD.cur.execute("""INSERT INTO Reservation(
                 idReservation, idJeu, idAdherent, idExtension, dateReservation, dureeEmpruntPrevue)
                VALUES(?, ?, ?, ?, ?, ?)""",
                (idReservation, idJeu, idAdherent, None, dateReservation, dureeEmpruntPrevue)) 
    BDD.conn.commit()
    
    @staticmethod
  def reserverExtensionAvecJeu(idAdherent, idExtension, dateReservation, dureeEmpruntPrevue):
    idJeuExt = Extension.getIdJeu(idExtension) #on récupère l'id du jeu correspondant à l'extension
    BDD.cur.execute("""SELECT MAX(idReservation) FROM Reservation""")
    f = BDD.cur.fetchone()[0]
    if (f==None):
      idReservation = 1
    else:
      idReservation =f+1
    BDD.cur.execute("""INSERT INTO Reservation(
                 idReservation, idJeu, idAdherent, idExtension, dateReservation, dureeEmpruntPrevue)
                VALUES(?, ?, ?, ?, ?, ?)""",
                (idReservation, idJeuExt, idAdherent,idExtension, dateReservation, dureeEmpruntPrevue)) 
    BDD.conn.commit()
    
    @staticmethod
  def reserverExtensionSansJeu(idAdherent, idExtension, dateReservation, dureeEmpruntPrevue):
    BDD.cur.execute("""SELECT MAX(idReservation) FROM Reservation""")
    f = BDD.cur.fetchone()[0]
    if (f==None):
      idReservation = 1
    else:
      idReservation =f+1
    BDD.cur.execute("""INSERT INTO Reservation(
                 idReservation, idJeu, idAdherent, idExtension, dateReservation, dureeEmpruntPrevue)
                VALUES(?, ?, ?, ?, ?, ?)""",
                (idReservation, None, idAdherent, idExtension, dateReservation, dureeEmpruntPrevue)) 
    BDD.conn.commit()
  
  @staticmethod
  def supprimerReserv(idReservation):
    BDD.cur.execute("""DELETE FROM Reservation WHERE idReservation = ?""",
                      (idReservation,))
    BDD.cur.commit()
  
  @staticmethod
  def annulerReservApresDateButoire(idReservation):
    Adherent.ajoutReservAnnule(Reservation.getIdAdhReserv(idReservation))     #on incrément son nombre d'annulation
    Adherent.setReservEnCours(Reservation.getIdAdhReserv(idReservation), None) #on annule l'id Reservation chez l'adhérent
    Reservation.supprimerReserv(idReservation)
    
  @staticmethod
  def annulerReservAvantDateButoire(idReservation):
    Adherent.setReservEnCours(Reservation.getIdAdhReserv(idReservation), None) #on annule l'id Reservation chez l'adhérent
    Reservation.supprimerReserv(idReservation)
    
  @staticmethod
  def validerEmprunt(idReservation, date):
    Adherent.setReservEnCours(Reservation.getIdAdhReserv(idReservation), None) #on annule l'id Reservation chez l'adhérent
    if ((Reservation.aUnJeu(idReservation))and(Reservation.aUneExtension(idReservation))):  #si l'adherent a réservé 1 jeu + 1 extension
        Emprunt.emprunterExtensionAvecJeu(Reservation.getIdAdhReserv(idReservation), 
                                          Reservation.getIdExtensionReserv(idReservation),
                                         date, Reservation.getDureeEmpruntPrevue(idReservation))
    elif (Reservation.aUnJeu(idReservation)):                           #si l'adherent a réservé juste 1 jeu
        Emprunt.emprunterJeu(Reservation.getIdAdhReserv(idReservation), 
                           Reservation.getIdJeuReserv(idReservation),
                           date, Reservation.getDureeEmpruntPrevue(idReservation))
    else:                                                              #si l'adherent a réservé juste 1 extension
        Emprunt.emprunterExtensionSansJeu(Reservation.getIdAdhReserv(idReservation), 
                                          Reservation.getIdExtensionReserv(idReservation),
                                         date, Reservation.getDureeEmpruntPrevue(idReservation))
    Reservation.supprimerReserv(idReservation)
  
  @staticmethod 
  def enAttente(idReservation):
    return (datetime.date.today() > Jeu.getDateReserv(idReservation))
    
  
   
  
