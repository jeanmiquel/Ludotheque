import sqlite3
from Jeu import Jeu



con = sqlite3.connect("Ludotheque.db")                    
con.execute('pragma foreign_keys = on')
con.commit()
cur = con.cursor()
def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsJeux(
                        id_Jeu INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Nom_Jeu TEXT,
                        Annee INTEGER,
                        Editeur TEXT,
                        Age INTEGER,
                        NombreJoueurs TEXT,
                        Description TEXT)""")
        con.commit()


def suppTable():
        cur.execute("""DROP TABLE EnsJeux""")
        con.commit()


def get_Jeu(id_Jeu=None,Nom_jeu=None):
        if (id_Jeu!=None): cur.execute("""SELECT * FROM EnsJeux WHERE Jeu_id = ?""",(Jeu_id,))
        if (Nom_Jeu!=None): cur.execute("""SELECT * FROM EnsJeux WHERE Nom_jeu = ?""",(Nom_jeu,))
        try:     
                result=cur.fetchone()
                return Jeu(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
        except:
                print "Erreur: ID du jeu non valide"

def suppJeu(Jeu):
        try:
                cur.execute("""DELETE FROM EnsJeux WHERE id_Jeu = ?""",(Jeu.get_id_Jeu(),))
                con.commit()
        except: 
                print "Erreur lors de la suppression !"

def has_Jeu(Nom_jeu):
        cur.execute("""SELECT id_Jeu FROM EnsJeux WHERE Nom_Jeu = ?""",(Nom_Jeu,))
        result=cur.fetchone()
        return result != None


def jeu_to_table(Jeu):
        # User -> List
        JeuTable=(Jeu.get_id_Jeu(),Jeu.get_Nom_Jeu(),Jeu.get_Annee(),Jeu.get_Editeur(),Jeu.get_Age(),Jeu.get_NombreJoueurs(),Jeu.get_Description())
        return JeuTable

def insert(Jeu):
        """Fonction permettant d'inserer un jeu dans l'ensemble de Jeux
        #Jeu x EnsJeux => EnsJeux
        >>>EnsJeux.insert(Type Jeu)"""
        if not(has_Jeu(Jeu.get_Nom_Jeu())):
                try:	
                        cur.execute("""INSERT INTO EnsJeux(id_Jeu,Nom_Jeu,Annee,Editeur,Age,NombreJoueurs,Description) VALUES (?, ?, ?, ?, ?, ?, ?)""",jeu_to_table(Jeu))
                        con.commit()
                        print("Jeu ajoute avec succes !")
                except:
                        print (jeu_to_table(Jeu))
                        print("Erreur lors de l'ajout du jeu")
        else:
                print("Erreur: Un jeu est deja enregistre au meme nom.")        


#### FONCTION SEULEMENT POUR IMPORTATION DE LA BASE INITIAL DES JEUX #####

def insertFromMain(Nom,Annee,Editeur,Age,NombreJoueurs,Description=""):
        """Fonction permettant d'inserer un jeu dans l'ensemble de Jeux
        #Jeu x EnsJeux => EnsJeux
        >>>EnsJeux.insert(Type Jeu)"""
        try:	
                cur.execute("""INSERT INTO EnsJeux(Nom_Jeu,Annee,Editeur,AgeMini,NombreJoueurs,Description) VALUES (?, ?, ?, ?, ?, ?)""",(Nom,Annee,Editeur,Age,NombreJoueurs,Description,))
                conn.commit()
        except:
                print(Nom,Annee,Editeur,Age,NombreJoueurs)
                
##########################################################################
     

                
def rechercher(nom):           # RAJOUTER PLUSIEURS RESULTATS :: fetchall()
        cur.execute("""SELECT * FROM EnsJeux WHERE Nom_Jeu LIKE ?""",(nom,))
        result = cur.fetchone()
        return Jeu(result[0],result[1],result[2],result[3])

def update(Jeu):
        """ Fonction permettant d'actualiser les infos d'un jeu dans l'ensemble de Jeux"""
        # A FAIRE !

def printAll():
        cur.execute("""SELECT * FROM EnsJeux""") 
        rows = cur.fetchall()
        return rows
        #for row in rows:
                #print('{0} : {1} - {2} : {3}'.format(row[0], row[1], row[2], row[3]))
