import sqlite3

conn = sqlite3.connect("P:/Piscine/ludotheque.db") # A modifier en fonction du chemin de votre bd

cur = conn.cursor()

# exemple de requête et d'affichage des résultats
# cur.execute("SELECT * FROM Jeu") 
# data = cur.fetchone()
# while (data<>None):
#   print data
#   data = cur.fetchone()
