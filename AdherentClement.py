from datetime import datetime

CREATE TABLE IF NOT EXISTS `Adherent` (
`idAdh` str(6) NOT NULL,
`nomAdh` varchar(25) NOT NULL,
`prenomAdh` varchar(25) NOT NULL,
`dateNaissance` date NOT NULL,
`adresse` varchar(30) NOT NULL,
`codePostal` varchar(10) NOT NULL,
`ville` varchar(10) NOT NULL,
`numTel` int(10) NOT NULL,
`pseudo` varchar(20) NOT NULL,
`password` varchar(26) NOT NULL,
`mail` varchar(50) NOT NULL,
`estAdmin` tinyint(1) NOT NULL,
`dateAbonnement` date NOT NULL,
`nbreRetards` int(3) NOT NULL,
`nbreJourRetards` int(3) NOT NULL,
`nbreReservAnnulees` int(3) NOT NULL,
`idEmprunt` int(11) NOT NULL,
`idReserv` int(11) NOT NULL,
PRIMARY KEY (`idAdherent`)
)


class Adherent :

    def __init__(self, nomAdh : str, pseudoAdh : str, password : str, numTel : str, mail : str, adresse : str, dataBase = BD):
      self.cursor = dataBase.cursor()
      self.Table = "Adherent"
      self.idAdherent = str(mail)
      self.cursor.execute("""INSERT INTO Adherent(
      idAdherent, nomAdh, pseudoAdh, password, numTel, mail, adresse, dateAbonnement, empruntEnCours, reservEnCours, nbreRetards, nbreJoursRetards, estAdmin, nbreReservAnnulees)
      VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
      (self.idAdherent, nomAdh, pseudoAdh, password, numTel, mail, adresse, "", None, None, 0, 0, False, 0))


#setters ?

    def setIdAdh(self, idAdh : str) : #On modifie l'id du jeu, dans l'objet et dans la BD
      self.cursor.execute("""UPDATE Adherent SET idAdh = ? WHERE idAdh = ?""",
      (idAdh, self.idAdh))
      self.idAdh = idAdh
      return self

    def setNomAdh(self, nomAdh : str) : #On modifie le nom du jeu dans la DB et donc son id
      self.cursor.execute("""UPDATE Adherent SET nomAdh = ? WHERE idAdh = ?""",
      (nomAdh, self.idAdh))
      return self

    def setPseudo(self, pseudoAdh : str) : #On modifie la date du jeu, et donc son id
      self.cursor.execute("""UPDATE Adherent SET pseudoAdh = ? WHERE idAdh = ?""",
      (pseudoAdh, self.idAdh))
      return self

    def setPassword(self, password : str):
      self.cursor.execute(""" UPDATE Adherent SET password = ? WHERE idAdh = ?""",(password,self.idAdh))
      return self

    def setNumTel(self, numTel : str):
      self.cursor.execute(""" UPDATE Adherent SET numTel = ? WHERE idAdh = ?""",(numTel,self.idAdh))
      return self

    def setMail(self, mail : str):
      self.cursor.execute(""" UPDATE Adherent SET mail = ? WHERE idAdh = ?""",(mail,self.idAdh))
      return self
      
    def setAdresse(self, adresse : str):
      self.cursor.execute(""" UPDATE Adherent SET adresse = ? WHERE idAdh = ?""",(adresse,self.idAdh))
      return self

    def setDateAbonnement(self, dateAbonnement : Date):
      self.cursor.execute(""" UPDATE Adherent SET dateAbonnement = ? WHERE idAdh = ?""",(dateAbonnement,self.idAdh))
      return self

    def setEmpruntEnCours(self, empruntEnCours : Emprunt):
      self.cursor.execute(""" UPDATE Adherent SET empruntEnCours = ? WHERE idAdh = ?""",(empruntEnCours,self.idAdh))
      return self

    def setReservEnCours(self, reservEnCours : Reservation):
      self.cursor.execute(""" UPDATE Adherent SET reservEnCours = ? WHERE idAdh = ?""",(reservEnCours,self.idAdh))
      return self

    def setNbreRetards(self, nbreRetards : int):
      self.cursor.execute(""" UPDATE Adherent SET nbreRetards = ? WHERE idAdh = ?""",(nbreRetards,self.idAdh))
      return self
      
    def setNbreJoursRetards(self, nbreJoursRetards : int):
      self.cursor.execute(""" UPDATE Adherent SET nbreJoursRetards = ? WHERE idAdh = ?""",(nbreJoursRetards,self.idAdh))
      return self

    def setAdmin(self, estAdmin : bool):
      self.cursor.execute(""" UPDATE Adherent SET estAdmin = ? WHERE idAdh = ?""",(estAdmin,self.idAdh))
      return self

    def setNbreReservAnnulees(self, nbreReservAnnulees : int):
      self.cursor.execute(""" UPDATE Adherent SET nbreReservAnnulees = ? WHERE idAdh = ?""",(nbreReservAnnulees,self.idAdh))
      return self

#getters ?

    def getInfoAdh(self) : #Saisir tout d'un coup
      """0 Id, 1 Nom, 2 Pseudo, 3 Mot de passe, 4 Numero de telephone, 5 Mail, 6 Adresse, 7 Date d'abonnement, 8 Emprunt en cours, 9 Reservation en cours, 10 Nombre de retards, 11 Nombre de jours de retards, 12 Statut admin, 13 Nombre Reservations annulees"""
      self.cursor.execute("""SELECT
      idAdherent, nomAdh, pseudoAdh, password, numTel, mail, adresse, dateAbonnement, empruntEnCours, reservEnCours, nbreRetards, nbreJoursRetards, estAdmin, NbreReservAnnulees
      FROM Adherent Where idAdh = ?""",(self.idAdh,))
      return self.cursor.fetchone()

    def getIdAdh(self) :
      return str(self.idAdh) #L'id est accessible dans les attributs

    def getNomAdh(self) : 
      return self.getInfoAdh()[1]

    def getPseudo(self) : 
      return self.getInfoAdh()[2]

    def getPassword(self) : 
      return self.getInfoAdh()[3]

    def getNumTel(self) : 
      return self.getInfoAdh()[4]

    def getMail(self) : 
      return self.getInfoAdh()[5]

    def getNomAdresse(self) : 
      return self.getInfoAdh()[6]

    def getDateAbonnement(self) : 
      return self.getInfoAdh()[7]
      
    def getEmpruntEnCours(self) : 
      return self.getInfoAdh()[8]
      
    def getReservEnCours(self) : 
      return self.getInfoAdh()[9]
      
    def getNbreRetards(self) : 
      return self.getInfoAdh()[10]
      
    def getNbreJoursRetards(self) : 
      return self.getInfoAdh()[11]
      
    def getEstAdmin(self) : 
      return self.getInfoAdh()[12]
      
    def getNbreReservAnnulees(self) : 
      return self.getInfoAdh()[13]
      
#Fonctions usuelles:


    def retirerAdh(self):
      cursor.execute("""DELETE FROM Adherent WHERE idAdh""",(self.idAdh,))
      return self
