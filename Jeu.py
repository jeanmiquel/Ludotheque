class Jeu:

    def __init__(self,id_Jeu=None,Nom_Jeu="",Annee=None,Editeur="",Age=None,NombreJoueurs="",Description=""):
        self.id_Jeu = id_Jeu
        self.Nom_Jeu = Nom_Jeu
        self.Annee = Annee
        self.Editeur = Editeur
        self.Age = Age
        self.NombreJoueurs = NombreJoueurs
        self.Description = Description


###### GETTERS ########
    def get_Nom_Jeu(self):
        return self.Nom_jeu

    def get_Age(self):
        return self.Age

    def get_Description(self):
        return self.Description

    def get_id_Jeu(self):
        return self.Jeu_id

    def get_NombreJoueurs(self):
        return self.NombreJoueurs

    def get_Editeur(self):
        return self.Editeur

    def get_Annee(self):
        return self.Annee


###### SETTERS ########
    def set_Nom_Jeu(self,Nom_Jeu):
        self.Nom_jeu = Nom_jeu
        
    def set_Age(self,Age):
        self.Age = Age
        
    def set_Description(self,Description):
        self.Description = Description
        
    def set_NombreJoueurs(self,NombreJoueurs):
        self.NombreJoueurs = NombreJoueurs
        
    def set_Editeur(self,Editeur):
        self.Editeur = Editeur
        
    def set_Annee(self,Annee):
        self.Annee = Annee
