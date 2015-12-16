import sqlite3

conn = sqlite3.connect("P:/Piscine/ludotheque.db") # A modifier en fonction du chemin de votre bd
conn.execute('pragma foreign_keys = on')
conn.commit()
cur = conn.cursor()

# exemple de requte et d'affichage des rsultats
# cur.execute("SELECT * FROM Jeu") 
# data = cur.fetchone()
# while (data<>None):
#   print data
#   data = cur.fetchone()
