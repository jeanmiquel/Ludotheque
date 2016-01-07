#-*- coding: utf-8 -*-
import datetime
import sqlite3
import Jeu
import Adherent
import Emprunt
from datetime import timedelta

import BDD

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
                (idReservation, idJeu, idAdherent, 0, dateReservation, dureeEmpruntPrevue)) 
    BDD.conn.commit()
    
  @staticmethod
  def reserverExtensionAvecJeu(idAdherent, idExtension, dateReservation, dureeEmpruntPrevue):
    idJeuExt = Extension.getIdJeu(idExtension) #on rÃ©cupÃ¨re l'id du jeu correspondant Ã  l'extension
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
                (idReservation, 0, idAdherent, idExtension, dateReservation, dureeEmpruntPrevue)) 
    BDD.conn.commit()
  
  @staticmethod
  def supprimerReserv(idReservation):
    BDD.cur.execute("""DELETE FROM Reservation WHERE idReservation = ?""",
                      (idReservation,))
    BDD.cur.commit()
  
  @staticmethod
  def annulerReservApresDateButoire(idReservation):
    Adherent.ajoutReservAnnule(Reservation.getIdAdhReserv(idReservation))     #on incrÃ©ment son nombre d'annulation
    Adherent.setReservEnCours(Reservation.getIdAdhReserv(idReservation), None) #on annule l'id Reservation chez l'adhÃ©rent
    Reservation.supprimerReserv(idReservation)
    
  @staticmethod
  def annulerReservAvantDateButoire(idReservation):
    Adherent.setReservEnCours(Reservation.getIdAdhReserv(idReservation), None) #on annule l'id Reservation chez l'adhÃ©rent
    Reservation.supprimerReserv(idReservation)
    
  @staticmethod
  def validerEmprunt(idReservation, date):
    Adherent.setReservEnCours(Reservation.getIdAdhReserv(idReservation), None) #on annule l'id Reservation chez l'adhÃ©rent
    if ((Reservation.aUnJeu(idReservation))and(Reservation.aUneExtension(idReservation))):  #si l'adherent a rÃ©servÃ© 1 jeu + 1 extension
        Emprunt.emprunterExtensionAvecJeu(Reservation.getIdAdhReserv(idReservation), 
                                          Reservation.getIdExtensionReserv(idReservation),
                                         date, Reservation.getDureeEmpruntPrevue(idReservation))
    elif (Reservation.aUnJeu(idReservation)):                           #si l'adherent a rÃ©servÃ© juste 1 jeu
        Emprunt.emprunterJeu(Reservation.getIdAdhReserv(idReservation), 
                           Reservation.getIdJeuReserv(idReservation),
                           date, Reservation.getDureeEmpruntPrevue(idReservation))
    else:                                                              #si l'adherent a rÃ©servÃ© juste 1 extension
        Emprunt.emprunterExtensionSansJeu(Reservation.getIdAdhReserv(idReservation), 
                                          Reservation.getIdExtensionReserv(idReservation),
                                         date, Reservation.getDureeEmpruntPrevue(idReservation))
    Reservation.supprimerReserv(idReservation)
  
  @staticmethod 
  def enAttente(idReservation):
    return (datetime.date.today() > datetime.date(int(Reservation.getDateReserv(idReservation)[0:4]),int(Reservation.getDateReserv(idReservation)[5:7]),int(Reservation.getDateReserv(idReservation)[8:10])))
    
    
  @staticmethod
  def getDateFinEmprunt(idReservation):
    return datetime.date(int(Reservation.getDateReserv(idReservation)[0:4]),int(Reservation.getDateReserv(idReservation)[5:7]),int(Reservation.getDateReserv(idReservation)[8:10])) + timedelta(Reservation.getDureeEmpruntPrevue(idReservation))
  
   
  
