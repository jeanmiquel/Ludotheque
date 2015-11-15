# -*- coding: utf-8 -*-
import EnsUtilisateurs
class Connexion:
        def __init__(self,username,password):
                self.username = username
                self.password = password


        def est_valide(self):
                if EnsUtilisateurs.has_username(self.username):
                        User=EnsUtilisateurs.get_user(username=self.username) # On récupère l'utilisateur
                        return EnsUtilisateurs.is_password(self.password,User)
                else:
                        return False
                        
        def creer_session(self):
                global session
                if self.est_valide():
                        User=EnsUtilisateurs.get_user(username=self.username) # ID Associe à username fourni
                        session=Session(User)
                else:
                        print "Oops !"
