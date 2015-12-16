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
  def getAllReservations():
    BDD.cur.execute("""SELECT * FROM Reservation""")
    return BDD.cur.fetchall()
  
  @staticmethod
  def ajoutReservation():
    BDD.cur.execute("""SELECT MAX(idReservation) FROM Reservation""")
    f = BDD.cur.fetchone()[0]
    if (f==None):
      idReservation = 1
    else:
      idReservation =f+1
    BDD.cur.execute("""INSERT INTO Reservation(
                 idReservation, idJeu, idAdherent, idExtension, dateReservation, dureeEmpruntPrevue)
                VALUES(?, ?, ?, ?, ?, ?)""",
                (idReservation, idJeu, idAdherent, idExtension, datetime.now(), 7)) #7 jours d'emprunts : a faire
    BDD.conn.commit()
  
  @staticmethod
  def annulerReserv(idReservation):
    Jeu.ajoutExemplaire(Reservation.getIdJeuReserv(idReservation))
    Adherent.ajoutReservAnnule(Reservation.getIdAdherent(idReservation))
    BDD.cur.execute("""DELETE FROM Reservation WHERE idReservation = ?""",
                      (idReservation,))
    BDD.conn.commit()
  
  @staticmethod 
  def enAttente(idReservation):
    return (datetime.date.today() > Jeu.getDateReserv(idReservation))
    
  
   
  
