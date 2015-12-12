import sqlite3
import datetime

conn = sqlite3.connect("ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS `Categorie` (
`idCategorie` int(6) NOT NULL,
`nomCategorie` varchar(25) NOT NULL,
PRIMARY KEY (`idCategorie`))""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS `Appartient` (
`idCategorie` int(6) NOT NULL,
`idJeu` int(6) NOT NULL,
PRIMARY KEY (`idCategorie`,`idJeu`),
FOREIGN KEY (`idCategorie`) REFERENCES Categorie(`idCategorie`),
FOREIGN KEY (`idJeu`) REFERENCES Jeu(`idJeu`)
)""")
conn.commit()

class Categorie :
  
  #setters
  @staticmethod
  def setNomJeu(idCategorie, nomCategorie) :
    cur.execute("""UPDATE Categorie SET nomCategorie = ? WHERE idCategorie = ?""",
                (nomCategorie, idCategorie))
    conn.commit()
    
  #getters
   @staticmethod
  def getIdCategorie(nomJeu) :
    cur.execute("""SELECT idCategorie FROM Categorie WHERE nomCategorie = ?""",(nomCategorie,))
    return cur.fetchone()[0]
    
  @staticmethod
  def getNomCategorie(idCategorie) :
    cur.execute("""SELECT nomCategorie FROM Categorie WHERE idCategorie = ?""",(idCategorie,))
    return cur.fetchone()[0]
    
  #Fonctions usuelles
  
  @staticmethod
  def afficherTableCategorie():
    cur.execute("""SELECT * FROM Categorie""")
    return cur.fetchall()
  
  @staticmethod
  def ajoutCategorie(nomCategorie):
    cur.execute("""SELECT MAX(idCategorie) FROM Categorie""")
    f = cur.fetchone()[0]
    if (f==None):
        idJeu = 1
    else:
        idJeu =f+1
    cur.execute("""INSERT INTO Categorie(idCategorie, nomCategorie)
                    VALUES(?, ?)""",(idCategorie, nomCategorie))
    conn.commit()
            
  @staticmethod
  def supprimerCategorie(idCategorie):
    cur.execute("""DELETE FROM Categorie WHERE idCategorie = ?""",(idCategorie,))
    conn.commit()

