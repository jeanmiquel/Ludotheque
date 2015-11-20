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
                        )""")
        con.commit()

data = [["1000 Bornes","1954","Dujardin","8","2-6",[]],["1775, la Révolution Américaine !","2013","Asynchron","12","14",[]],["6 qui prend !","2009","Gigamic","10","2-10",[]],["7 Wonders","2010","Repos Prod","14","2-7",[]],["A Few Acres of Snow","2011","Treefrog Games","13","2",[]],["Abalone","1989","","","",[]],["Abyss","2014","Bombyx","14","2-4",[]],["Advanced Heroquest","1989","Games Workshop","14","1-5",[]],["Agricola","2008","Ystari Games","12","1-5",["Les Fermiers de la Lande","Belgique"]],["Agricola Terres d'élevage","2012","Filosofia","12","2",["Bâtiments de Ferme"]],["Amytis","2007","Ystari Games","10","2-4",[]],["Anaconda","2009","Smart Games","7","1",[]],["Anti-virus","2009","Smart Games","7","1",[]],["Armada","1986","Jeux Descartes","10","2-4",[]],["Art Moderne","2009","Matagot","8","3-5",[]],["Assyria","2009","Ystari Games","12","2-4",[]],["Automobile","2010","Iello","12","2-4",[]],["Ave Caesar","1989","Ravensburger","12","3-6",[]],["Awele","0","","","2",[]],["Backgammon","0","","","2",[]],["Barony","2015","Matagot","14","2-4",[]],["Bazaar","1967","Schmidt international","12","2-6",[]],["Boomerang","2010","Lui-même","8","3-5",[]],["Brass","2007","White Goblin Games","13","3-4",[]],["Bruxelles 1893","2013","Pearl Games","14","2-5",[]],["Cacao","2015","Filosofia","8","2-4",[]],["Cant Stop!","2006","Asmodee","7","2-4",[]],["Capital Power","1981","International team","13","3-4",[]],["Carcassonne - Die Jäger und Sammler","2002","Hans im Glück","8","2-5",[]],["Cargo Noir","2011","Days of wonder","8","2-5",[]],["Carrom","0","","","2",[]],["Carson City","2009","White Goblin Games","12","2-5",["Gold´n Guns"]],["Caverna","2013","Filosofia","12","1-7",[]],["Caylus","2012","Ystari Games","12","2-5",[]],["Chinatown","2008","Filosofia","12","3-5",[]],["Citadelles","2000","Edge entertainment","14","3-7",[]],["Civilization","1982","Avalon Hill","12","2-7",[]],["Clash of Cultures","2012","Zman Games","12","2-4",["CoC: Civilisations"]],["Claustrophobia","2009","Asmodee","14","2",["De Profondis","Furor sanguinis"]],["Cluedo","1974","Parker","8","2-6",[]],["CoH: Le Réveil de l'Ours","2012","Asynchron","14","2",[]],["Colt Express","2014","Ludonaute","10","2-6",[]],["Concept","2013","Repos Prod","10","4-12",[]],["Conquest of the Empire","2005","Eagle Games","10","2-6",[]],["Contrario","2001","Cocktail Games","12","3-10",[]],["Cry Havoc","1981","Euro Games","12","2",[]],["Cyclades","2012","Matagot","10","2-5",[]],["De Vulgari Eloquentia","2010","Matagot","14","2-5",[]],["Descendance","2011","Gigamic","12","2-4",["Tuiles clients sup","La taverne","Le port"]],["Descent : voyage dans les ténèbres","2006","Edge entertainment","","",["Héros de Légende","Le Puit des Ténèbres","Quest compendium","Le Tombeau de Glace","L’Autel du Désespoir","Mer de Sang"]],["Descent : Voyages dans les Ténèbres ! (Seconde Edition)","2012","Edge entertainment","","",["Kit de conversion"]],["Desperado of Dice Town","2014","Matagot","8","2-4",[]],["Deus","2014","Pearl Games","12","2-4",[]],["Diplomatie","1976","Miro","12","4-7",[]],["Discoveries","2015","Ludonaute","14","2-4",[]],["Dobble","2010","Asmodee","6","2-8",[]],["Dominant Species","2012","Filosofia","12","2-6",[]],["Dominion","2008","Filosofia","8","2-4",[]],["Dominion l’Intrigue","2009","Filosofia","8","2-4",[]],["Dune","1979","Avalon Hill","12","2-6",[]],["Dungeon Lords","2010","Iello","12","2-4",[]],["Earth Reborn","2010","Ludically","10","2-4",[]],["Eclipse","2011","Ystari Games","12","2-6",["Eclipse: L’éveil des anciens"]],["Endeavor","2009","Ystari Games","12","3-5",[]],["Essen the game","2014","Geek Attitude Games","10","2-4",[]],["Euphoria","2014","Morning Players","13","2-6",[]],["Evo","2011","Asmodee","14","2-5",[]],["Fief","1983","International team","10","2-6",[]],["Fief (nouvelle édition)","2011","Asynchron","12","3-6",[]],["Five Tribes","2014","Days of wonder","13","2-4",[]],["Formule Dé","1991","Ludodélire","12","2-10",["World Championship"]],["Fresco","2010","Queen Games","10","2-4",[]],["Galaxy Trucker : édition anniversaire","2013","Iello","10","2-4",[]],["Gear of war","2011","Edge entertainment","13","1-4",[]],["Ghost Stories","2008","Repos Prod","10","1-4",["White Moon","Black Secret","B-Rice Lee","Guardhouse","Village People"]],["Goa","2010","Filosofia","12","2-4",[]],["Gueules noires","2013","Gigamic","10","2-4",[]],["Heroes of Normandie","2014","Devil Pig","10","2",["HoN: D-Day","HoN: Ste Mère l’église","German Army Box"]],["Himalaya","2004","Tilsit","12","3-4",[]],["Hyperborea","2014","Marabunta","12","2-6",[]],["Identik","2009","Asmodee","8","3+",[]],["Infarkt","2011","Czech board games","10","2-5",[]],["Jeu des cochons","1977","Winning Moves","7","2-6",[]],["Jungle Speed","1997","Asmodee","7","3-7",[]],["Junta","1979","Jeux Descartes","14","2-7",[]],["Kahuna","1998","Filosofia","10","2",[]],["Kezako","2007","Cocktail Games","10","4-8",[]],["King and Assassins","2013","Runes Edition","10","2",[]],["King of Tokyo","2011","Iello","8","2-6",[]],["Krosmaster Arena","2012","Ankama Products","12","2-4",[]],["L'Aventurier","2012","Smart Games","7","1",[]],["L'Île interdite","2010","Cocktail Games","10","2-4",[]],["L’Âge de Pierre","2008","Filosofia","10","2-4",[]],["La bataille des cinq armées","2014","Iello","13","2",[]],["La Gloire de Rome","2011","Filosofia","12","2-5",[]],["La Granja","2015","Pearl Games","12","1-4",[]],["La Guerre de l'Anneau","2004","Asmodee","10","2-4",[]],["La Vallée des Mammouths","1991","Ludodélire","12","2-6",[]],["Lancaster","2011","Queen Games","10","2-5",[]],["Le Lièvre et la Tortue","2000","Ravensburger","8","2-6",[]],["Le Seigneur des Anneaux JCE","2011","Edge entertainment","13","1-4",["Les Collines d'Emyn Muil","Les Marais des Morts","Voyage à Rhosgobel"]],["Le Tapis Volant","1987","Ravensburger","10","3-6",[]],["Lemming Mafia","2010","Iello","8","3-6",[]],["Les aventuriers du Rail : 10th anniversary","2014","Days of wonder","8","2-5",[]],["Les Bâtisseurs","2013","Bombyx","10","2-4",[]],["Les Chevaliers de la Table Ronde","2005","Days of wonder","10","3-7",[]],["Les Colons de Catane","1997","Euro Games","10","3-4",["5\/6","Marins"]],["Les Colons de Catane - Le Jeu de Cartes","1999","Kosmos","12","2",["Politique & Intrigues"]],["Les Demeures de l'Épouvante","2011","Edge entertainment","12","2-5",["Expériences interdites","La Saison de la Sorcière","La Tablette d'Argent "]],["Les Loups-Garous de Thiercelieux","2001","Lui-même","8","8-18",[]],["Les Pingouins Patineurs","2011","Smart Games","6","1",[]],["Les Princes de Florence","2007","Ystari Games","12","2-5",[]],["Lewis & Clark","2013","Ludonaute","14","1-5",[]],["Long Horn","2013","Blue Orange","8","2",[]],["Loony quest","2014","Libellud","8","2-5",[]],["Lords of Xidit","2014","Libellud","14","3-5",[]],["Mafia de Cuba","2015","Lui-même","10","6-12",[]],["Mage Knight","2011","Wizkids\/Intrafin","14","1-4",[]],["Maka Bana","2003","Tilsit","10","2-5",[]],["Marble Monster","2012","Hutch & friends","6","1",[]],["Marrakech","2007","Gigamic","6","2-4",[]],["Mars Attacks","2014","Edge entertainment","14","2",[]],["Massillia","2014","Quined Games","12","2-4",[]],["Medina","2001","Gigamic","10","2-4",[]],["Megawatts","2008","Filosofia","14","2-6",[]],["Megawatts : Les Premières Étincelles","2012","Filosofia","14","2-6",[]],["Mémoire 44","2004","Days of wonder","8","2",["Front Est","Terrain Pack","Carnets de campagne"]],["Mexica","2014","Super Meeple","14","2-4",[]],["Monopoly","1935","Parker","8","2-8",[]],["Munchkin","2004","Steve Jackson Games","10","3-6",[]],["Myrmes","2012","Ystari Games","12","2-4",[]],["Mystérami - Jack L'éventreur","2010","Edge entertainment","8","2-4",[]],["Mysterium","2015","Libellud","10","2-7",[]],["Niagara","2004","Gigamic","8","3-5",[]],["Norenberc","2010","White Goblin Games","12","2-5",["Ext Essen 2010"]],["Olympos","2011","Ystari Games","10","2-5",["Oikoumene"]],["Onirim","2011","Filosofia","8","1-2",[]],["Opération Commando: Pegasus Bridge","2014","Ajax Games","10","2",[]],["Pandémie","2008","Filosofia","10","2-4",[]],["Pandémie contagion","2014","Filosofia","14","2-5",[]],["Pathfinder","2010","Paizo Games","","",[]],["Pathfinder le jeu de carte","2014","Black Book Edition","","",[]],["Peloponnes","2009","Irongames","10","1-5",["Hellas"]],["Pergamon","2011","Iello","10","2-4",[]],["Perplexus","2009","Asmodee","6","1",[]],["Perplexus Epic","2011","Asmodee","6","1",[]],["Perudo","2003","Asmodee","8","2-6",[]],["Pictionary","1993","MB","8","3-16",[]],["Pique Plume","1998","Gigamic","4","2-4",[]],["Pix","2012","Gameworks","8","4-9",[]],["Planet Steam","2014","Edge entertainment","14","2-5",[]],["Puerto Rico","2002","Filosofia","","",[]],["Quarriors","2013","Intrafin","14","2-4",[]],["Quarto!","1991","Gigamic","8","2",[]],["Qui est-ce ?","2005","Hasbro","6","2",[]],["Quoridor","1997","","6","2-4",[]],["Rallyman : Dirt","2011","Rallyman","9","1-4",[]],["Rallyman Asphalte et Neige","2009","Rallyman","9","1-4",[]],["Rasende Roboter","1999","Hans im Glück","10","2-10",[]],["Ringgeister","1993","Lauring Verlag & Queen Games","10","2-4",[]],["Risk Napoléon","2000","Parker","12","2-5",[]],["River Dragons","2012","Matagot","8","2-6",[]],["Roborally","2006","Avalon Hill","12","2-8",[]],["Rockwell","2013","Sit-down","14","2-4",[]],["Rummikub Chiffres","1980","MB","8","2-4",[]],["Russian Railroads","2013","Filosofia","12","2-4",[]],["Saboteur : Les mineurs contre-attaquent !","2011","Gigamic","8","3-10",[]],["Saint Petersburg","2004","Filosofia","13","2-5",[]],["San Juan","2008","Filosofia","10","2-4",[]],["Scrabble","1931","Mattel","10","2-4",[]],["Seasons","2012","Libellud","10","2-4",[]],["Serenissima","2013","Ystari Games","13","2-4",[]],["Sherlock Holmes - Détective Conseil","2011","Ystari Games","12","1+",[]],["Siege","1983","Euro Games","14","2",[]],["Skull & Roses","2011","Lui-même","10","3-6",[]],["Small world","2009","Days of wonder","8","2-5",[]],["Small world underground","2011","Days of wonder","8","2-5",[]],["Smash Up","2012","AEG","12","2-4",[]],["Snowdonia","2013","Indie Board & Game","10","1-5",[]],["Splendor","2014","SpaceCowboy","10","2-4",[]],["Spyrium","2013","Ystari Games","13","2-5",[]],["Star Wars : X-Wing ","2012","Edge entertainment","12","2",["X-Wing","Y-Wing","A-Wing","Faucon Millenium","Tie-Fighter","Tie-Advanced","Tie-Interceptor","Slave I","B-Wing","Tie-Bomber","Navette lambda","HWK-290","As impériaux","Z-95","E-Wing","Tie-Defender","Tie Fantôme","Transport Rebelle","Tantine IV","As rebelles","YT-2400","VT-49","Ennemis publics","Star-Viper","M3-A","IG-2000","Raider Impérial","Hound’s Tooth","Kihraxz","K-Wing","Tie-Punisher"]],["Star Wars : X-Wing Le réveil de la force","2015","Edge entertainment","12","2",[]],["Star Wars: Assaut sur l’Empire","2015","Edge entertainment","12","2-5",[]],["Steam","2009","Edge entertainment","12","3-6",[]],["Sushi Bar","2008","Gigamic","8","3-5",[]],["Sylla","2008","Ystari Games","12","2-4",[]],["Takenoko","2011","Matagot & Bombyx","8","2-4",[]],["Taluva","2006","Hans im Glück","10","2-4",[]],["Targui","2013","Filosofia","12","2",[]],["Tempête sur l'échiquier","1991","Ludodélire","8","2",[]],["Terra Mystica","2013","Filosofia","12","2-5",[]],["The City","2012","Gigamic","10","2-5",[]],["The Island","2012","Asmodee","8","2-4",[]],["The Manhattan Project","2014","Marabunta","14","2-5",[]],["Through the Ages","2008","Iello","12","2-4",[]],["Thunderstone","2011","Edge entertainment","12","2-5",["Légion Doomgate : La colère des éléments","Le Pic du Dragon"]],["Tigre et Euphrate","2009","Matagot","12","2-4",[]],["Tikal","2005","Tilsit","12","2-4",[]],["Time's Up ! - édition verte","2011","Repos Prod","12","4-12",["Recharge 2012 - 2013"]],["Timeline","2010","Asmodee","8","2-8",["Invention","Découvertes","Evénements"]],["Titanic","2008","Smart Games","8","1",[]],["Tournay","2011","Pearl Games","12","2-4",[]],["Trifouilli","2013","Gigamic","5","2-4",[]],["Triominos de Luxe","1990","Goliath","6","1-4",[]],["Twilight Struggle","2005","GMT games","14","2",[]],["Twin It !","2011","Cocktail Games & Ystari Games","5","1",[]],["Tzolk'in","2012","Iello","13","2-4",[]],["Union Pacific","1998","Amigo","10","2-6",[]],["Uno","1992","Mattel","7","2-10",[]],["Vanuatu","2011","Krok Nik Douil","12","2-5",[]],["Vendredi","2011","Filosofia","10","1",[]],["Vinci","1999","Jeux Descartes","14","2-6",[]],["Yggdrasil","2011","Ludonaute","13","1-6",[]],["Yokai No Mori","2013","Ferti","7","2",[]],["Ys","2008","Ystari Games","12","2-4",["Ys+"]],["Yspahan","2006","Ystari Games","8","2-4",[]],["Yunnan","2012","Argentum Verlag","12","2-5",[]],["Zargo's Lords","1981","International team","15","2-4",[]],["Zombicide","2012","Guillotine Games","13","1-6",["Prison Outbreak","Companion Dogs","Zombies Dogs","Compendium #1"]],["Zombie 15’","2014","Iello","14","2-4",[]],["Zombie Dice","2012","Steve Jackson Games","14","2-8",[]]]

for d in data:
        cur.execute("""INSERT INTO Jeu VALUES (,d[0],d[1],d[2],d[3],d[4])""")

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
