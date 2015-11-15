import sqlite3
from Utilisateur import Utilisateur


conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsUtilisateurs(
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        name TEXT,
                        pseudo TEXT,
                        password TEXT,
                        numTel TEXT,
                        adresse TEXT
                        abonnementValide BOOLEAN,
                        empruntEnCours BOOLEAN,
                        reservationEnCours BOOLEAN,
                        nbRetard INTEGER)""")
        conn.commit()


def destroyTable():
        cur.execute("""DROP TABLE EnsUtilisateurs""")
        conn.commit()

def has_pseudo(pseudo):
        cur.execute("""SELECT user_id FROM EnsAdherent WHERE pseudo = ?""",(pseudo,))
        result=cur.fetchone()
        return result != None
        
def has_name(name):
        cur.execute("""SELECT user_id FROM EnsAdherent WHERE name = ?""",(name,))
        result=cur.fetchone()
        return result != None


def is_password(password,Adherent):
        cur.execute("""SELECT password FROM EnsAdherent WHERE user_id = ?""",(Adherent.get_user_id(),))
        result=cur.fetchone()
        return str(result[0]) == password

def get_nombre_adherents():
        cur.execute("""SELECT COUNT(user_id) FROM EnsAdherent""")
        result=cur.fetchone()
        return result[0]

def get_user(user_id=None,name=None):
        if (user_id != None): cur.execute("""SELECT * FROM EnsAdherent WHERE user_id = ?""",(user_id,))
        if (name != None): cur.execute("""SELECT * FROM EnsAdherent WHERE username = ?""",(name,))
        # Return User
        try:
                result= cur.fetchone()
                return Adherent(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
        except:
                print "ID non valide"
        


def delete_user(Adherent):
        try:
                cur.execute("""DELETE FROM EnsAdherent WHERE user_id = ?""",(Adherent.get_user_id(),))
                conn.commit()
        except: 
                print "Erreur lors de la suppression !"
def user_to_table(Adherent):
        # User -> List
        AdherentTable=(Adherent.get_user_id(),Adherent.get_name(),Adherent.get_password(),Adherent.get_pseudo(),Adherent.get_abonnementValide(),Adherent.get_empruntEnCours(),Adherent.get_reservationEnCours(),Adherent.get_nbRetard())
        return AdherentTable

def rechercher(name): # RAJOUTER PLUSIEURS RESULTATS :: fetchall()
        cur.execute("""SELECT * FROM EnsAdherent WHERE name LIKE ?""",(name,))
        rows = cur.fetchall()
        return rows

def insert(Adherent):
        # VERIFIER SI USERNAME EXISTES PAS DEJA
        if not(has_name(Adherent.get_name())):
                try:	
                        cur.execute("""INSERT INTO EnsAdherent(user_id,username,pseudo,password,abonnementValide,empruntEnCours,reservationEnCours,nbRetard) 
                                       VALUES (?,?,?,?,?,?,?)""",user_to_table(Adherent))
                        conn.commit()
                        print("Adherent ajoute avec succes !")
                except:
                        print("Erreur lors de l'ajout de l'adherent")
        else:
                print("Erreur: Adherent deja existant")
                

def printAll():
        cur.execute("""SELECT * FROM EnsAdherent""")
        rows = cur.fetchall()
        return rows
        #for row in rows:
                #print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
