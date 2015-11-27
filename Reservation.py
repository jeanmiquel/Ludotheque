import datetime
import sqlite3
from Jeu import Jeu
from Adherent import Adherent
from Emprunt import Emprunt

conn = sqlite3.connect("P:\Ludotheque-master\Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Reservation 
  (idReservation int(6) NOT NULL, 
  idAdherent int(6) NOT NULL, 
  idJeu int(6) NOT NULL, 
  idExtension int(6) NOT NULL, 
  dateReservation date NOT NULL, 
  dureeEmpruntPrevue int(3) NOT NULL, 
  PRIMARY KEY (idReservation))""")
conn.commit()

class Reservation:

  def __init__(self):
        cur.execute("""INSERT INTO Reservation(
    idReservation, idJeu, idAdherent, idExtension, dateReservation, dureeEmpruntPrevue)
    VALUES(?, ?, ?, ?, ?, ?)""",
        (0, 0, 0, 0, datetime.now(), 7)) #7 jours d'emprunts

  #setters ?
  def setIdReserv(self, idReservation, idAdherent) :                                                                                                                                                                                                                                                                                                                                                                    
        cur.execute("""UPDATE Reservation SET idReservation = ? WHERE idAdherent = ?""",
                          (idReservation, idAdherent))
        conn.commit()
     
  def setDateReserv(self,idReservation, dateReservation) :    
        cur.execute("""UPDATE Reservation SET dateReservation = ? WHERE idReservation = ?""",
                          (dateReservation, idReservation))
        conn.commit()

  def setDureeEmpruntPrevue(self,idReservation, dureeEmpruntPrevue) :   
        cur.execute("""UPDATE Reservation SET dureeEmpruntPrevue = ? WHERE idReservation = ?""",
                          (dureeEmpruntPrevue, idReservation))
        conn.commit()


  #getters ?
  
  def getIdReserv(self):
    cur.execute("""SELECT idReservation FROM Jeu WHERE idAdherent = ?""", (idAdherent))
    return cur.fetchone()[0]
    
  def getIdJeuReserv(self, idReservation):
    
  def getDateReserv(self, idReservation):
    cur.execute("""SELECT dateReservation FROM Reservation WHERE idReservation = ? """, (idReservation))
    return cur.fetchone()[0]
    
  def getDureeEmpruntPrevue(idReservation):
    cur.execute("""SELECT dureeEmpruntPrevue FROM Reservation WHERE idReservation =?""",(idReservation))
    return cur.fetchone()[0]
    
  #Fonctions usuelles:
  
  def annulerReserv(self, idReservation):
    Jeu.ajoutExemplaire(self.getIdJeuReserv(idReservation))
    cur.execute("""DELETE FROM Reservation Where idReservation = ?""",
                      (idReservation))
    conn.commit()
    
  def enAttente(self, idReservation):
    return (datetime.now() > self.getDateReserv(idReservation))
    
  
   
  
