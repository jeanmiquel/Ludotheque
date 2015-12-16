import sqlite3
import datetime

import BDD

BDD.cur.execute("""CREATE TABLE IF NOT EXISTS `Categorie` (
`idCategorie` int(6) NOT NULL,
`nomCategorie` varchar(25) NOT NULL,
PRIMARY KEY (`idCategorie`))""")
BDD.conn.commit()

BDD.cur.execute("""CREATE TABLE IF NOT EXISTS `Appartient` (
`idCategorie` int(6) NOT NULL,
`idJeu` int(6) NOT NULL,
PRIMARY KEY (`idCategorie`,`idJeu`),
FOREIGN KEY (`idCategorie`) REFERENCES Categorie(`idCategorie`),
FOREIGN KEY (`idJeu`) REFERENCES Jeu(`idJeu`)
)""")
BDD.conn.commit()

class Categorie :
  
  #setters
  @staticmethod
  def setNomCategorie(idCategorie, nomCategorie) :
    BDD.cur.execute("""UPDATE Categorie SET nomCategorie = ? WHERE idCategorie = ?""",
                (nomCategorie, idCategorie))
    BDD.conn.commit()
    
  #getters
    @staticmethod
    def getIdCategorie(nomJeu):
      BDD.cur.execute("""SELECT idCategorie FROM Categorie WHERE nomCategorie = ?""",(nomCategorie,))
      return BDD.cur.fetchone()[0]
    
  @staticmethod
  def getNomCategorie(idCategorie) :
    BDD.cur.execute("""SELECT nomCategorie FROM Categorie WHERE idCategorie = ?""",(idCategorie,))
    return BDD.cur.fetchone()[0]
    
  #Fonctions usuelles
  
  @staticmethod
  def getAllCategories():
    BDD.cur.execute("""SELECT * FROM Categorie""")
    return BDD.cur.fetchall()
  
  @staticmethod
  def ajoutCategorie(nomCategorie):
    BDD.cur.execute("""SELECT MAX(idCategorie) FROM Categorie""")
    f = BDD.cur.fetchone()[0]
    if (f==None):
        idJeu = 1
    else:
        idJeu =f+1
    BDD.cur.execute("""INSERT INTO Categorie(idCategorie, nomCategorie)
                    VALUES(?, ?)""",(idCategorie, nomCategorie))
    BDD.conn.commit()
            
  @staticmethod
  def supprimerCategorie(idCategorie):
    BDD.cur.execute("""DELETE FROM Categorie WHERE idCategorie = ?""",(idCategorie,))
    BDD.conn.commit()


