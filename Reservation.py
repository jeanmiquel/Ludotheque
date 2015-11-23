import Jeu
import Adherent

CREATE TABLE IF NOT EXISTS Reservation 
  (idReserv str(6) NOT NULL, 
  idAdh str(6) NOT NULL, 
  idJeu str(6) NOT NULL, 
  idExt str(6) NOT NULL, 
  dateReserv date NOT NULL, 
  dureeEmpruntPrevue int(3) NOT NULL, 
  KEY fk_idExtR(idExtension), 
  KEY fk_idJeuR (idJeu),
  KEY fk_idAdhR (idAdherent))


class Reservation:

  def __init__(self, dataBase = BD):
    		self.cursor = dataBase.cursor()
    		self.Table = "Reservation"

    		self.cursor.execute("""INSERT INTO Reservation(
		idReserv, idJeu, idAdh, idExt, dateReserv, dureeEmpruntPrevue)
		VALUES(?, ?, ?, ?, ?, ?)""",
    (self.idReserv, self.idJeu, self.idAdh, self.idExt, date, 14)) #14 jours

	#setters ?
	def setIdReserv(self, idReserv : str) :       
    		self.cursor.execute("""UPDATE Reservation SET idReserv = ? WHERE idReserv = ?""",
                        	(idReserv, self.idReserv))
    		self.idReserv = idReserv
    		return self
   	 
	def setDateReserv(self, dateReserv : date) :    
    		self.cursor.execute("""UPDATE Reservation SET dateReserv = ? WHERE idReserv = ?""",
                        	(dateReserv, self.idReserv))
    		return self

	def setDureeEmpruntPrevue(self, dureeEmpruntPrevue : int) : 	
    		self.cursor.execute("""UPDATE Reservation SET dureeEmpruntPrevue = ? WHERE idReserv = ?""",
                        	(dureeEmpruntPrevue, self.idReserv))
    		return self


	#getters ?
	
	def getIdReserv(self):
	  return self.idReserv
	  
	def getDateReserv(self):
	  return self.dateReserv
	  
	def getDureeEmpruntPrevue(self):
	  return self.dureeEmpruntPrevue
	  
	#Fonctions usuelles:
	
	def annulerReserv(self):
	  self.cursor.execute("""DELETE FROM Reservation Where idReserv = ?""",
	                    (self.idReserv))
	 
	
