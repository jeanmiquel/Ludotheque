#-*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *
from datetime import *
import datetime
from functools import partial
from Jeu import Jeu
from Adherent import Adherent
from Extension import Extension
from Emprunt import Emprunt
from Reservation import Reservation


infos = [1,True, Tk()]

#FORMULAIRE DE JEU

def formulaireJeu(idJeu = -1): #Par defaut, -1 = creation
    """Prend l'id d'un jeu pour le modifier, ou -1 pour en creer un nouveau"""
    FJ = Frame(infos[2])
    #FJ.wm_attributes("-topmost" , -1) #Mets la fenetre au premier plan des son apparition.
    idJ = IntVar()
    idJ.set(idJeu)
    Creation = BooleanVar()            #Les variables declaree comme ceci semble etre utilisable pour les fonctions imbrique de Tkinter
    Creation.set(False)
    if idJ.get() < 0 : #Cas de creation du jeu, valeur par defaut
        nomJ="Nom du jeu"
        anneeJ=1960
        ageJ=0
        nbJoueurJ="00-00"
        quantiteJ=0
        auteurJ="Auteur du jeu"
        illustrateurJ="Illustrateur du jeu"
        editeurJ="Editeur du jeu"
        estEmpruntableJ=False
        synopsisJ="Description sommaire du jeu."
        Creation.set(True)
    else : #Jeu existant, recuperation, des infos
        nomJ=Jeu.getNomJeu(idJ.get())
        anneeJ=Jeu.getAnneeJeu(idJ.get())
        ageJ=Jeu.getAgeJeu(idJ.get())
        nbJoueurJ=Jeu.getNbJoueurJeu(idJ.get())
        quantiteJ=Jeu.getQuantiteJeu(idJ.get())
        auteurJ=Jeu.getAuteurJeu(idJ.get())
        illustrateurJ=Jeu.getIllustrateurJeu(idJ.get())
        editeurJ=Jeu.getEditeurJeu(idJ.get())
        estEmpruntableJ=Jeu.estEmpruntable(idJ.get())
        synopsisJ=Jeu.getSynopsisJeu(idJ.get())

    def submit(): #Fonction de confirmation DANS la fonction de fenetre.
        if askyesno("Confirmation", "Enregister le jeu ?"):
            FJ.quit()
            if Creation.get():
                idJ.set(Jeu.ajoutJeu(nomJeu.get(),anneeJeu.get(),editeurJeu.get()))
            Jeu.setNomJeu(idJ.get(),nomJeu.get())
            Jeu.setAnneeJeu(idJ.get(),anneeJeu.get())
            Jeu.setAgeJeu(idJ.get(),ageJeu.
                          get())
            Jeu.setNbJoueurJeu(idJ.get(),nbJoueurJeu.get())
            Jeu.setQuantiteJeu(idJ.get(),quantiteJeu.get())
            Jeu.setAuteurJeu(idJ.get(),auteurJeu.get())
            Jeu.setIllustrateurJeu(idJ.get(),illustrateurJeu.get())
            Jeu.setEditeurJeu(idJ.get(),editeurJeu.get())
            Jeu.setEmpruntable(idJ.get(),Empbool.get())
            Jeu.setSynopsisJeu(idJ.get(),synopsisJeu.get())
            return FJ.destroy() #Ferme apres avoir enregistre.
        else : return 

    def cancel(): #Ferme la fenetre
        if askyesno("Quitter", "Annuler le formulaire ?"):
            FJ.quit() #Ferme la fenetre
            return FJ.destroy() #N'enregistre rien
        else : return
    T1 = LabelFrame(FJ, text="Formulaire de jeu :")
    NJ = Label(FJ, text="Nom du jeu :")
    AnJ = Label(FJ, text="AnnÃƒÂ©e de sortie du jeu :")
    AgJ = Label(FJ, text="Ages du public du jeu :")
    NbJ = Label(FJ, text="Nombre de joueur pour ce jeu($$-$$) :")
    QJ = Label(FJ, text="Nombre d'exemplaire total du jeu :")
    AJ = Label(FJ, text="Auteur du jeu :")
    IJ = Label(FJ, text="Illustrateur du jeu :")
    EJ = Label(FJ, text="Editeur du jeu :")
    Emp = Label(FJ, text="Ce jeu peut-etre EmpruntÃƒÂ© :")
    SJ =Label(FJ, text="Description du jeu (200caractÃƒÂ¨res) :")
    AddJ = Label(FJ, text="Ajouter le jeu :")
    #Titre
    T1.pack()
    #Nom du jeu (champs a remplir)
    NJ.pack()
    nomJeu = StringVar()
    nomJeu.set(nomJ)
    NJI = Entry(FJ,textvariable=nomJeu,width=40)
    NJI.pack()
    #Annee Jeu (graduation)
    AnJ.pack()
    anneeJeu = IntVar()
    anneeJeu.set(anneeJ)
    AnJI = Spinbox(FJ, from_=1960, to = date.today().year, textvariable=anneeJeu)
    AnJI.pack()
    #Age joueurs(Champs a remplir)
    AgJ.pack()
    ageJeu=IntVar()
    ageJeu.set(ageJ)
    AgJI = Spinbox(FJ, from_=0, to = 20, textvariable=ageJeu)
    AgJI.pack()
    #Nombre de joueurs (graduation)
    NbJ.pack()
    nbJoueurJeu=StringVar()
    nbJoueurJeu.set(nbJoueurJ)
    NbJI = Entry(FJ, textvariable=nbJoueurJeu, width=45)
    NbJI.pack()
    #Quantite d'exemplaire du jeu (gradutation)
    QJ.pack()
    quantiteJeu = IntVar()
    quantiteJeu.set(quantiteJ)
    QJI = Spinbox(FJ, from_=0, to=999, textvariable=quantiteJeu)
    QJI.pack()
    #Auteur du jeu (champs a remplir)
    AJ.pack()
    auteurJeu=StringVar()
    auteurJeu.set(auteurJ)
    AJI = Entry(FJ, textvariable=auteurJeu, width = 45)
    AJI.pack()
    #Illustrateur du jeu (champs a remplir)
    IJ.pack()
    illustrateurJeu=StringVar()
    illustrateurJeu.set(illustrateurJ)
    IJI = Entry(FJ, textvariable=illustrateurJeu, width = 45)
    IJI.pack()
    #Editeur du jeu (champs a remplir)
    EJ.pack()
    editeurJeu=StringVar()
    editeurJeu.set(editeurJ)
    EJI = Entry(FJ, textvariable=editeurJeu, width = 45)
    EJI.pack()
    #Empruntable ou non ? (case a cocher)
    Emp.pack()
    Empbool = BooleanVar()
    Empbool.set(estEmpruntableJ)
    EmpI = Checkbutton(FJ, text="Est-il empruntable?", variable = Empbool)
    EmpI.pack()
    #Synospis du jeu (Champs a remplir)
    SJ.pack()
    synopsisJeu = StringVar()
    synopsisJeu.set(synopsisJ)
    SJI = Entry(FJ, textvariable=synopsisJeu, width = 45)
    SJI.pack()
    #Fin : Confirmation de l'ajout/modification du jeu, appel de la fonction submit (sans parentheses)
    AddJ.pack()
    AddJI = Button(FJ, text="Confirmer", command = submit)
    AddJI.pack()
    #Fin : Annulation.(marche pas encore)
    Cancel = Button(FJ, text="Annuler", command = cancel)
    Cancel.pack()
    #Lancement de la fenetre
    FJ.pack()
    infos[2].mainloop()
    return catalogue(Jeu.getAllJeu())


def formulaireExt(idExt = -1, idJeu=0): #Par defaut, idExt =-1 => creation
    """Prend l'id d'une extension pour la modifier, ou -1 pour en creer une nouvelle"""
    
    FE = Frame(infos[2])
    infos[2].title("Formulaire d'extension")
    #FE.wm_attributes("-topmost" , -1) #Mets la fenetre au premier plan des son apparition.
    idE = IntVar()
    idE.set(idExt)
    Creation = BooleanVar()            #Les variables declaree comme ceci semble etre utilisable pour les fonctions imbrique de Tkinter
    Creation.set(False)
    if idE.get() >= 0:
        idJeu = Extension.getIdJeu(idExt)
    idJ = IntVar()
    idJ.set(idJeu)
    if idE.get() < 0 : #Cas de creation du Ext, valeur par defaut.
        NomJeuE = Jeu.getNomJeu(idJeu)
        nomE="Nom de l'extension"
        quantiteE=0
        Creation.set(True)
    else : #Extension existant, recuperation, des infos        
        NomJeuE = Jeu.getNomJeu(idJeu)
        nomE=Extension.getNomExtension(idE.get())
        quantiteE=Extension.getNbreTotalExtension(idE.get())
    
    def submit(): #Fonction de confirmation DANS la fonction de fenetre.
        if askyesno("Confirmation", "Enregister L'extension ?"):
            FE.quit()
            if Creation.get():
                Extension.ajoutExtension(idJ.get(),NEI.get(),QEI.get())
            else :
                Extension.setNomExtension(idE.get(),nomExt.get())
                Extension.setNbreTotalExtension(idE.get(),quantiteExt.get())
            return FE.destroy() #Ferme apres avoir enregistre.
        else : return

    def cancel(): #Ferme la fenetre
        if askyesno("Quitter", "Annuler le formulaire ?"):
            FE.quit() #Ferme la fenetre
            return FE.destroy() #N'enregistre rien
        else : return
        
    T1 = LabelFrame(FE, text="Formulaire de l'extension :")
    NJE = Label(FE, text="Nom du jeu de l'extension :")
    NE = Label(FE, text="Nom de l'extension :")
    QE = Label(FE, text="Nombre d'exemplaire total de l'extension :")
    AddE = Label(FE, text="Ajouter l'extension :")
    #Titre
    T1.pack()
    #Nom du jeu (recupere l'id du jeu dans la liste)
    NJE.pack()
    NomJeu = Label(FE, text =Jeu.getNomJeu(idJeu))
    NomJeu.pack() 
    #Nom de l'extension (champs a remplir)
    NE.pack()
    nomExt = StringVar()
    nomExt.set(nomE)
    NEI = Entry(FE,textvariable=nomExt,width=40)
    NEI.pack()
    #Quantite d'exemplaire de l'extension (gradutation)
    QE.pack()
    quantiteExt = IntVar()
    quantiteExt.set(quantiteE)
    QEI = Spinbox(FE, from_=0, to=999, textvariable=quantiteExt)
    QEI.pack()
    #Fin : Confirmation de l'ajout/modification du extension, appel de la fonction submit (sans parentheses)
    AddE.pack()
    AddEI = Button(FE, text="Confirmer", command = submit)
    AddEI.pack()
    #Fin : Annulation.(marche pas encore)
    Cancel = Button(FE, text="Annuler", command = cancel)
    Cancel.pack()
    #Lancement de la fenetre
    FE.pack()
    infos[2].mainloop()
    return afficheExtensions(idJeu)





#INTERFACE DE CONNEXION


def connexion():
    def verification():
        infos[0] = Adherent.getIdByPseudo(pseudo.get())
        if (infos[0] <> None):
            if (mdp.get()==Adherent.getMotDePasse(infos[0])):
                infos[1]=(Adherent.getEstAdministrateur(infos[0])<>None and Adherent.getEstAdministrateur(infos[0]))
                fconnexion.destroy()
                menu()
            else:
                showwarning('Mot de passe incorrect','Mot de passe incorrect.\nVeuillez recommencer !')
                mdp.set('')
        else:
            showwarning('Pseudo inexistant','Pseudo inexistant.\nVeuillez recommencer !')
            mdp.set('')
            pseudo.set('')
        
    fconnexion =  Frame(infos[2])
    infos[2].title("Connexion a  la Ludotheque")
    #fenetre aparaisse au premier plan
    infos[2].wm_attributes("-topmost", 1)
    
    p = PanedWindow(fconnexion, orient = HORIZONTAL, height = 20, width = 300)
    p.grid(row=1)
    p.add(Label(p, text="Pseudo : ", anchor=CENTER, width= 20))
    pseudo = StringVar()
    p.add(Entry(p, width = 20, textvariable = pseudo))
    

    pd = PanedWindow(fconnexion, orient = HORIZONTAL, height = 20, width = 300)
    pd.grid(row=2)
    pd.add(Label(pd,text="Mot de passe : ", anchor = CENTER, width= 20))
    mdp = StringVar()
    pd.add(Entry(pd, width=20, show="*", textvariable = mdp ))
    

    Button(fconnexion, text ="Se connecter", command = verification).grid(row=3)

    fconnexion.pack()
    infos[2].mainloop()

def rien():
    return 










#MENU PRINCIPAL
        
def menu(): #numIdAdherent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fmenu.after(1000,maj)

    def LancePanneauAdmin():
        fmenu.destroy()
        return panneauAdmin() 
        
    def LanceCatalogue():
        fmenu.destroy()
        return catalogue(Jeu.getAllJeu())

    def LanceProfil():
        fmenu.destroy()
        return formulaireAdherent(infos[0])

    def LanceEmprunt():
        fmenu.destroy()
        return catalogueEmprunt(Adherent.getAllEmpruntAdherent(infos[0]))

    def LancerReserver():
        fmenu.destroy()
        return catalogueReservation(Adherent.getAllReservationAdherent(infos[0]))

    
    fmenu = Frame(infos[2])
    infos[2].title("Menu principal")
    p = PanedWindow(fmenu,orient=HORIZONTAL, height=100, width=600)
    p.grid(row=1)
    
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=20))
    maj()
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(infos[0]), bg="white", anchor=CENTER, width=20))
    if (infos[1]):
        p.add(Button(p, text="Panneau d'administration", bg="orange", activebackground="orange", borderwidth=10, width=20, command=LancePanneauAdmin ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = infos[2].destroy ))
    

    pd = PanedWindow(fmenu,orient=HORIZONTAL, height=350, width=600)
    pd.grid(row=2)
    pd.add(Button(pd, text="Profil", width=38, command = LanceProfil, bg="yellow", activebackground="yellow", borderwidth=10))
    pd.add(Button(pd, text="Catalogue", width=38, command = LanceCatalogue, bg="red", activebackground="red", borderwidth=10))

    
    pt = PanedWindow(fmenu,orient=HORIZONTAL, height=350, width=600)
    pt.grid(row=3)
    pt.add(Button(pt, text="Mes emprunts", command = LanceEmprunt, bg="green", width=38,activebackground="green", borderwidth=10))
    pt.add(Button(pt, text="Réservation", command = LancerReserver,bg="cyan", width=38,activebackground="cyan", borderwidth=10))
    
    fmenu.pack()
    infos[2].mainloop()

    










#PANNEAU D'ADMINISTRATION


def panneauAdmin(): #numIdAdherent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fpanneauadmin.after(1000,maj)

    def retourMenu():
        fpanneauadmin.destroy()
        return menu()

    def LanceCatalogue():
        fpanneauadmin.destroy()
        return catalogue(Jeu.getAllJeu())

    def LanceEmprunt():
        fpanneauadmin.destroy()
        return catalogueEmprunt(Emprunt.getAllEmprunts())

    def LanceReservation():
        fpanneauadmin.destroy()
        return catalogueReservation(Reservation.getAllReservations())


    def LanceAdherent():
        fpanneauadmin.destroy()
        return catalogueAdherents(Adherent.getAllAdherent())
    

    if (not(infos[1])):
        return menu(numAdh)
    
    fpanneauadmin = Frame(infos[2])
    infos[2].title("Panneau d'aministration")
    
    p = PanedWindow(fpanneauadmin,orient=HORIZONTAL, height=100, width=600)
    p.grid(row=1)
    
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=20))
    maj()
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(infos[0]), bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour menu", bg="orange", activebackground="orange", borderwidth=10, width=20, command= retourMenu))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = infos[2].destroy ))
    
    pd = PanedWindow(fpanneauadmin,orient=HORIZONTAL, height=350, width=600)
    pd.grid(row=2)
    pd.add(Button(pd, text="Gestion des Adherents", width=38, command = LanceAdherent, bg="yellow", activebackground="yellow", borderwidth=10))
    pd.add(Button(pd, text="Gestion des Jeux", width=38, command = LanceCatalogue, bg="red", activebackground="red", borderwidth=10))


    pt = PanedWindow(fpanneauadmin,orient=HORIZONTAL, height=350, width=600)
    pt.grid(row=3)
    pt.add(Button(pt, text="Gestion des Emprunts", command = LanceEmprunt, bg="green", width=38,activebackground="green", borderwidth=10))
    pt.add(Button(pt, text="Gestion des Reservations", command = LanceReservation,bg="cyan", width=38,activebackground="cyan", borderwidth=10))

    fpanneauadmin.pack()
    infos[2].mainloop()




#CATALOGUE DES JEUX


def catalogue(Jeux=Jeu.getAllJeu()): #idAdherent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fcatalogue.after(1000,maj)

    def retourMenu():
        fcatalogue.destroy()
        return menu()

    def afficheFicheJeu(i):
        fcatalogue.destroy()
        return ficheJeu(i)
    
    def lancerEmprunt(i):
        fcatalogue.destroy()
        return formulaireEmprunt(i)

    def lancerReserv(i):
        fcatalogue.destroy()
        return reserver(i)

    def lanceCatalogue():
        r = entryRecherche.get()
        fcatalogue.destroy()
        return catalogue(Jeu.getJeuByNom(r))

    def lancerExtension(i):
        fcatalogue.destroy()
        return afficheExtensions(i)

    def lanceFormulaireExt(j, i):
        fcatalogue.destroy()
        return formulaireExt(j, i)

    def lanceFormulaireJeu(i):
        fcatalogue.destroy()
        return formulaireJeu(i)

    def supp(i):
        if askyesno("Confirmation", "etes-vous sur de vouloir supprimer ce jeu ainsi que toutes les données associées (emprunts, réservations, extensions) ?"):
            Jeu.supprimerJeu(i)
            fcatalogue.destroy()
            return catalogue(Jeu.getAllJeu())
        else:
            return

    def afficheJeu(n, Jeux, k=0):
        n[0]=n[0]+k
        r = n[2]-n[1]
        if (r>20): r=20
        if (n[0]<n[1]):
            n[0]=n[1]
        if (n[0]+r>n[2]):
            n[0]=n[2]-r
        j=3
        
        for i in range(n[0],n[0]+r):
            Label(fcatalogue, text=str(Jeux[i][1]), bg="orange", width = 25).grid(row=j, column=1)
            Label(fcatalogue, text=str(Jeux[i][2]), bg="orange", width = 10).grid(row=j, column=2)
            Label(fcatalogue, text=str(Jeux[i][3]), bg="orange", width = 10).grid(row=j, column=3)
            Label(fcatalogue, text=str(Jeux[i][4]), bg="orange", width = 10).grid(row=j, column=4)
            Label(fcatalogue, text=str(Jeux[i][5]), bg="orange", width = 15).grid(row=j, column=5)
            Label(fcatalogue, text=str(Jeux[i][6]), bg="orange", width = 15).grid(row=j, column=6)
            Label(fcatalogue, text=str(Jeux[i][7]), bg="orange", width = 15).grid(row=j, column=7)
            Label(fcatalogue, text=str(Jeux[i][8]), bg="orange", width = 15).grid(row=j, column=8)
            if (infos[1]):
                Button(fcatalogue, text="Modifier", command = partial(lanceFormulaireJeu, Jeux[i][0]),bg="blue", width=13,activebackground="blue").grid(row=j, column=9) #partial(formulaireJeu,Jeux[i][0])
                Button(fcatalogue, text="Creer extension", command = partial(lanceFormulaireExt, -1, Jeux[i][0]),bg="cyan", width=13,activebackground="cyan").grid(row=j, column=14)
            else:
                Button(fcatalogue, text="Detail", command = partial(afficheFicheJeu,Jeux[i][0]) ,bg="blue", width=13,activebackground="blue").grid(row=j, column=9)
                
            if (Jeu.aDesExtensions(Jeux[i][0])):
                Button(fcatalogue, text="Extensions", command = partial(lancerExtension, Jeux[i][0]),bg="red", width=13,activebackground="red").grid(row=j, column=10)
            else:
                Label(fcatalogue, bg="lightgrey", width = 14, height=1).grid(row=j, column=10)
            Button(fcatalogue, text="Emprunt", command = partial(lancerEmprunt, Jeux[i][0]),bg="green", width=13,activebackground="green").grid(row=j, column=11)
            Button(fcatalogue, text="Reserv", command = partial(lancerReserv, Jeux[i][0]),bg="red", width=13,activebackground="red").grid(row=j, column=12)
            if (infos[1]):
                Button(fcatalogue, text="Supprimer", command = partial(supp, Jeux[i][0]),bg="yellow", width=13,activebackground="red").grid(row=j, column=13)
            j=j+1

    
    fcatalogue = Frame(infos[2])
    infos[2].title("Les jeux de la ludotheque")
    #fcatalogue.grid_columnconfigure(0,weight=1)
    #fcatalogue.grid_rowconfigure(20,weight=21)


    
    p = PanedWindow(fcatalogue, orient = HORIZONTAL, height=100, width=1000)
    p.grid(row=1, column=1, columnspan=11)
     
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=30))
    maj()

    rech=StringVar()
    rech.set("Faites une recherche ici !")

    entryRecherche = Entry(p, textvariable=rech, width = 30)
    p.add(entryRecherche)
    p.add(Button(p, text="Recherchez !", bg="orange", activebackground="orange", borderwidth=10, width=10, command= lanceCatalogue))

    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(infos[0]), bg="white", anchor=CENTER, width=10))
    if (infos[1]):
        p.add(Button(p, text="Ajouter un jeu", bg="cyan", activebackground="cyan", borderwidth=10, width=10, command= partial(lanceFormulaireJeu,-1)))
    p.add(Button(p, text="Retour au menu principal", bg="orange", activebackground="orange", borderwidth=10, width=10, command= retourMenu ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = infos[2].destroy ))





    Label(fcatalogue, text="Nom", bg="green", width = 23).grid(row=2, column=1)
    Label(fcatalogue, text="Annee", bg="green", width = 8).grid(row=2, column=2)
    Label(fcatalogue, text="Age Min.", bg="green", width = 8).grid(row=2, column=3)
    Label(fcatalogue, text="Nb Joueur", bg="green", width = 8).grid(row=2, column=4)
    Label(fcatalogue, text="Disponibilite", bg="green", width = 13).grid(row=2, column=5)
    Label(fcatalogue, text="Auteur", bg="green", width = 13).grid(row=2, column=6)
    Label(fcatalogue, text="Illustrateur", bg="green", width = 15).grid(row=2, column=7)
    Label(fcatalogue, text="Editeur", bg="green", width = 13).grid(row=2, column=8)
    if (infos[1]):
        Label(fcatalogue, text="Que faire ?", bg="green", width = 73).grid(row=2, column=9, columnspan=6)
    else:
        Label(fcatalogue, text="Que faire ?", bg="green", width = 73).grid(row=2, column=9, columnspan=4)

    numJeu=[0,0,len(Jeux)]
    flecheH = Button(fcatalogue, text="^", command = partial(afficheJeu, numJeu, Jeux, -20), bg="blue", width=5,activebackground="blue").grid(row=3, column=15)
    flecheB = Button(fcatalogue, text="v", command = partial(afficheJeu, numJeu, Jeux, 20), bg="blue", width=5,activebackground="blue").grid(row=22, column=15)
    afficheJeu(numJeu, Jeux)
    
        
    fcatalogue.pack()
    infos[2].mainloop()




#EXTENSIONS A PARTIR DU BOUTON "EXTENSION" SUR JEU
def afficheExtensions(idJeu=-1): #idJeu = -1 <==> affiche toutes les extensions
    
    def retourCatalogue():
        fextension.destroy()
        return catalogue()

    def lancerEmprunt(i,mode):
        fextension.destroy()
        return formulaireEmprunt(i,mode)

    def lancerReserv(i,mode):
        fextension.destroy()
        return reserver(i,mode)

    def LanceFormulaireExt(i, j=0):
        fextension.destroy()
        return formulaireExt(i, j)

    def voirFiche():
        fextension.destroy()
        return ficheJeu(idJeu)

    def supp(i):
        if askyesno("Confirmation", "Etes-vous sur de vouloir supprimer cette Extension ainsi que toutes les données associées (emprunts, réservations) ?"):
            Extension.supprimerExtension(i)
            fextension.destroy()
            return afficheExtensions(idJeu)
        else:
            return
    
    fextension=Frame(infos[2])
    infos[2].title("Extension(s) du jeu ")
    fextension.grid_columnconfigure(0,weight=1)
    fextension.grid_rowconfigure(20,weight=21)

    p = PanedWindow(fextension, orient = HORIZONTAL, height=100, width=600)
    p.grid(row=1, column=1, columnspan=4)
    p.add(Label(p, text="Bonjour " + Adherent.getPseudo(infos[0]), bg="white", anchor=CENTER, width=20))
    if (idJeu <> -1):
        p.add(Button(p, text="Voir la fiche du Jeu", bg="orange", activebackground="orange", borderwidth=10, width=20, command=voirFiche))
    p.add(Button(p, text="Retour au catalogue", bg="orange", activebackground="orange", borderwidth=10, width=20, command=retourCatalogue))
    if (infos[1]):
        p.add(Button(p, text="Ajouter Extension", bg="cyan", activebackground="cyan", borderwidth=10, width=20, command= partial(LanceFormulaireExt, -1, idJeu)))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = infos[2].destroy ))
    
    if (Jeu.aDesExtensions(idJeu)==False and idJeu <> -1):
        Label(fextension, text="Pas d'extension", bg="white", width=25).grid(row=2)
    else:
        Label(fextension, text="Nom Extension", bg="red", width=30).grid(row=2, column=2) #affiche "Nom Extension" au dessus des noms
        Label(fextension, text="Nom Jeu", bg="red", width=30).grid(row=2, column=1)
        if (idJeu == -1):
            j = Extension.getAllExtension()
        else:
            j = Jeu.getExtensions(idJeu)
        k=3
        for i in j:
            Label(fextension, text=str(Extension.getNomExtension(i[0])), bg="white", width=25).grid(row=k, column=2)
            Label(fextension, text=str(Jeu.getNomJeu(Extension.getIdJeu(i[0]))), bg="white", width=25).grid(row=k, column=1)
            Button(fextension, text="Emprunt avec Jeu", command = partial(lancerEmprunt, i[0],1),bg="green", width=13,activebackground="green").grid(row=k, column=4)
            Button(fextension, text="Emprunt sans Jeu", command = partial(lancerEmprunt, i[0],0),bg="green", width=13,activebackground="green").grid(row=k, column=5)
            Button(fextension, text="Reserv avec Jeu", command = partial(lancerReserv, i[0],1),bg="red", width=13,activebackground="red").grid(row=k, column=6)
            Button(fextension, text="Reserv sans Jeu", command = partial(lancerReserv, i[0],0),bg="red", width=13,activebackground="red").grid(row=k, column=7)
            Label(fextension, text="Quantité disponible", bg="red", width=30).grid(row=2, column=3)
            Label(fextension, text=Extension.getNbreTotalExtension(i[0]), bg="white", width=25).grid(row=k,column=3)
            if (infos[1]):
                Button(fextension, text="Modifier", command = partial(LanceFormulaireExt, i[0]), bg="yellow", width=13, activebackground="yellow").grid(row=k, column=8)  
                Button(fextension, text="Supprimer", command= partial(supp, i[0]), bg="yellow", width=13, activebackground="yellow").grid(row=k, column=9)
            k=k+1
            
    fextension.pack()
    infos[2].mainloop()









#AFFICHAGE JEU COTE UTILISATEUR

def ficheJeu(numJeu): #idAdherent + idJeu
    
    def retourCatalogue():
        fficheJeu.destroy()
        return catalogue()

    def lancerEmprunt(i):
        fficheJeu.destroy()
        return formulaireEmprunt(i)

    def lancerReserv(i):
        fficheJeu.destroy()
        return reserver(i)

    def lancerExtension(i):
        fficheJeu.destroy()
        return afficheExtensions(i)

    def lancerExtension(i):
        fficheJeu.destroy()
        return afficheExtensions(i)

    def lanceFormulaireExt(j, i):
        fficheJeu.destroy()
        return formulaireExt(j, i)

    def lanceFormulaireJeu(i):
        fficheJeu.destroy()
        return formulaireJeu(i)
    
    fficheJeu = Frame(infos[2])
    infos[2].title(str(Jeu.getNomJeu(numJeu)))
    fficheJeu.grid_columnconfigure(0,weight=1)
    fficheJeu.grid_rowconfigure(20,weight=21)

    p = PanedWindow(fficheJeu, orient = HORIZONTAL, height=100, width=600)
    p.grid(row=1, column=1, columnspan=3)
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(infos[0]), bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour au catalogue", bg="orange", activebackground="orange", borderwidth=10, width=20, command= retourCatalogue ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = infos[2].destroy ))

   
    Label(fficheJeu, text=str(Jeu.getNomJeu(numJeu)), bg="orange", width = 50, height=5, anchor = CENTER).grid(row=2, column=1, columnspan=3)

    Label(fficheJeu, text="AnnÃƒÂ©e de parution : ", bg="green", width = 15).grid(row=3, column=1)
    Label(fficheJeu, text=str(Jeu.getAnneeJeu(numJeu)), bg="orange", width = 15).grid(row=3, column=2)

    Label(fficheJeu, text="Age Mininimum : ", bg="green", width = 15).grid(row=4, column=1)
    Label(fficheJeu, text=str(Jeu.getAgeJeu(numJeu)), bg="orange", width = 15).grid(row=4, column=2)

    try:
        photo = PhotoImage(file="imageJeu/" + str(numJeu) + ".gif")
        canvas = Canvas(fficheJeu,width=350, height=200)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.grid(row=3, rowspan=3, column=3)
    except:
        print ""

    Label(fficheJeu, text="Nombre de Joueurs : ", bg="green", width = 15).grid(row=5, column=1)
    Label(fficheJeu, text=str(Jeu.getNbJoueurJeu(numJeu)), bg="orange", width = 15).grid(row=5, column=2)

    Label(fficheJeu, text="Quantitee en stock : ", bg="green", width = 15).grid(row=6, column=1)
    Label(fficheJeu, text=str(Jeu.getQuantiteJeu(numJeu)), bg="orange", width = 15).grid(row=6, column=2)
    
    Label(fficheJeu, text="Auteur : ", bg="green", width = 15).grid(row=7, column=1)
    Label(fficheJeu, text=str(Jeu.getAuteurJeu(numJeu)), bg="orange", width = 15).grid(row=7, column=2)

    Label(fficheJeu, text="Illustrateur : ", bg="green", width = 15).grid(row=8, column=1)
    Label(fficheJeu, text=str(Jeu.getIllustrateurJeu(numJeu)), bg="orange", width = 15).grid(row=8, column=2)
    
    Label(fficheJeu, text="Editeur : ", bg="green", width = 15).grid(row=9, column=1)
    Label(fficheJeu, text=str(Jeu.getEditeurJeu(numJeu)), bg="orange", width = 15).grid(row=9, column=2)

    Label(fficheJeu, text="Synopsis : ", bg="green", width = 15).grid(row=10, column=1)
    Label(fficheJeu, text=str(Jeu.getSynopsisJeu(numJeu)), bg="orange", width = 15).grid(row=10, column=2)

    r = 5
    if (infos[1]):
        Button(fficheJeu, text="Modifier", command = partial(lanceFormulaireJeu, numJeu),bg="blue", width=13,activebackground="blue").grid(row=r, column=3) #partial(formulaireJeu,Jeux[i][0])
        Button(fficheJeu, text="Creer extension", command = partial(lanceFormulaireExt, -1, numJeu),bg="cyan", width=13,activebackground="cyan").grid(row=r+1, column=3)
        r=r+2

    if (Jeu.aDesExtensions(numJeu)):
        Button(fficheJeu, text="Extensions", command = partial(lancerExtension, numJeu),bg="red", width=13,activebackground="red").grid(row=r, column=3)
        r=r+1
    
    Button(fficheJeu, text="Emprunt", command = partial(lancerEmprunt, numJeu),bg="green", width=13,activebackground="green").grid(row=r, column=3)
    Button(fficheJeu, text="Reserv", command = partial(lancerReserv, numJeu),bg="red", width=13,activebackground="red").grid(row=r+1, column=3)
    r=r+2
    if (infos[1]):
        Button(fficheJeu, text="Supprimer", command = rien,bg="yellow", width=13,activebackground="red").grid(row=r, column=3)

    fficheJeu.pack()
    infos[2].mainloop()













#INTERFACE D'EMPRUNT D'UN JEU

def formulaireEmprunt(numJeu, mode=-1): #idJeu/extension + idAdherent + boolÃƒÂ©en + boolÃƒÂ©en
    
    def CallBackEmprunt(numJeu, adh): #Fonction de confirmation DANS la fonction de fenetre.
        if askyesno("Confirmation", "etes-vous sur de vouloir emprunter ce jeu ?"):
            dateDeb = datetime.date(int(ddy.get()), int(ddm.get()), int(ddd.get()))
            dur = int(duree.get())
            if mode==-1:
                Emprunt.emprunterJeu(numJeu, adh, dateDeb, dur)
            if mode==0:
                Emprunt.emprunterExtensionSansJeu(adh, numJeu, dateDeb, dur)
            if mode==1:
                Emprunt.emprunterExtensionAvecJeu(adh, numJeu, dateDeb, dur)
            return retourCatalogue() #Ferme si "oui"
        else :
            return retourCatalogue()

    def retourJeu(numJeu):
        fEmprunt.destroy()
        return ficheJeu(numJeu)

    def retourCatalogue():
        fEmprunt.destroy()
        return catalogue()
        
    fEmprunt = Frame(infos[2])
    infos[2].title("Emprunt d'un jeu")
    #fEmprunt.grid_columnconfigure(0,weight=1)
    #fEmprunt.grid_rowconfigure(20,weight=21)

    p = PanedWindow(fEmprunt, orient = HORIZONTAL, height=100, width=300)
    adh=infos[0]
    p.grid(row=1)
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(infos[0]), bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour au catalogue", bg="orange", activebackground="orange", borderwidth=10, width=20, command= retourCatalogue ))
    p.add(Button(p, text="Retour au jeu", bg="orange", activebackground="orange", borderwidth=10, width=20, command= partial(retourJeu, numJeu)))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fEmprunt.destroy ))
    
    pd = PanedWindow(fEmprunt, orient = HORIZONTAL, height = 20, width = 400)
    pd.grid(row=2)
    pd.add(Label(pd, text="Date de debut : ", anchor=CENTER, width= 20))

    ddd = Spinbox(pd, from_=1, to=31, width= 5)
    ddm = Spinbox(pd, from_=1, to=12, width= 5)
    ddy = Spinbox(pd, from_=2016, to=2017, width= 8)
    pd.add(ddd)
    pd.add(ddm)
    pd.add(ddy)
    

    pt = PanedWindow(fEmprunt, orient = HORIZONTAL, height = 20, width = 400)
    pt.grid(row=3)
    pt.add(Label(pt, text="Durée (en jour) : ", anchor=CENTER, width= 20))
    duree = Spinbox(pt, from_=1, to=99, width= 5)
    pt.add(duree)


    
    Button(fEmprunt, text ="Emprunter !", command = partial(CallBackEmprunt, numJeu, adh)).grid(row=4)

    fEmprunt.pack()
    infos[2].mainloop()

    donneesEmprunt = [ddd.get(), ddm.get(), ddy.get(), dfd.get(), dfm.get(), dfy.get()]
    
    fEmprunt.destroy()

    return donneesEmprunt















#INTERFACE DE RESERVATION D'UN JEU


def reserver(numJeu, mode=-1): #idJeu/extension + idAdherent + booleenJeu (Vrai si l'id en param est un Jeu, Faux si c'est une extension
    # + booleenExtension (Par defaut a faux, vrai si on ne reserve qu'UNE extension)
    def CallBackReserv(adh, numJeu): #Fonction de confirmation DANS la fonction de fenetre.
        if askyesno("Confirmation", "etes-vous sur de vouloir réserver ce jeu ?"):
            dateDeb = datetime.date(int(ddy.get()), int(ddm.get()), int(ddd.get()))
            dur = int(duree.get())
            if mode==-1:
                Reservation.reserverJeu(adh, numJeu, dateDeb, dur)
            if mode==0:
                Reservation.reserverExtensionSansJeu(adh, numJeu, dateDeb, dur)
            if mode==1:
                Reservation.reserverExtensionAvecJeu(adh, numJeu, dateDeb, dur)
            return retourCatalogue() #Ferme si "oui"
        else :
            return retourCatalogue()

    def retourJeu(numJeu):
        fResa.destroy()
        return ficheJeu(numJeu)

    def retourCatalogue():
        fResa.destroy()
        return catalogue()
        
    fResa = Frame(infos[2])
    infos[2].title("Reservation du jeu " + str(Jeu.getNomJeu(numJeu)))
    fResa.grid_columnconfigure(0,weight=1)
    fResa.grid_rowconfigure(20,weight=21)

    p = PanedWindow(fResa, orient = HORIZONTAL, height=100, width=300)
    p.grid(row=1)
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(infos[0]), bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour au catalogue", bg="orange", activebackground="orange", borderwidth=10, width=20, command= retourCatalogue ))
    p.add(Button(p, text="Retour au jeu", bg="orange", activebackground="orange", borderwidth=10, width=20, command= partial(retourJeu, numJeu)))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = infos[2].destroy ))
    
    pd = PanedWindow(fResa, orient = HORIZONTAL, height = 20, width = 400)
    pd.grid(row=2)
    pd.add(Label(pd, text="Date de début : ", anchor=CENTER, width= 20))
    ddd = Spinbox(pd, from_=1, to=31, width= 5)
    ddm = Spinbox(pd, from_=1, to=12, width= 5)
    ddy = Spinbox(pd, from_=2016, to=2018, width= 8)
    pd.add(ddd)
    pd.add(ddm)
    pd.add(ddy)
    

    pt = PanedWindow(fResa, orient = HORIZONTAL, height = 20, width = 400)
    pt.grid(row=3)
    pt.add(Label(pt, text="Durée : ", anchor=CENTER, width= 20))
    duree = Spinbox(pt, from_=1, to=99, width= 5)
    pt.add(duree)
    

    Button(fResa, text ="Reserver !", command = partial(CallBackReserv, infos[0], numJeu)).grid(row=4)

    fResa.pack()
    infos[2].mainloop()

    donneesEmprunt = [ddd.get(), ddm.get(), ddy.get(), dfd.get(), dfm.get(), dfy.get()]

    fResa.destroy()

    return donneesEmprunt















##Si modification=-1 : modification d'un adhérent par l'adhérent
##    -Permet à l'adhérent de modifier ses infos
##
##Si modification= 0 : modification d'un adhérent par l'administrateur
##    -Permet à l'admin de modifier les infos d'un adhérent
##    -Le paramètre numAdh est égale à l'id de l'adhérent qui doit etre modifier
##
##Si modification= 1 : création d'un adhérent par l'administrateur
##    -Permet à l'admin de créer un adhérent. L'idAdhérent en paramètre n'a pas d'importance
##    -Le paramètre idAdmin est égale à l'id de l'administrateur qui modifie l'adhérent


#MODIFICATION/CREATION D'UN ADHERENT


def formulaireAdherent(numAdh=infos[0], modification=1):
    fAdh = Frame(infos[2])
    infos[2].title("Profil de "+Adherent.getPrenom(numAdh))

    def retourMenu(): #Fonction de confirmation DANS la fonction de fenetre.
        fAdh.destroy()
        return menu()


    def CallBackFormulaireAdh(): #Fonction de confirmation DANS la fonction de fenetre.
        #recupere les infos 
        infoAdh.append(entryNomAdh.get())
        infoAdh.append(entryPrenomAdh.get())
        infoAdh.append(entryPseudoAdh.get())
        if(modification == -1):
                infoAdh.append(entryMdpAdh.get())
        else:
            infoAdh.append(None)
        j = int(entryDnjAdh.get())
        m = int(entryDnmAdh.get())
        a = int(entryDnaAdh.get())
        d = datetime.date(a, m, j)
        infoAdh.append(d)
        infoAdh.append(entryAdrAdh.get())
        infoAdh.append(entryVilleAdh.get())
        infoAdh.append(entryCpAdh.get())
        infoAdh.append(entryNumAdh.get())
        infoAdh.append(entryMailAdh.get())
        if(cocher.get()==1):
            infoAdh.append(True)
        else:
            infoAdh.append(False)
        
        #ordre infoAdh : nom,prenom,pseudo,mdp,dateNaissance,adresse,ville,codepostale,numTel,@Mail,estAdmin
        #on modifie un adherent
        if(modification<>1):
            if (askyesno("Confirmation", "Enregistrer vos modification")):
                Adherent.setNom(numAdh,infoAdh[0])
                Adherent.setPrenom(numAdh,infoAdh[1])
                Adherent.setPseudo(numAdh,infoAdh[2])
                if modification == -1:
                    Adherent.setMotDePasse(numAdh,infoAdh[3])
                Adherent.setNaissance(numAdh,infoAdh[4])
                Adherent.setAdresse(numAdh,infoAdh[5])
                Adherent.setVille(numAdh,infoAdh[6])
                Adherent.setCodePostale(numAdh,infoAdh[7])
                Adherent.setNumeroTelephone(numAdh,infoAdh[8])
                Adherent.setMail(numAdh,infoAdh[9])
                if modification == 0:
                    Adherent.setAdministrateur(numAdh,infoAdh[10])
                return fAdh.quit() #Ferme si "oui"
            else:
                return 
        #on creer un adherent
        else:
            #verification de l'unicité du pseudo
            if Adherent.getIdByPseudo(infoAdh[2]) <> None:
                showwarning('Pseudo','Ce pseudo est déja utilisé.\nVeuillez recommencer !')
                entryPseudoAdh.delete(0, END)
                return
            else:
                #ajout de l'adherent
                if (askyesno("Confirmation", "Creer ce nouveau adherent ?")):
                    #ajoutAdherent(nomAdherent, prenomAdherent, dateNaissanceAdherent, adresseAdherent, codePostalAdherent, villeAdherent, numeroTelAdherent,  pseudoAdherent, adresseMailAdherent, estAdmin)
                    Adherent.ajoutAdherent(infoAdh[0],infoAdh[1],infoAdh[4],infoAdh[5],infoAdh[7],infoAdh[6],infoAdh[8],infoAdh[2],infoAdh[9],infoAdh[10])
                    return fAdh.quit() #Ferme si "oui"
                else:
                    return 

    #menu haut
    p = PanedWindow(fAdh, orient = HORIZONTAL, height=100, width=600)
    p.grid(row=1, column=1, columnspan=4)
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(numAdh), bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour au menu", bg="orange", activebackground="orange", borderwidth=10, width=20, command= partial(retourMenu)))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = infos[2].destroy ))
    
    Label(fAdh, text="Profil", font=("Helvetica", 30), height=4).grid(row=2, column=1, columnspan=4)

    
    #ordre : nom,prenom,pseudo,mdp,dateNaissance,adresse,ville,codepostale,numTel,@Mail,estAdmin
    infoAdh = []
    
    #nom
    Label(fAdh, text="Nom : ").grid(row=3, column=1, columnspan=1)
    if(modification == 1):
        nomAdh = ""
    else:
        nomAdh = StringVar()
        nomAdh.set(Adherent.getNom(numAdh))
    entryNomAdh = Entry(fAdh,textvariable=nomAdh,width=40)
    entryNomAdh.grid(row=3, column=2, columnspan=1)
    
    #prenom
    Label(fAdh, text="Prénom : ").grid(row=4, column=1, columnspan=1)
    if(modification == 1):
        prenomAdh = ""
    else:
        prenomAdh = StringVar()
        prenomAdh.set(Adherent.getPrenom(numAdh))
    entryPrenomAdh = Entry(fAdh,textvariable=prenomAdh,width=40)
    entryPrenomAdh.grid(row=4, column=2, columnspan=1)
    
    #pseudo
    Label(fAdh, text="Pseudo : ").grid(row=5, column=1, columnspan=1)
    if(modification == 1):
        pseudoAdh = ""
        entryPseudoAdh = Entry(fAdh,textvariable=pseudoAdh,width=40)
    else:
        pseudoAdh = StringVar()
        pseudoAdh.set(Adherent.getPseudo(numAdh))
        entryPseudoAdh = Entry(fAdh,textvariable=pseudoAdh,width=40, state=DISABLED)
    entryPseudoAdh.grid(row=5, column=2, columnspan=1)
    
    #mdp
    if(modification <> 1):
        Label(fAdh, text="Mot de passe : ").grid(row=6, column=1, columnspan=1)
        if modification == 0:
            Button(fAdh, text="Reinitialiser MDP", command= Adherent.reinitialiserMDPAdherent(numAdh)).grid(row=6, column=2, columnspan=2)
        else:
            mdpAdh = StringVar()
            mdpAdh.set(Adherent.getMotDePasse(numAdh))
            entryMdpAdh = Entry(fAdh,textvariable=mdpAdh,width=40,show="*")
            entryMdpAdh.grid(row=6, column=2, columnspan=1)
        
    #date Naissance
    Label(fAdh, text="Date de naissance : ").grid(row=7, column=1)
    if(modification == 1):
        dnjAdh=""
        dnmAdh=""
        dnaAdh="1900"

    else:
        dnaAdh = StringVar()
        dnaAdh.set(Adherent.getNaissance(numAdh)[0:4])
        dnmAdh = StringVar()
        dnmAdh.set(Adherent.getNaissance(numAdh)[5:7])
        dnjAdh = StringVar()
        dnjAdh.set(Adherent.getNaissance(numAdh)[8:10])

    poo = PanedWindow(fAdh, orient = HORIZONTAL)
    entryDnjAdh = Spinbox(fAdh, textvariable=dnjAdh, from_=1, to =31, width=10)
    poo.add(entryDnjAdh)
    
    entryDnmAdh = Spinbox(fAdh, textvariable=dnmAdh, from_=1, to =12, width=10)
    poo.add(entryDnmAdh)
    
    entryDnaAdh = Spinbox(fAdh, textvariable=dnaAdh, from_=1900, to=datetime.date.today().year, width=10)
    poo.add(entryDnaAdh)

    poo.grid(row=7, column=2, columnspan=1)

    #adresse
    Label(fAdh, text="Adresse : ").grid(row=8,column=1, columnspan=1)
    if(modification == 1):
        adrAdh = ""
    else:
        adrAdh = StringVar()
        adrAdh.set(Adherent.getAdresse(numAdh))
    entryAdrAdh = Entry(fAdh,textvariable=adrAdh,width=40)
    entryAdrAdh.grid(row=8, column=2, columnspan=1)

    #ville
    Label(fAdh, text="Ville : ").grid(row=9, column=1, columnspan=1)
    if(modification == 1):
        villeAdh = ""
    else:
        villeAdh = StringVar()
        villeAdh.set(Adherent.getVille(numAdh))
    entryVilleAdh = Entry(fAdh,textvariable=villeAdh,width=40)
    entryVilleAdh.grid(row=10, column=2, columnspan=1)
    
    #code postale
    Label(fAdh, text="Code postal : ").grid(row=10, column=1, columnspan=1)
    if(modification == 1):
        cpAdh = ""
    else:
        cpAdh = StringVar()
        cpAdh.set(Adherent.getCodePostal(numAdh))
    entryCpAdh = Entry(fAdh,textvariable=cpAdh,width=40)
    entryCpAdh.grid(row=9, column=2, columnspan=1)
    
    #num telephone
    Label(fAdh, text="Numéro : ").grid(row=11, column=1, columnspan=1)
    if(modification == 1):
        numeroAdh = ""
    else:
        numeroAdh = StringVar()
        numeroAdh.set(Adherent.getNumTelephone(numAdh))
    entryNumAdh = Entry(fAdh,textvariable=numeroAdh,width=40)
    entryNumAdh.grid(row=11, column=2, columnspan=1)

    #adresse mail
    Label(fAdh, text="Adresse Mail : ").grid(row=12, column=1, columnspan=1)
    if(modification == 1):
        mailAdh = ""
    else:
        mailAdh = StringVar()
        mailAdh.set(Adherent.getMail(numAdh))
    entryMailAdh = Entry(fAdh,textvariable=mailAdh,width=40)
    entryMailAdh.grid(row=12, column=2, columnspan=1)
    

    #estAdmin
    cocher = IntVar()    
    Label(fAdh, text="Administrateur : ").grid(row=13, column=1, columnspan=1)
    if modification == -1:
       admAdh = Checkbutton(fAdh, text="", variable = cocher, state=DISABLED)
    else:
        admAdh = Checkbutton(fAdh, text="", variable = cocher)
    admAdh.grid(row=13, column=2, columnspan=1)
    if Adherent.getEstAdministrateur(numAdh)==True:
        admAdh.select()
    else:
        admAdh.deselect()
    if modification==1:
        admAdh.deselect()
        
    
       
    
    Button(fAdh, text="Enregistrer", command = partial(CallBackFormulaireAdh)).grid(row=14, column=1, columnspan=4)
    
    #Lancement de la fenetre
    fAdh.pack()
    infos[2].mainloop()
    #Enfin on detruit la fenetre
    fAdh.destroy()
    
    menu()

    




####AFFICHAGE DES EMPRUNTS

def catalogueEmprunt(Emprunts=Emprunt.getAllEmprunts()): #idAdherent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fcatalogue.after(1000,maj)

    def retourMenu():
        fcatalogue.destroy()
        return menu()

    def rend(i):
        Emprunt.rendre(i, datetime.date.today())
        fcatalogue.destroy()
        return catalogueEmprunt(Adherent.getAllEmpruntAdherent(infos[0]))
        

    def afficheEmprunts(n, Emprunts, k=0):
        n[0]=n[0]+k
        r = n[2]-n[1]
        if (r>20): r=20
        if (n[0]<n[1]):
            n[0]=n[1]
        if (n[0]+r>n[2]):
            n[0]=n[2]-r
        j=3
        
        for i in range(n[0],n[0]+r):
            Label(fcatalogue, text=str(Adherent.getNom(Emprunts[i][1])), bg="orange", width = 25).grid(row=j, column=1)
            Label(fcatalogue, text=str(Jeu.getNomJeu(Emprunts[i][2])), bg="orange", width = 25).grid(row=j, column=2)
            Label(fcatalogue, text=str(Extension.getNomExtension(Emprunts[i][3])), bg="orange", width = 20).grid(row=j, column=3)
            Label(fcatalogue, text=str(Emprunts[i][4]), bg="orange", width = 15).grid(row=j, column=4)
            Label(fcatalogue, text=str(Emprunts[i][5]), bg="orange", width = 15).grid(row=j, column=5)
            Label(fcatalogue, text=str(Emprunts[i][6]), bg="orange", width = 10).grid(row=j, column=6)
            Label(fcatalogue, text=str(Emprunt.getDateFinEmprunt(Emprunts[i][0])), bg="orange", width = 10).grid(row=j, column=7)
            if (Emprunts[i][5]==0):
                if (Emprunt.getDateFinEmprunt(Emprunts[i][0]) > datetime.date.today()):
                    Label(fcatalogue, text=str("EN COURS"), bg="cyan", width = 10).grid(row=j, column=8)
                else:
                    Label(fcatalogue, text=str("EN RETARD"), bg="red", width = 10).grid(row=j, column=8)
            else:
                if (Emprunt.getDateFinEmprunt(Emprunts[i][0]) > datetime.date(int(Emprunt.getDateRenduEmprunt(Emprunts[i][0])[0:4]),
                                                                              int(Emprunt.getDateRenduEmprunt(Emprunts[i][0])[5:7]),
                                                                              int(Emprunt.getDateRenduEmprunt(Emprunts[i][0])[8:10]))):
                    Label(fcatalogue, text=str("RENDU"), bg="orange", width = 10).grid(row=j, column=8)
                else:
                    Label(fcatalogue, text=str("RENDU"), bg="pink", width = 10).grid(row=j, column=8)
            if (infos[1]):
                Button(fcatalogue, text="Modifier", command = rien,bg="blue", width=13,activebackground="blue").grid(row=j, column=9)

            if (infos[1] and Emprunts[i][5]==0):
                Button(fcatalogue, text="Rendre", command = partial(rend,Emprunts[i][0]),bg="yellow", width=13,activebackground="red").grid(row=j, column=10)
            j=j+1

    
    fcatalogue = Frame(infos[2])
    infos[2].title("Listes des emprunts")
    fcatalogue.grid_columnconfigure(0,weight=1)
    fcatalogue.grid_rowconfigure(20,weight=21)
    
    p = PanedWindow(fcatalogue, orient = HORIZONTAL, height=100, width=1000)
    p.grid(row=1, column=1, columnspan=11)
     
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=30))
    maj()
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(infos[0]), bg="white", anchor=CENTER, width=10))
    if (infos[1]):
        p.add(Button(p, text="Ajouter un emprunt", bg="cyan", activebackground="cyan", borderwidth=10, width=10, command= rien))#partial(formulaireJeu,numAdh)))
    p.add(Button(p, text="Retour au menu principal", bg="orange", activebackground="orange", borderwidth=10, width=10, command= retourMenu ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = infos[2].destroy ))

    Label(fcatalogue, text="Adhérent", bg="green", width = 25).grid(row=2, column=1)
    Label(fcatalogue, text="Jeu", bg="green", width = 25).grid(row=2, column=2)
    Label(fcatalogue, text="Extension", bg="green", width = 20).grid(row=2, column=3)
    Label(fcatalogue, text="Date du début", bg="green", width = 15).grid(row=2, column=4)
    Label(fcatalogue, text="Date de rendu", bg="green", width = 15).grid(row=2, column=5)
    Label(fcatalogue, text="Durée prévue", bg="green", width = 10).grid(row=2, column=6)
    Label(fcatalogue, text="Date de rendu prévue", bg="green", width = 10).grid(row=2, column=7)
    Label(fcatalogue, text="Emprunt en cours", bg="blue", width = 13).grid(row=2, column=8)
    
    if (infos[1]):
        Label(fcatalogue, text="Que faire ?", bg="green", width = 24).grid(row=2, column=9, columnspan=2)

    numEmprunt=[0,0,len(Emprunts)]
    flecheH = Button(fcatalogue, text="^", command = partial(afficheEmprunts, numEmprunt, Emprunts, -20), bg="blue", width=5,activebackground="blue").grid(row=3, column=11)
    flecheB = Button(fcatalogue, text="v", command = partial(afficheEmprunts, numEmprunt, Emprunts, 20), bg="blue", width=5,activebackground="blue").grid(row=22, column=11)
    afficheEmprunts(numEmprunt, Emprunts)
    
        
    fcatalogue.pack()
    infos[2].mainloop()














    ####AFFICHAGE DES RESERVATION

def catalogueReservation(Reservations=Reservation.getAllReservations()): #idAdherent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fcatalogue.after(1000,maj)

    def retourMenu():
        fcatalogue.destroy()
        return menu()

    def annule(i):
        if askyesno("Confirmation", "etes-vous sur de vouloir annuler votre réservation ?"):
            if (Reservation.enAttente(i)):
                Reservation.annulerReservApresDateButoire(i)
            else:
                Reservation.annulerReservAvantDateButoire(i)
            fcatalogue.destroy()
            if (infos[1]):
                return catalogueReservation(Reservation.getAllReservations())
            else:
                return catalogueReservation(Adherent.getAllReservationAdherent(infos[0]))
        else:
            return

    def valide(i):
        if askyesno("Confirmation", "etes-vous sur de vouloir valider cette réservation et en faire un emprunt ?"):
            Reservation.validerEmprunt(i, datetime.date.today())
            fcatalogue.destroy()
            return catalogueReservation(Reservation.getAllReservations())
        else:
            return

    def afficheReservations(n, Reservations, k=0):
        n[0]=n[0]+k
        r = n[2]-n[1]
        if (r>20): r=20
        if (n[0]<n[1]):
            n[0]=n[1]
        if (n[0]+r>n[2]):
            n[0]=n[2]-r
        j=3
        
        for i in range(n[0],n[0]+r):
            Label(fcatalogue, text=str(Adherent.getNom(Reservations[i][1])), bg="orange", width = 20).grid(row=j, column=1)
            Label(fcatalogue, text=str(Jeu.getNomJeu(Reservations[i][2])), bg="orange", width = 25).grid(row=j, column=2)
            Label(fcatalogue, text=str(Extension.getNomExtension(Reservations[i][3])), bg="orange", width = 20).grid(row=j, column=3)
            Label(fcatalogue, text=str(Reservations[i][4]), bg="orange", width = 25).grid(row=j, column=4)
            Label(fcatalogue, text=str(Reservations[i][5]), bg="orange", width = 25).grid(row=j, column=5)
            Label(fcatalogue, text=str(Reservation.getDateFinEmprunt(Reservations[i][0])), bg="orange", width = 20).grid(row=j, column=6)
            if (Reservation.enAttente(Reservations[i][0])):
                Label(fcatalogue, text=str("En Retard"), bg="red", width = 20).grid(row=j, column=7)
            else:
                Label(fcatalogue, text=str("En Attente"), bg="cyan", width =20).grid(row=j, column=7)
            Button(fcatalogue, text="Annuler", command = partial(annule, Reservations[i][0]),bg="yellow", width=13,activebackground="red").grid(row=j, column=9)
            if (infos[1]):
                Button(fcatalogue, text="Modifier", command = rien,bg="blue", width=13,activebackground="blue").grid(row=j, column=8)
                Button(fcatalogue, text="Valider", command = partial(valide, Reservations[i][0] ),bg="yellow", width=13,activebackground="red").grid(row=j, column=10)
            j=j+1

         
    fcatalogue = Frame(infos[2])
    infos[2].title("Listes des réservations")
    fcatalogue.grid_columnconfigure(0,weight=1) #Label(fcatalogue, text="Date de fin d'emprunt", bg="green", width = 20).grid(row=2, column=6)
    fcatalogue.grid_rowconfigure(20,weight=21)
    
    p = PanedWindow(fcatalogue, orient = HORIZONTAL, height=100, width=1000)
    p.grid(row=1, column=1, columnspan=11)
     
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=30))
    maj()
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(infos[0]), bg="white", anchor=CENTER, width=10))
    p.add(Button(p, text="Ajouter une réservation", bg="cyan", activebackground="cyan", borderwidth=10, width=10, command= rien))#partial(formulaireReservation,numAdh)))
    p.add(Button(p, text="Retour au menu principal", bg="orange", activebackground="orange", borderwidth=10, width=10, command= retourMenu ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = infos[2].destroy ))

    Label(fcatalogue, text="AdhÃƒÂ©rent", bg="green", width = 20).grid(row=2, column=1)
    Label(fcatalogue, text="Jeu", bg="green", width = 25).grid(row=2, column=2)
    Label(fcatalogue, text="Extension", bg="green", width = 20).grid(row=2, column=3)
    Label(fcatalogue, text="Date de la Réservation", bg="green", width = 25).grid(row=2, column=4)
    Label(fcatalogue, text="Durée prévu de l'emprunt", bg="green", width = 25).grid(row=2, column=5)
    Label(fcatalogue, text="Date de fin d'emprunt", bg="green", width = 20).grid(row=2, column=6)
    Label(fcatalogue, text="Réservation en attente", bg="blue", width = 20).grid(row=2, column=7)
    Label(fcatalogue, text="Que faire ?", bg="green", width = 24).grid(row=2, column=8, columnspan=2)

    numReservation=[0,0,len(Reservations)]
    flecheH = Button(fcatalogue, text="^", command = partial(afficheReservations, numReservation, Reservations, -20), bg="blue", width=5,activebackground="blue").grid(row=3, column=11)
    flecheB = Button(fcatalogue, text="v", command = partial(afficheReservations, numReservation, Reservations, 20), bg="blue", width=5,activebackground="blue").grid(row=22, column=11)
    afficheReservations(numReservation, Reservations)
    
        
    fcatalogue.pack()
    infos[2].mainloop()






####AFFICHAGE DES ADHERENTS

def catalogueAdherents(Adherents=Adherent.getAllAdherent()): #idAdherent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fcatalogue.after(1000,maj)

    def retourMenu():
        fcatalogue.destroy()
        return panneauAdmin()

    def lanceCatalogue():
        r = entryRecherche.get()
        fcatalogue.destroy()
        return catalogueAdherents(Adherent.getAdherentByName(r))

    def adhr(i,j):
        fcatalogue.destroy()
        return formulaireAdherent(i,j)

    def supp(i):
        if askyesno("Confirmation", "Etes-vous sur de vouloir supprimer cet adhérent ainsi que toutes les données associées (emprunts, réservations) ?"):
            Adherent.supprimerAdherent(i)
            fcatalogue.destroy()
            return catalogueAdherents(Adherent.getAllAdherent())
        else:
            return

    def afficheAdherents(n, Adherents, k=0):
        n[0]=n[0]+k
        r = n[2]-n[1]
        if (r>20): r=20
        if (n[0]<n[1]):
            n[0]=n[1]
        if (n[0]+r>n[2]):
            n[0]=n[2]-r
        j=3
        
        for i in range(n[0],n[0]+r):
            Label(fcatalogue, text=str(Adherents[i][1]), bg="orange", width = 10).grid(row=j, column=1)
            Label(fcatalogue, text=str(Adherents[i][2]), bg="orange", width = 10).grid(row=j, column=2)
            Label(fcatalogue, text=str(Adherents[i][3]), bg="orange", width =10).grid(row=j, column=3)
            Label(fcatalogue, text=str(Adherents[i][4]), bg="orange", width = 12).grid(row=j, column=4)
            Label(fcatalogue, text=str(Adherents[i][5]), bg="orange", width = 8).grid(row=j, column=5)
            Label(fcatalogue, text=str(Adherents[i][6]), bg="orange", width = 10).grid(row=j, column=6)
            Label(fcatalogue, text=str(Adherents[i][7]), bg="orange", width = 10).grid(row=j, column=7)
            Label(fcatalogue, text=str(Adherents[i][8]), bg="orange", width = 10).grid(row=j, column=8)
            Label(fcatalogue, text=str(Adherents[i][10]), bg="orange", width = 10).grid(row=j, column=10)
            if (Adherents[i][11]):
                Label(fcatalogue, text="Oui", bg="orange", width = 7).grid(row=j, column=11)
            else:
                Label(fcatalogue, text="Non", bg="orange", width = 7).grid(row=j, column=11)
            Label(fcatalogue, text=str(Adherents[i][12]), bg="orange", width = 10).grid(row=j, column=12)
            Label(fcatalogue, text=str(Adherents[i][13]), bg="orange", width = 5).grid(row=j, column=14)
            Label(fcatalogue, text=str(Adherents[i][14]), bg="orange", width = 5).grid(row=j, column=15)
            Label(fcatalogue, text=str(Adherents[i][15]), bg="orange", width = 5).grid(row=j, column=16)
            if (Adherents[i][16]<> 0):
                Label(fcatalogue, text=str(Jeu.getNomJeu(Emprunt.getIdJeuEmprunt(Adherents[i][16]))), bg="cyan", width = 10).grid(row=j, column=17)
            else:
                Label(fcatalogue, text=str("AUCUN"), bg="orange", width = 10).grid(row=j, column=17)
            if (Adherents[i][17]<>0):
                Label(fcatalogue, text=str(Jeu.getNomJeu(Reservation.getIdJeuReserv(Adherents[i][17]))), bg="cyan", width = 10).grid(row=j, column=18)
            else:
                Label(fcatalogue, text=str("AUCUN"), bg="orange", width = 10).grid(row=j, column=18)
            
            if (Adherent.estAJour(Adherents[i][0])):
                Label(fcatalogue, text=str("DEPASSE"), bg="red", width = 10).grid(row=j, column=13)
            else:
                Label(fcatalogue, text=str("A JOUR"), bg="cyan", width =10).grid(row=j, column=13)
            Button(fcatalogue, text="Modifier", command = partial(adhr,Adherents[i][0],0),bg="blue", width=13,activebackground="blue").grid(row=j, column=19)
            Button(fcatalogue, text="Supprimer", command = partial(supp, Adherents[i][0]),bg="yellow", width=13,activebackground="red").grid(row=j, column=20)
            Button(fcatalogue, text="Réinitialiser", command = rien,bg="yellow", width=10,activebackground="red").grid(row=j, column=9)
            j=j+1

    
    fcatalogue = Frame(infos[2])
    infos[2].title("Listes des adherents")
    fcatalogue.grid_columnconfigure(0,weight=1)
    fcatalogue.grid_rowconfigure(20,weight=21)
    
    p = PanedWindow(fcatalogue, orient = HORIZONTAL, height=100, width=1600)
    p.grid(row=1, column=1, columnspan=21)
     
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=30))
    maj()
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(infos[0]), bg="white", anchor=CENTER, width=10))
    rech=StringVar()
    rech.set("Faites une recherche ici !")

    entryRecherche = Entry(p, textvariable=rech, width = 30)
    p.add(entryRecherche)
    p.add(Button(p, text="Recherchez !", bg="orange", activebackground="orange", borderwidth=10, width=10, command= lanceCatalogue))
    p.add(Button(p, text="Ajouter un adherent", bg="cyan", activebackground="cyan", borderwidth=10, width=10, command= partial(adhr,0,1)))#partial(formulaireAdhésion,numAdh)))
    p.add(Button(p, text="Retour au menu principal", bg="orange", activebackground="orange", borderwidth=10, width=10, command= retourMenu ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = infos[2].destroy ))

    Label(fcatalogue, text="Nom", bg="green", width = 10).grid(row=2, column=1)
    Label(fcatalogue, text="Prénom", bg="green", width = 10).grid(row=2, column=2)
    Label(fcatalogue, text="Anniversaire", bg="green", width = 10).grid(row=2, column=3)
    Label(fcatalogue, text="Adresse", bg="green", width = 12).grid(row=2, column=4)
    Label(fcatalogue, text="Code Postal", bg="green", width = 8).grid(row=2, column=5)
    Label(fcatalogue, text="Ville", bg="green", width = 10).grid(row=2, column=6)
    Label(fcatalogue, text="Telephone", bg="green", width = 10).grid(row=2, column=7)
    Label(fcatalogue, text="Pseudo", bg="green", width = 10).grid(row=2, column=8)
    Label(fcatalogue, text="Mot de Passe", bg="green", width = 10).grid(row=2, column=9)
    Label(fcatalogue, text="Email", bg="green", width = 10).grid(row=2, column=10)
    Label(fcatalogue, text="Admin", bg="green", width = 7).grid(row=2, column=11)
    Label(fcatalogue, text="Paiement", bg="green", width = 10).grid(row=2, column=12)
    Label(fcatalogue, text="A jour ?", bg="green", width = 10).grid(row=2, column=13)
    Label(fcatalogue, text="NR", bg="green", width = 5).grid(row=2, column=14)
    Label(fcatalogue, text="JR", bg="green", width = 5).grid(row=2, column=15)
    Label(fcatalogue, text="RA", bg="green", width = 5).grid(row=2, column=16)
    Label(fcatalogue, text="Jeu Emprunté", bg="green", width = 10).grid(row=2, column=17)
    Label(fcatalogue, text="Jeu Réservé", bg="green", width = 10).grid(row=2, column=18)
    Label(fcatalogue, text="Que faire ?", bg="green", width = 24).grid(row=2, column=19, columnspan=2)

    numAdherents=[0,0,len(Adherents)]
    flecheH = Button(fcatalogue, text="^", command = partial(afficheAdherents, numAdherents, Adherents, -20), bg="blue", width=5,activebackground="blue").grid(row=3, column=21)
    flecheB = Button(fcatalogue, text="v", command = partial(afficheAdherents, numAdherents, Adherents, 20), bg="blue", width=5,activebackground="blue").grid(row=22, column=21)
    afficheAdherents(numAdherents, Adherents)
    
        
    fcatalogue.pack()
    infos[2].mainloop()
