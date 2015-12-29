import BDD
import tkinter as tk
import Adherent as ad
import datetime

#ajout d'un adherent dans la base de donnée pour le test de la connexion
ad.Adherent.ajoutAdherent("nom", "prenom", datetime.datetime.now(), "adresse", 34190, "ville", "numeroTel",  "pseudo", "adresseMail")
ad.Adherent.getAllAdherent()

#A lier avec la suite ....
def verificationConnexion():
    idAd = ad.Adherent.getIdByPseudo(pseudo.get())
    if idAd == None:
        print("Mauvais pseudo")
    else:
        if ad.Adherent.compareMDP(idAd,mdp.get()) == False:
            print("Mauvais MDP")
        else:
            print("Connexion reussi")

#creation de la fênetre principle
fenetre = tk.Tk()
fenetre.title('Ludotheque')

framePrincip = tk.Frame(fenetre)
framePrincip.pack(padx = 30, pady = 30)

labelTitre = tk.Label(framePrincip, text = "Connexion")
labelTitre.pack(padx = 50, pady = 10)

#pseudo
framePseudo = tk.Frame(framePrincip)
framePseudo.pack(pady = 20)

labPseudo = tk.Label(framePseudo, text = "Pseudo")
labPseudo.pack(side = "left", padx = 5, pady = 5)

#Saisie du pseudo
pseudo = tk.StringVar()
champPseudo = tk.Entry(framePseudo, textvariable = pseudo, bg ='bisque', fg='maroon')
champPseudo.focus_set()
champPseudo.pack(side = "left", padx = 5, pady = 5)


#MDP
frameMDP = tk.Frame(framePrincip)
frameMDP.pack(pady = 20)

labMdp = tk.Label(frameMDP, text = "Mot de passe ")
labMdp.pack(side = "left", padx = 5, pady = 5)

#Saisie du MDP
mdp = tk.StringVar()
champMdp = tk.Entry(frameMDP, textvariable = mdp, show='*', bg ='bisque', fg='maroon')
champMdp.pack(side = "left", padx = 5, pady = 5)


#Bouton Valider
Bouton = tk.Button(framePrincip, text ='Valider', command = verificationConnexion)
Bouton.pack(side = "right", padx = 5, pady = 5)
