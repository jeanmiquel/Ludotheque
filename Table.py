import BDD

##BDD.cur.execute("""DROP TABLE Reservation""")
##BDD.cur.execute("""DROP TABLE Emprunt""")
##BDD.cur.execute("""DROP TABLE Adherent""")
##BDD.cur.execute("""DROP TABLE Categorie""")
##BDD.cur.execute("""DROP TABLE Appartient""")
##BDD.cur.execute("""DROP TABLE Extension""")
##BDD.cur.execute("""DROP TABLE Jeu""")
##BDD.conn.commit()


BDD.cur.execute("""CREATE TABLE IF NOT EXISTS Reservation 
  (idReservation int(6) NOT NULL, 
  idAdherent int(6) NOT NULL, 
  idJeu int(6), 
  idExtension int(6), 
  dateReservation date NOT NULL, 
  dureeEmpruntPrevue int(3) NOT NULL, 
  PRIMARY KEY (idReservation),
  FOREIGN KEY (idJeu) REFERENCES Jeu(idJeu),
  FOREIGN KEY (idExtension) REFERENCES Extension(idExtension),
  FOREIGN KEY (idAdherent) REFERENCES Adherent(idAdherent))""")
BDD.conn.commit()

BDD.cur.execute("""CREATE TABLE IF NOT EXISTS `Emprunt` (
                                `idEmprunt` int(6) NOT NULL,
                                `idAdherent` int(6) NOT NULL,
                                `idJeu` int(6),
                                `idExtension` int(6),
                                `dateDebutEmprunt` date NOT NULL,
                                `dateRenduEmprunt` date NOT NULL,
                                `dureePrevueEmprunt` int(3) NOT NULL,
                                PRIMARY KEY (`idEmprunt`),
                                FOREIGN KEY (`idAdherent`) REFERENCES Adherent(`idAdherent`),
                                FOREIGN KEY (`idExtension`) REFERENCES Extension(`idExtension`),
                                FOREIGN KEY (`idJeu`) REFERENCES Jeu(`idJeu`)
                                )""")
BDD.conn.commit()

BDD.cur.execute("""CREATE TABLE IF NOT EXISTS `Adherent` (
                    `idAdherent` int(6) NOT NULL,
                    `nomAdherent` varchar(25) NOT NULL,
                    `prenomAdherent` varchar(25) NOT NULL,
                    `dateNaissanceAdherent` date NOT NULL,
                    `adresseAdherent` varchar(30) NOT NULL,
                    `codePostalAdherent` varchar(10) NOT NULL,
                    `villeAdherent` varchar(10) NOT NULL,
                    `numeroTelAdherent` int(10) NOT NULL,
                    `pseudoAdherent` varchar(20) NOT NULL,
                    `motDePasseAdherent` varchar(26) NOT NULL,
                    `adresseMailAdherent` varchar(50) NOT NULL,
                    `estAdminAdherent` tinyint(1) NOT NULL,
                    `datePaiementAdherent` date,
                    `nombreRetardAdherent` int(3) NOT NULL,
                    `nombreJourRetardAdherent` int(3) NOT NULL,
                    `reservationAnnuleAdherent` int(3) NOT NULL,
                    `idEmprunt` int(11),
                    `idReservation` int(11),
                    PRIMARY KEY (`idAdherent`)
                    FOREIGN KEY (`idEmprunt`) REFERENCES Emprunt(`idEmprunt`),
                    FOREIGN KEY (`idReservation`) REFERENCES Reservation(`idReservation`))""")
BDD.conn.commit()

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

BDD.cur.execute("""CREATE TABLE IF NOT EXISTS `Extension`
    (`idExtension` int(6) NOT NULL, 
     `idJeu` int(6) NOT NULL, 
     `nomExtension` varchar(20) NOT NULL, 
     `nbreTotalExtension` int(3) NOT NULL,
     PRIMARY KEY (`idExtension`)
     FOREIGN KEY (`idJeu`) REFERENCES Jeu(`idJeu`))""")
BDD.conn.commit()

BDD.cur.execute("""CREATE TABLE IF NOT EXISTS `Jeu` (
`idJeu` int(6) NOT NULL,
`nomJeu` varchar(50) NOT NULL,
`anneeJeu` int(4) NOT NULL,
`ageJeu` int(2) NOT NULL,
`nbJoueurJeu` varchar(5) NOT NULL,
`quantiteJeu` int(3) NOT NULL,
`auteurJeu` varchar(20) NOT NULL,
`illustrateurJeu` varchar(20) NOT NULL,
`editeurJeu` varchar(20) NOT NULL,
`estEmpruntableJeu` tinyint(1) NOT NULL,
`synopsisJeu` varchar(200) NOT NULL,
PRIMARY KEY (`idJeu`))""")
BDD.conn.commit()
