import sqlite3
from Utilisateur import Utilisateur


conn = sqlite3.connect("Ludotheque.db")
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

def createTable():
        cur.execute("""CREATE TABLE IF NOT EXISTS EnsUtilisateurs(
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                        username STRING,
                        password STRING,
                        abonnementValide BOOLEAN,
                        empruntEnCours BOOLEAN,
                        reservationEnCours BOOLEAN,
                        nbRetard INTEGER)""")
        conn.commit()


def destroyTable():
        cur.execute("""DROP TABLE EnsUtilisateurs""")
        conn.commit()

def has_username(username):
        cur.execute("""SELECT user_id FROM EnsUtilisateurs WHERE username = ?""",(username,))
        result=cur.fetchone()
        return result != None


def is_password(password,User):
        cur.execute("""SELECT password FROM EnsUtilisateurs WHERE user_id = ?""",(User.get_user_id(),))
        result=cur.fetchone()
        return str(result[0]) == password

def get_nombre_utilisateurs():
        cur.execute("""SELECT COUNT(User_id) FROM EnsUtilisateurs""")
        result=cur.fetchone()
        return result[0]

def get_user(user_id=None,username=None):
        if (user_id != None): cur.execute("""SELECT * FROM EnsUtilisateurs WHERE user_id = ?""",(user_id,))
        if (username != None): cur.execute("""SELECT * FROM EnsUtilisateurs WHERE username = ?""",(username,))
        # Return User
        try:
                result= cur.fetchone()
                return Utilisateur(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
        except:
                print "ID non valide"
        


def delete_user(User):
        try:
                cur.execute("""DELETE FROM EnsUtilisateurs WHERE user_id = ?""",(User.get_user_id(),))
                conn.commit()
        except: 
                print "Erreur lors de la suppression !"
def user_to_table(User):
        # User -> List
        UserTable=(User.get_user_id(),User.get_username(),User.get_password(),User.get_abonnementValide(),User.get_empruntEnCours(),User.get_reservationEnCours(),User.get_nbRetard())
        return UserTable

def rechercher(username): # RAJOUTER PLUSIEURS RESULTATS :: fetchall()
        cur.execute("""SELECT * FROM EnsUtilisateurs WHERE username LIKE ?""",(username,))
        rows = cur.fetchall()
        return rows

def insert(User):
        # VERIFIER SI USERNAME EXISTES PAS DEJA
        if not(has_username(User.get_username())):
                try:	
                        cur.execute("""INSERT INTO EnsUtilisateurs(user_id,username,password,abonnementValide,empruntEnCours,reservationEnCours,nbRetard) 
                                       VALUES (?,?,?,?,?,?,?)""",user_to_table(User))
                        conn.commit()
                        print("Utilisateur ajoute avec succes !")
                except:
                        print("Erreur lors de l'ajout de l'utilisateur")
        else:
                print("Erreur: Utilisateur deja existant")
                

def printAll():
        cur.execute("""SELECT * FROM EnsUtilisateurs""")
        rows = cur.fetchall()
        return rows
        #for row in rows:
                #print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
