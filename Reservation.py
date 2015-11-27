import datetime
import sqlite3
from Jeu import Jeu
from Adherent import Adherent
from Emprunt import Emprunt

conn = sqlite3.connect("/Users/david.ringayen/Desktop/Ludotheque-master\Ludotheque.db")
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
  PRIMARY KEY (idReservation),
  FOREIGN KEY (idExtension), 
  FOREIGN KEY (idJeu),
  FOREIGN KEY (idAdherent))""")
conn.commit()

class Reservation:

  def __init__(self, dataBase = conn):
    		self.cursor = dataBase.cursor()
    		self.Table = "Reservation"

    		self.cursor.execute("""INSERT INTO Reservation(
		idReservation, idJeu, idAdherent, idExtension, dateReservation, dureeEmpruntPrevue)
		VALUES(?, ?, ?, ?, ?, ?)""",
    		(self.idReservation, self.idJeu, self.idAdherent, self.idExtension, datetime.now(), 7)) #7 jours d'emprunts

	#setters ?
	def setIdReserv(self, idReservation) :       
    		self.cursor.execute("""UPDATE Reservation SET idReservation = ? WHERE idReservation = ?""",
                        	(idReservation, self.idReservation))
    		self.idReserv = idReservation
    		return self
   	 
	def setDateReserv(self, dateReservation) :    
    		self.cursor.execute("""UPDATE Reservation SET dateReservation = ? WHERE idReservation = ?""",
                        	(dateReservation, self.idReservation))
    		return self

	def setDureeEmpruntPrevue(self, dureeEmpruntPrevue) : 	
    		self.cursor.execute("""UPDATE Reservation SET dureeEmpruntPrevue = ? WHERE idReservation = ?""",
                        	(dureeEmpruntPrevue, self.idReservation))
    		return self


	#getters ?
	
	def getIdReserv(self):
	  return self.idReservation
	  
	def getDateReserv(self):
          self.cursor.execute("""SELECT """, (self.idReservation))
	  return self.dateReservation
	  
	def getDureeEmpruntPrevue(self):
	  return self.dureeEmpruntPrevue
	  
	#Fonctions usuelles:
	
	def annulerReserv(self):
	  self.cursor.execute("""DELETE FROM Reservation Where idReservation = ?""",
	                    (self.idReservation))
	 
	
