import datetime
import sqlite3
import Jeu
import Adherent
import Emprunt

conn = sqlite3.connect("ludotheque.db")
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
  FOREIGN KEY (idJeu) REFERENCES Jeu(idJeu),
  FOREIGN KEY (idExtension) REFERENCES Extension(idExtension),
  FOREIGN KEY (idAdherent) REFERENCES Adherent(idAdherent))""")
conn.commit()

class Reservation:
  
  #setters
  
  @staticmethod
  def setDateReserv(idReservation, dateReservation) :    
        cur.execute("""UPDATE Reservation SET dateReservation = ? WHERE idReservation = ?""",
                          (dateReservation, idReservation))
        conn.commit()
  
  @staticmethod
  def setDureeEmpruntPrevue(idReservation, dureeEmpruntPrevue) :   
        cur.execute("""UPDATE Reservation SET dureeEmpruntPrevue = ? WHERE idReservation = ?""",
                          (dureeEmpruntPrevue, idReservation))
        conn.commit()


  #getters
  
  @staticmethod
  def getIdReserv(idAdherent):
    cur.execute("""SELECT idReservation FROM Reservation WHERE idAdherent = ?""", (idAdherent,))
    return cur.fetchone()[0]
  
  @staticmethod
  def getIdJeuReserv(idReservation):
    cur.execute("""SELECT idJeu FROM Reservation WHERE idReservation = ?""",(idReservation,))
    return cur.fetchone()[0]
  
  @staticmethod
  def getIdAdhReserv(idReservation):
    cur.execute("""SELECT idAdherent FROM Reservation WHERE idReservation = ?""",(idReservation,))
    return cur.fetchone()[0]
  
  @staticmethod
  def getIdExtensionReserv(idReservation):
    cur.execute("""SELECT idExtension FROM Reservation WHERE idReservation = ?""",(idReservation,))
    return cur.fetchone()[0]
  
  @staticmethod
  def getDateReserv(idReservation):
    cur.execute("""SELECT dateReservation FROM Reservation WHERE idReservation = ? """, (idReservation,))
    return cur.fetchone()[0]
  
  @staticmethod
  def getDureeEmpruntPrevue(idReservation):
    cur.execute("""SELECT dureeEmpruntPrevue FROM Reservation WHERE idReservation =?""",(idReservation,))
    return cur.fetchone()[0]
    
  #Fonctions usuelles:
  
  @staticmethod
  def afficherTableReservation():
    cur.execute("""SELECT * FROM Reservation""")
    return cur.fetchall()
  
  @staticmethod
  def ajoutReservation():
    cur.execute("""SELECT MAX(idReservation) FROM Reservation""")
    f = cur.fetchone()[0]
    if (f==None):
      idReservation = 1
    else:
      idReservation =f+1
    cur.execute("""INSERT INTO Reservation(
                 idReservation, idJeu, idAdherent, idExtension, dateReservation, dureeEmpruntPrevue)
                VALUES(?, ?, ?, ?, ?, ?)""",
                (idReservation, idJeu, idAdherent, idExtension, datetime.now(), 7)) #7 jours d'emprunts : a faire
    conn.commit()
  
  @staticmethod
  def annulerReserv(idReservation):
    Jeu.ajoutExemplaire(Reservation.getIdJeuReserv(idReservation))
    Adherent.ajoutReservAnnule(Reservation.getIdAdherent(idReservation))
    cur.execute("""DELETE FROM Reservation WHERE idReservation = ?""",
                      (idReservation,))
    conn.commit()
  
  @staticmethod 
  def enAttente(idReservation):
    return (datetime.date.today() > Jeu.getDateReserv(idReservation))
    
  
   
  
