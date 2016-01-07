from Tkinter import *
from tkMessageBox import *
from datetime import *
import datetime
from functools import partial
from Jeu import Jeu
from Adherent import Adherent
from Extension import Extension
from Emprunt import Emprunt




#FORMULAIRE DE JEU

def formulaireJeu(idJeu = -1): #Par dÃ©faut, -1 = creation
    """Prend l'id d'un jeu pour le modifier, ou -1 pour en creer un nouveau"""
    FJ = Tk()
    FJ.wm_attributes("-topmost" , -1) #Mets la fenetre au premier plan dÃ¨s son apparition.
    idJ = IntVar()
    idJ.set(idJeu)
    Creation = BooleanVar()            #Les variables declarÃ©e comme ceci semble Ãªtre utilisable pour les fonctions imbriquÃ© de Tkinter
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
            return FJ.destroy() #Ferme aprÃ¨s avoir enregistre.
        else : return

    def cancel(): #Ferme la fenetre
        if askyesno("Quitter", "Annuler le formulaire ?"):
            FJ.quit() #Ferme la fenetre
            return FJ.destroy() #N'enregistre rien
        else : return
    T1 = LabelFrame(FJ, text="Formulaire de jeu :")
    NJ = Label(FJ, text="Nom du jeu :")
    AnJ = Label(FJ, text="AnnÃ©e de sortie du jeu :")
    AgJ = Label(FJ, text="Ages du public du jeu :")
    NbJ = Label(FJ, text="Nombre de joueur pour ce jeu($$-$$) :")
    QJ = Label(FJ, text="Nombre d'exemplaire total du jeu :")
    AJ = Label(FJ, text="Auteur du jeu :")
    IJ = Label(FJ, text="Illustrateur du jeu :")
    EJ = Label(FJ, text="Editeur du jeu :")
    Emp = Label(FJ, text="Ce jeu peut-etre EmpruntÃ© :")
    SJ =Label(FJ, text="Description du jeu (200caractÃ¨res) :")
    AddJ = Label(FJ, text="Ajouter le jeu :")
    #Titre
    T1.pack()
    #Nom du jeu (champs Ã  remplir)
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
    #Age joueurs(Champs Ã  remplir)
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
    #Auteur du jeu (champs Ã  remplir)
    AJ.pack()
    auteurJeu=StringVar()
    auteurJeu.set(auteurJ)
    AJI = Entry(FJ, textvariable=auteurJeu, width = 45)
    AJI.pack()
    #Illustrateur du jeu (champs Ã  remplir)
    IJ.pack()
    illustrateurJeu=StringVar()
    illustrateurJeu.set(illustrateurJ)
    IJI = Entry(FJ, textvariable=illustrateurJeu, width = 45)
    IJI.pack()
    #Editeur du jeu (champs Ã  remplir)
    EJ.pack()
    editeurJeu=StringVar()
    editeurJeu.set(editeurJ)
    EJI = Entry(FJ, textvariable=editeurJeu, width = 45)
    EJI.pack()
    #Empruntable ou non ? (case Ã  cocher)
    Emp.pack()
    Empbool = BooleanVar()
    Empbool.set(estEmpruntableJ)
    EmpI = Checkbutton(FJ, text="Est-il empruntable?", variable = Empbool)
    EmpI.pack()
    #Synospis du jeu (Champs Ã  remplir)
    SJ.pack()
    synopsisJeu = StringVar()
    synopsisJeu.set(synopsisJ)
    SJI = Entry(FJ, textvariable=synopsisJeu, width = 45)
    SJI.pack()
    #Fin : Confirmation de l'ajout/modification du jeu, appel de la fonction submit (sans parenthÃ¨ses)
    AddJ.pack()
    AddJI = Button(FJ, text="Confirmer", command = submit)
    AddJI.pack()
    #Fin : Annulation.(marche pas encore)
    Cancel = Button(FJ, text="Annuler", command = cancel)
    Cancel.pack()
    #Lancement de la fenetre
    FJ.mainloop()



def formulaireExt(idExt = -1, idJeu=0): #Par dÃ©faut, idExt =-1 => creation
    """Prend l'id d'une extension pour la modifier, ou -1 pour en creer une nouvelle"""
    
    FE = Tk()
    FE.title("Formulaire d'extension")
    FE.wm_attributes("-topmost" , -1) #Mets la fenetre au premier plan dÃ¨s son apparition.
    idE = IntVar()
    idE.set(idExt)
    Creation = BooleanVar()            #Les variables declarÃ©e comme ceci semble Ãªtre utilisable pour les fonctions imbriquÃ© de Tkinter
    Creation.set(False)
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
            return FE.destroy() #Ferme aprÃ¨s avoir enregistre.
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
    #Nom du jeu (recupÃ¨re l'id du jeu dans la liste)
    NJE.pack()
    NomJeu = Label(FE, text =Jeu.getNomJeu(idJeu))
    NomJeu.pack() 
    #Nom de l'extension (champs Ã  remplir)
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
    #Fin : Confirmation de l'ajout/modification du extension, appel de la fonction submit (sans parenthÃ¨ses)
    AddE.pack()
    AddEI = Button(FE, text="Confirmer", command = submit)
    AddEI.pack()
    #Fin : Annulation.(marche pas encore)
    Cancel = Button(FE, text="Annuler", command = cancel)
    Cancel.pack()
    #Lancement de la fenetre
    FE.mainloop()






#INTERFACE DE CONNEXION


def connexion():
    def verification():
        ID = Adherent.getId(pseudo.get())
        if (ID <> None):
            if (mdp.get()==Adherent.getMotDePasse(ID)):
                fconnexion.destroy()
                menu(ID)
            else:
                showwarning('Mot de passe incorrect','Mot de passe incorrect.\nVeuillez recommencer !')
                mdp.set('')
        else:
            showwarning('Pseudo inexistant','Adresse mail ou pseudo inexistant.\nVeuillez recommencer !')
            mdp.set('')
            pseudo.set('')
        
    fconnexion = Tk()
    fconnexion.title("Connexion Ã  la LudothÃ©que")
    
    p = PanedWindow(fconnexion, orient = HORIZONTAL, height = 20, width = 300)
    p.grid(row=1)
    p.add(Label(p, text="Nom de connexion : ", anchor=CENTER, width= 20))
    pseudo = StringVar()
    p.add(Entry(p, width = 20, textvariable = pseudo))
    

    pd = PanedWindow(fconnexion, orient = HORIZONTAL, height = 20, width = 300)
    pd.grid(row=2)
    pd.add(Label(pd,text="Mot de passe : ", anchor = CENTER, width= 20))
    mdp = StringVar()
    pd.add(Entry(pd, width=20, show="*", textvariable = mdp ))
    

    Button(fconnexion, text ="Se connecter", command = verification).grid(row=3)

    fconnexion.mainloop()

def rien():
    return 










#MENU PRINCIPAL
        
def menu(numAdh=0): #numIdAdhÃ©rent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fmenu.after(1000,maj)

    def LancePanneauAdmin():
        fmenu.destroy()
        return panneauAdmin(numAdh) 
        
    def LanceCatalogue():
        fmenu.destroy()
        return catalogue(numAdherent=numAdh)

    def LanceProfil():
        fmenu.destroy()
        return formulaireAdherent(numAdh)

    def LanceEmprunt():
        fmenu.destroy()
        return catalogueEmprunt(numAdh, Adherent.getAllEmpruntAdherent(numAdh))

    def LancerReserver():
        fmenu.destroy()
        return reserver(0,numAdh)
        
    fmenu = Tk()
    fmenu.title("Menu principal")
    p = PanedWindow(fmenu,orient=HORIZONTAL, height=100, width=600)
    p.grid(row=1)
    
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=20))
    maj()
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(numAdh), bg="white", anchor=CENTER, width=20))
    if (Adherent.getEstAdministrateur(numAdh)<>None and Adherent.getEstAdministrateur(numAdh)):
        p.add(Button(p, text="Panneau d'administration", bg="orange", activebackground="orange", borderwidth=10, width=20, command=LancePanneauAdmin ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fmenu.destroy ))
    

    pd = PanedWindow(fmenu,orient=HORIZONTAL, height=350, width=600)
    pd.grid(row=2)
    pd.add(Button(pd, text="Profil", width=38, command = LanceProfil, bg="yellow", activebackground="yellow", borderwidth=10))
    pd.add(Button(pd, text="Catalogue", width=38, command = LanceCatalogue, bg="red", activebackground="red", borderwidth=10))

    
    pt = PanedWindow(fmenu,orient=HORIZONTAL, height=350, width=600)
    pt.grid(row=3)
    pt.add(Button(pt, text="Mes emprunts", command = LanceEmprunt, bg="green", width=38,activebackground="green", borderwidth=10))
    pt.add(Button(pt, text="RÃ©servation", command = LancerReserver,bg="cyan", width=38,activebackground="cyan", borderwidth=10))
    
    fmenu.mainloop()

    










#PANNEAU D'ADMINISTRATION


def panneauAdmin(numAdh=0): #numIdAdhÃ©rent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fpanneauadmin.after(1000,maj)

    def retourMenu():
        fpanneauadmin.destroy()
        return menu(numAdh)

    def LanceCatalogue():
        fpanneauadmin.destroy()
        return catalogue(numAdherent=numAdh, modeAdmin=True)

    def LanceEmprunt():
        fpanneauadmin.destroy()
        return catalogueEmprunt(numAdh, modeAdmin=True)
        
    if (not(Adherent.getEstAdministrateur(numAdh)<>None and Adherent.getEstAdministrateur(numAdh))):
        return menu(numAdh)
    
    fpanneauadmin = Tk()
    fpanneauadmin.title("Panneau d'aministration")
    
    p = PanedWindow(fpanneauadmin,orient=HORIZONTAL, height=100, width=600)
    p.grid(row=1)
    
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=20))
    maj()
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(numAdh), bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour menu", bg="orange", activebackground="orange", borderwidth=10, width=20, command= retourMenu))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fpanneauadmin.destroy ))
    
    pd = PanedWindow(fpanneauadmin,orient=HORIZONTAL, height=350, width=600)
    pd.grid(row=2)
    pd.add(Button(pd, text="Gestion des AdhÃ©rents", width=38, command = rien, bg="yellow", activebackground="yellow", borderwidth=10))
    pd.add(Button(pd, text="Gestion des Jeux", width=38, command = LanceCatalogue, bg="red", activebackground="red", borderwidth=10))


    pt = PanedWindow(fpanneauadmin,orient=HORIZONTAL, height=350, width=600)
    pt.grid(row=3)
    pt.add(Button(pt, text="Gestion des Emprunts", command = LanceEmprunt, bg="green", width=38,activebackground="green", borderwidth=10))
    pt.add(Button(pt, text="Gestion des rÃ©servations", command = rien,bg="cyan", width=38,activebackground="cyan", borderwidth=10))

    fpanneauadmin.mainloop()




#CATALOGUE DES JEUX


def catalogue( modeAdmin=False, numAdherent=0, Jeux=Jeu.getAllJeu()): #idAdherent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fcatalogue.after(1000,maj)

    def retourMenu():
        fcatalogue.destroy()
        return menu(numAdherent)

    def afficheFicheJeu(i):
        fcatalogue.destroy()
        return ficheJeu(numAdherent, i)
    
    def lancerEmprunt(i):
        fcatalogue.destroy()
        return formulaireEmprunt(i)

    def lancerReserv(i):
        fcatalogue.destroy()
        return reserver(i)

    def lanceCatalogue(n, ma):
        r = entryRecherche.get()
        fcatalogue.destroy()
        return catalogue(ma, n, Jeu.getJeuByNom(r))

    def lancerExtension(i, mode):
        fcatalogue.destroy()
        return afficheExtensions(i, mode)

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
            if (modeAdmin):
                Button(fcatalogue, text="Modifier", command = partial(formulaireJeu, Jeux[i][0]),bg="blue", width=13,activebackground="blue").grid(row=j, column=9) #partial(formulaireJeu,Jeux[i][0])
                Button(fcatalogue, text="CrÃ©er extension", command = partial(formulaireExt, -1, Jeux[i][0]),bg="cyan", width=13,activebackground="cyan").grid(row=j, column=14)
            else:
                Button(fcatalogue, text="DÃ©tail", command = partial(afficheFicheJeu,Jeux[i][0]) ,bg="blue", width=13,activebackground="blue").grid(row=j, column=9)
                
            if (Jeu.aDesExtensions(Jeux[i][0])):
                Button(fcatalogue, text="Extensions", command = partial(lancerExtension, Jeux[i][0], modeAdmin),bg="red", width=13,activebackground="red").grid(row=j, column=10)
            Button(fcatalogue, text="Emprunt", command = partial(lancerEmprunt, Jeux[i][0]),bg="green", width=13,activebackground="green").grid(row=j, column=11)
            Button(fcatalogue, text="Reserv", command = partial(lancerReserv, Jeux[i][0]),bg="red", width=13,activebackground="red").grid(row=j, column=12)
            if (modeAdmin):
                Button(fcatalogue, text="Supprimer", command = rien,bg="yellow", width=13,activebackground="red").grid(row=j, column=13)
            j=j+1

    
    fcatalogue = Tk()
    fcatalogue.title("Les jeux de la ludothÃ¨que")
    fcatalogue.grid_columnconfigure(0,weight=1)
    fcatalogue.grid_rowconfigure(20,weight=21)


    
    p = PanedWindow(fcatalogue, orient = HORIZONTAL, height=100, width=1000)
    p.grid(row=1, column=1, columnspan=11)
     
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=30))
    maj()

    rech=StringVar()
    rech.set("Faites une recherche ici !")

    entryRecherche = Entry(p, textvariable=rech, width = 30)
    p.add(entryRecherche)
    p.add(Button(p, text="Recherchez !", bg="orange", activebackground="orange", borderwidth=10, width=10, command= partial(lanceCatalogue,numAdherent,modeAdmin)))

    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(numAdherent), bg="white", anchor=CENTER, width=10))
    if (modeAdmin):
        p.add(Button(p, text="Ajouter un jeu", bg="cyan", activebackground="cyan", borderwidth=10, width=10, command= formulaireJeu))#partial(formulaireJeu,numAdh)))
    p.add(Button(p, text="Retour au menu principal", bg="orange", activebackground="orange", borderwidth=10, width=10, command= retourMenu ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fcatalogue.destroy ))





    Label(fcatalogue, text="Nom", bg="green", width = 23).grid(row=2, column=1)
    Label(fcatalogue, text="AnnÃ©e", bg="green", width = 8).grid(row=2, column=2)
    Label(fcatalogue, text="Age Min.", bg="green", width = 8).grid(row=2, column=3)
    Label(fcatalogue, text="Nb Joueur", bg="green", width = 8).grid(row=2, column=4)
    Label(fcatalogue, text="DisponibilitÃ©", bg="green", width = 13).grid(row=2, column=5)
    Label(fcatalogue, text="Auteur", bg="green", width = 13).grid(row=2, column=6)
    Label(fcatalogue, text="Illustrateur", bg="green", width = 15).grid(row=2, column=7)
    Label(fcatalogue, text="Editeur", bg="green", width = 13).grid(row=2, column=8)
    if (modeAdmin):
        Label(fcatalogue, text="Que faire ?", bg="green", width = 73).grid(row=2, column=9, columnspan=6)
    else:
        Label(fcatalogue, text="Que faire ?", bg="green", width = 73).grid(row=2, column=9, columnspan=4)

    numJeu=[0,0,len(Jeux)]
    flecheH = Button(fcatalogue, text="^", command = partial(afficheJeu, numJeu, Jeux, -20), bg="blue", width=5,activebackground="blue").grid(row=3, column=15)
    flecheB = Button(fcatalogue, text="v", command = partial(afficheJeu, numJeu, Jeux, 20), bg="blue", width=5,activebackground="blue").grid(row=22, column=15)
    afficheJeu(numJeu, Jeux)
    
        
    fcatalogue.mainloop()




#EXTENSIONS A PARTIR DU BOUTON "EXTENSION" SUR JEU
def afficheExtensions(idJeu, modeAdmin=False):
    
    def retourCatalogue(mode):
        fextension.destroy()
        return catalogue(mode)

    def lancerEmprunt(i):
        fextension.destroy()
        return formulaireEmprunt(i)

    def lancerReserv(i):
        fextension.destroy()
        return reserver(i)
    
    fextension=Tk()
    fextension.title("Extension(s) du jeu ")
    fextension.grid_columnconfigure(0,weight=1)
    fextension.grid_rowconfigure(20,weight=21)

    p = PanedWindow(fextension, orient = HORIZONTAL, height=100, width=600)
    p.grid(row=1, column=1, columnspan=4)
    p.add(Label(p, text="Bonjour pseudo", bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour au catalogue", bg="orange", activebackground="orange", borderwidth=10, width=20, command=partial(retourCatalogue,modeAdmin)))
    if (modeAdmin):
        p.add(Button(p, text="Ajouter Extension", bg="cyan", activebackground="cyan", borderwidth=10, width=20, command=partial(formulaireExt)))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fextension.destroy ))
    
    if (Jeu.aDesExtensions(idJeu)==False):
        Label(fextension, text="Pas d'extension", bg="white", width=25).grid(row=2)
    else:
        Label(fextension, text="Nom Extension", bg="red", width=30).grid(row=2, column=2) #affiche "Nom Extension" au dessus des noms
        Label(fextension, text="Nom Jeu", bg="red", width=30).grid(row=2, column=1)
        j = Jeu.getExtensions(idJeu)
        k=3
        for i in j:
            Label(fextension, text=str(Extension.getNomExtension(i[0])), bg="white", width=25).grid(row=k, column=2)
            Label(fextension, text=str(Jeu.getNomJeu(Extension.getIdJeu(i[0]))), bg="white", width=25).grid(row=k, column=1)
            Button(fextension, text="Emprunt", command = partial(lancerEmprunt, i[0]),bg="green", width=13,activebackground="green").grid(row=k, column=4)
            Button(fextension, text="Reserv", command = partial(lancerReserv, i[0]),bg="red", width=13,activebackground="red").grid(row=k, column=5)
            Label(fextension, text="QuantitÃ© disponible", bg="red", width=30).grid(row=2, column=3)
            Label(fextension, text=Extension.getNbreTotalExtension(i[0]), bg="white", width=25).grid(row=k,column=3)
            if (modeAdmin):
                Button(fextension, text="Modifier", command = partial(formulaireExt, i[0]), bg="yellow", width=13, activebackground="yellow").grid(row=k, column=6)  
                Button(fextension, text="Supprimer", command=rien, bg="yellow", width=13, activebackground="yellow").grid(row=k, column=7)
            k=k+1
            
    fextension.mainloop()









#AFFICHAGE JEU COTE UTILISATEUR

def ficheJeu(numAdherent, numJeu, modeAdmin=False): #idAdherent + idJeu
    
    def retourCatalogue():
        fficheJeu.destroy()
        return catalogue(numAdherent)

    def lancerEmprunt(i):
        fficheJeu.destroy()
        return formulaireEmprunt(i)

    def lancerReserv(i):
        fficheJeu.destroy()
        return reserver(i)

    def lancerExtension(i):
        fficheJeu.destroy()
        return afficheExtensions(i)

    def lancerExtension(i, mode):
        fficheJeu.destroy()
        return afficheExtensions(i, mode)

    def lanceFormulaireExt(j, i):
        fficheJeu.destroy()
        return formulaireExt(j, i)

    def lanceFormulaireJeu(i):
        fficheJeu.destroy()
        return formulaireJeu(i)
    
    fficheJeu = Tk()
    fficheJeu.title(str(Jeu.getNomJeu(numJeu)))
    fficheJeu.grid_columnconfigure(0,weight=1)
    fficheJeu.grid_rowconfigure(20,weight=21)

    p = PanedWindow(fficheJeu, orient = HORIZONTAL, height=100, width=600)
    p.grid(row=1, column=1, columnspan=3)
    
    p.add(Label(p, text="Bonjour Pseudo", bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour au catalogue", bg="orange", activebackground="orange", borderwidth=10, width=20, command= retourCatalogue ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fficheJeu.destroy ))

   
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

    Label(fficheJeu, text="QuantitÃƒÂ© en stock : ", bg="green", width = 15).grid(row=6, column=1)
    Label(fficheJeu, text=str(Jeu.getQuantiteJeu(numJeu)), bg="orange", width = 15).grid(row=6, column=2)
    
    Label(fficheJeu, text="Auteur : ", bg="green", width = 15).grid(row=7, column=1)
    Label(fficheJeu, text=str(Jeu.getAuteurJeu(numJeu)), bg="orange", width = 15).grid(row=7, column=2)

    Label(fficheJeu, text="Illustrateur : ", bg="green", width = 15).grid(row=8, column=1)
    Label(fficheJeu, text=str(Jeu.getIllustrateurJeu(numJeu)), bg="orange", width = 15).grid(row=8, column=2)
    
    Label(fficheJeu, text="Editeur : ", bg="green", width = 15).grid(row=9, column=1)
    Label(fficheJeu, text=str(Jeu.getEditeurJeu(numJeu)), bg="orange", width = 15).grid(row=9, column=2)

    Label(fficheJeu, text="Synopsis : ", bg="green", width = 15).grid(row=10, column=1)
    Label(fficheJeu, text=str(Jeu.getSynopsisJeu(numJeu)), bg="orange", width = 15).grid(row=10, column=2)

    r = 6
    if (modeAdmin):
        Button(fficheJeu, text="Modifier", command = partial(lanceFormulaireJeu, numJeu),bg="blue", width=13,activebackground="blue").grid(row=r, column=3) #partial(formulaireJeu,Jeux[i][0])
        Button(fficheJeu, text="CrÃƒÂ©er extension", command = partial(lanceFormulaireExt, -1, numJeu),bg="cyan", width=13,activebackground="cyan").grid(row=r+1, column=3)
        r=r+2

    if (Jeu.aDesExtensions(numJeu)):
        Button(fficheJeu, text="Extensions", command = partial(lancerExtension, numJeu, modeAdmin),bg="red", width=13,activebackground="red").grid(row=r, column=3)
        r=r+1
    
    Button(fficheJeu, text="Emprunt", command = partial(lancerEmprunt, numJeu),bg="green", width=13,activebackground="green").grid(row=r, column=3)
    Button(fficheJeu, text="Reserv", command = partial(lancerReserv, numJeu),bg="red", width=13,activebackground="red").grid(row=r+1, column=3)
    r=r+2
    if (modeAdmin):
        Button(fficheJeu, text="Supprimer", command = rien,bg="yellow", width=13,activebackground="red").grid(row=r, column=3)

    fficheJeu.mainloop()













#INTERFACE D'EMPRUNT D'UN JEU

def formulaireEmprunt( numJeu, numAdh=0): #idJeu/extension + idAdherent + boolÃ©en + boolÃ©en
    def CallBackEmprunt(): #Fonction de confirmation DANS la fonction de fenetre.
        if askyesno("Confirmation", "ÃŠtes-vous sÃ»r de vouloir emprunt ce jeu ?"):
            return fEmprunt.quit() #Ferme si "oui"
        else : return

    def retourJeu(numJeu):
        fEmprunt.destroy()
        return ficheJeu(numAdh, numJeu)

    def retourCatalogue():
        fEmprunt.destroy()
        return catalogue()
        
    fEmprunt = Tk()
    fEmprunt.title("Emprunt du jeu " + str(Jeu.getNomJeu(numJeu)))
    fEmprunt.grid_columnconfigure(0,weight=1)
    fEmprunt.grid_rowconfigure(20,weight=21)

    p = PanedWindow(fEmprunt, orient = HORIZONTAL, height=100, width=300)
    p.grid(row=1)
    p.add(Label(p, text="Bonjour Pseudo", bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour au catalogue", bg="orange", activebackground="orange", borderwidth=10, width=20, command= retourCatalogue ))
    p.add(Button(p, text="Retour au jeu", bg="orange", activebackground="orange", borderwidth=10, width=20, command= partial(retourJeu, numJeu)))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fEmprunt.destroy ))
    
    pd = PanedWindow(fEmprunt, orient = HORIZONTAL, height = 20, width = 400)
    pd.grid(row=2)
    pd.add(Label(pd, text="Date de dÃ©but : ", anchor=CENTER, width= 20))
    ddd = Spinbox(pd, from_=1, to=31, width= 5)
    ddm = Spinbox(pd, from_=1, to=12, width= 5)
    ddy = Spinbox(pd, from_=2015, to=2017, width= 8)
    pd.add(ddd)
    pd.add(ddm)
    pd.add(ddy)
    

    pt = PanedWindow(fEmprunt, orient = HORIZONTAL, height = 20, width = 400)
    pt.grid(row=3)
    pt.add(Label(pt, text="Date de fin : ", anchor=CENTER, width= 20))
    dfd = Spinbox(pt, from_=1, to=31, width= 5)
    dfm = Spinbox(pt, from_=1, to=12, width= 5)
    dfy = Spinbox(pt, from_=2015, to=2017, width= 8)
    pt.add(dfd)
    pt.add(dfm)
    pt.add(dfy)
    

    Button(fEmprunt, text ="Emprunter !", command = CallBackEmprunt).grid(row=4)

    fEmprunt.mainloop()

    donneesEmprunt = [ddd.get(), ddm.get(), ddy.get(), dfd.get(), dfm.get(), dfy.get()]

    fEmprunt.destroy()

    return donneesEmprunt















#INTERFACE DE RESERVATION D'UN JEU


def reserver( numJeu,numAdh=0): #idJeu/extension + idAdherent + boolÃ©enJeu (Vrai si l'id en param est un Jeu, Faux si c'est une extension
    # + boolÃ©enExtension (Par dÃ©faut Ã  faux, vrai si on ne rÃ©serve qu'UNE extension)
    def CallBackEmprunt(): #Fonction de confirmation DANS la fonction de fenetre.
        if askyesno("Confirmation", "ÃŠtes-vous sÃ»r de vouloir emprunt ce jeu ?"):
            return fResa.quit() #Ferme si "oui"
        else : return

    def retourJeu(numJeu):
        fResa.destroy()
        return ficheJeu(numAdh, numJeu)

    def retourCatalogue():
        fResa.destroy()
        return catalogue()
        
    fResa = Tk()
    fResa.title("Reservation du jeu " + str(Jeu.getNomJeu(numJeu)))
    fResa.grid_columnconfigure(0,weight=1)
    fResa.grid_rowconfigure(20,weight=21)

    p = PanedWindow(fResa, orient = HORIZONTAL, height=100, width=300)
    p.grid(row=1)
    p.add(Label(p, text="Bonjour Pseudo", bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour au catalogue", bg="orange", activebackground="orange", borderwidth=10, width=20, command= retourCatalogue ))
    p.add(Button(p, text="Retour au jeu", bg="orange", activebackground="orange", borderwidth=10, width=20, command= partial(retourJeu, numJeu)))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fResa.destroy ))
    
    pd = PanedWindow(fResa, orient = HORIZONTAL, height = 20, width = 400)
    pd.grid(row=2)
    pd.add(Label(pd, text="Date de dÃ©but : ", anchor=CENTER, width= 20))
    ddd = Spinbox(pd, from_=1, to=31, width= 5)
    ddm = Spinbox(pd, from_=1, to=12, width= 5)
    ddy = Spinbox(pd, from_=2015, to=2017, width= 8)
    pd.add(ddd)
    pd.add(ddm)
    pd.add(ddy)
    

    pt = PanedWindow(fResa, orient = HORIZONTAL, height = 20, width = 400)
    pt.grid(row=3)
    pt.add(Label(pt, text="Date de fin : ", anchor=CENTER, width= 20))
    dfd = Spinbox(pt, from_=1, to=31, width= 5)
    dfm = Spinbox(pt, from_=1, to=12, width= 5)
    dfy = Spinbox(pt, from_=2015, to=2017, width= 8)
    pt.add(dfd)
    pt.add(dfm)
    pt.add(dfy)
    

    Button(fResa, text ="Reserver !", command = CallBackEmprunt).grid(row=4)

    fResa.mainloop()

    donneesEmprunt = [ddd.get(), ddm.get(), ddy.get(), dfd.get(), dfm.get(), dfy.get()]

    fResa.destroy()

    return donneesEmprunt















#MODIFICATION/CREATION D'UN ADHERENT


def formulaireAdherent(numAdh=0): #numAdhÃ©rent + boolÃ©en pour savoir si mode Admin ou pas + boolÃ©en savoir si crÃ©ation ou modification
    
    fAdh = Tk()
    fAdh.title("Profil de "+Adherent.getPrenom(numAdh))

    def CallBackFormulaireAdh(num): #Fonction de confirmation DANS la fonction de fenetre.
        if (askyesno("Confirmation", "Enregister ces informations ?")):
            return fAdh.quit() #Ferme si "oui"
        else:
            fAdh.destroy()
            return menu(num)


    p = PanedWindow(fAdh, orient = HORIZONTAL, height=100, width=1000)
    p.grid(row=1, column=1, columnspan=4)
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(numAdh), bg="white", anchor=CENTER, width=20))
    p.add(Button(p, text="Retour au menu", bg="orange", activebackground="orange", borderwidth=10, width=20, command= partial(CallBackFormulaireAdh, numAdh)))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fAdh.destroy ))
    
    Label(fAdh, text="Profil", font=("Helvetica", 30), height=4).grid(row=2, column=1, columnspan=4)
    
    Label(fAdh, text="Nom : ").grid(row=3, column=1, columnspan=2)
    nomAdh = StringVar()
    nomAdh.set(Adherent.getNom(numAdh))
    entryNomAdh = Entry(fAdh,textvariable=nomAdh,width=40)
    entryNomAdh.grid(row=3, column=3, columnspan=2)

    Label(fAdh, text="PrÃ©nom : ").grid(row=4, column=1, columnspan=2)
    prenomAdh = StringVar()
    prenomAdh.set(Adherent.getPrenom(numAdh))
    entryPrenomAdh = Entry(fAdh,textvariable=prenomAdh,width=40)
    entryPrenomAdh.grid(row=4, column=3, columnspan=2)


    Label(fAdh, text="Pseudo : ").grid(row=5, column=1, columnspan=2)
    pseudoAdh = StringVar()
    pseudoAdh.set(Adherent.getPseudo(numAdh))
    entryPseudoAdh = Entry(fAdh,textvariable=pseudoAdh,width=40)
    entryPseudoAdh.grid(row=5, column=3, columnspan=2)

    Label(fAdh, text="Mot de passe : ").grid(row=6, column=1, columnspan=2)
    mdpAdh = StringVar()
    mdpAdh.set(Adherent.getMotDePasse(numAdh))
    entryMdpAdh = Entry(fAdh,textvariable=mdpAdh,width=40,show="*")
    entryMdpAdh.grid(row=6, column=3, columnspan=2)

      

    Label(fAdh, text="Date de naissance : ").grid(row=7, column=1)
    
    dnaAdh = StringVar()
    dnaAdh.set(Adherent.getNaissance(numAdh)[0:4])
    dnmAdh = StringVar()
    dnmAdh.set(Adherent.getNaissance(numAdh)[5:7])
    dnjAdh = StringVar()
    dnjAdh.set(Adherent.getNaissance(numAdh)[8:10])
    
    entryDnjAdh = Spinbox(fAdh, textvariable=dnjAdh, from_=1, to =31)
    entryDnjAdh.grid(row=7, column=2)

    entryDnmAdh = Spinbox(fAdh, textvariable=dnmAdh, from_=1, to =12)
    entryDnmAdh.grid(row=7, column=3)

    entryDnaAdh = Spinbox(fAdh, textvariable=dnaAdh, from_=1900, to=datetime.date.today().year)
    entryDnaAdh.grid(row=7, column=4)


    Label(fAdh, text="Adresse : ").grid(row=8,column=1, columnspan=2)
    adrAdh = StringVar()
    adrAdh.set(Adherent.getAdresse(numAdh))
    entryAdrAdh = Entry(fAdh,textvariable=adrAdh,width=40)
    entryAdrAdh.grid(row=8, column=3, columnspan=2)

    Label(fAdh, text="Code postal : ").grid(row=9, column=1, columnspan=2)
    cpAdh = StringVar()
    cpAdh.set(Adherent.getCodePostal(numAdh))
    entryCpAdh = Entry(fAdh,textvariable=cpAdh,width=40)
    entryCpAdh.grid(row=9, column=3, columnspan=2)

    Label(fAdh, text="Ville : ").grid(row=10, column=1, columnspan=2)
    villeAdh = StringVar()
    villeAdh.set(Adherent.getVille(numAdh))
    entryVilleAdh = Entry(fAdh,textvariable=villeAdh,width=40)
    entryVilleAdh.grid(row=10, column=3, columnspan=2)

    Label(fAdh, text="NumÃ©ro : ").grid(row=11, column=1, columnspan=2)
    numeroAdh = StringVar()
    numeroAdh.set(Adherent.getNumTelephone(numAdh))
    entryNumAdh = Entry(fAdh,textvariable=numeroAdh,width=40)
    entryNumAdh.grid(row=11, column=3, columnspan=2)

    Label(fAdh, text="Adresse Mail : ").grid(row=12, column=1, columnspan=2)
    mailAdh = StringVar()
    mailAdh.set(Adherent.getMail(numAdh))
    entryMailAdh = Entry(fAdh,textvariable=mailAdh,width=40)
    entryMailAdh.grid(row=12, column=3, columnspan=2)    

   
    #admAdh = Checkbutton(FJ, text="Est-il empruntable?", variable = Empbool)
    
    Button(fAdh, text="Enregistrer", command = partial(CallBackFormulaireAdh,numAdh)).grid(row=13, column=1, columnspan=4)
   
    #Lancement de la fenetre
    fAdh.mainloop()
    #On recupere les donnÃƒÂ©es de chaque entrÃƒÂ©e.
    #DonneesJeu = (NJI.get(), AnJI.get(), AgJI.get(),NbJI.get(), QJI.get(),AJI.get(),IJI.get(),EJI.get(), bool(Empbool.get()), SJI.get())
    #Enfin on detruit la fenetre
    fAdh.destroy()

    #Mettre Ã  jour les donnÃ©es
    
    menu(1)



def connexion2():
    def verificationConnexion():
        idAd =  Adherent.getId(pseudo.get())
        if idAd == None:
            print("Mauvais pseudo")
        else:
            if Adherent.compareMDP(idAd,mdp.get()) == False:
                print("Mauvais MDP")
            else:
                print("Connexion reussi")

    #creation de la fÃªnetre principle
    fenetre = Tk()
    fenetre.title('Ludotheque')

    framePrincip = Frame(fenetre)
    framePrincip.pack(padx = 30, pady = 30)

    labelTitre = Label(framePrincip, text = "Connexion")
    labelTitre.pack(padx = 50, pady = 10)

    #pseudo
    framePseudo = Frame(framePrincip)
    framePseudo.pack(pady = 20)

    labPseudo = Label(framePseudo, text = "Pseudo")
    labPseudo.pack(side = "left", padx = 5, pady = 5)

    #Saisie du pseudo
    pseudo = StringVar()
    champPseudo = Entry(framePseudo, textvariable = pseudo, bg ='bisque', fg='maroon')
    champPseudo.focus_set()
    champPseudo.pack(side = "left", padx = 5, pady = 5)


    #MDP
    frameMDP = Frame(framePrincip)
    frameMDP.pack(pady = 20)

    labMdp = Label(frameMDP, text = "Mot de passe ")
    labMdp.pack(side = "left", padx = 5, pady = 5)

    #Saisie du MDP
    mdp = StringVar()
    champMdp = Entry(frameMDP, textvariable = mdp, show='*', bg ='bisque', fg='maroon')
    champMdp.pack(side = "left", padx = 5, pady = 5)


    #Bouton Valider
    Bouton = Button(framePrincip, text ='Valider', command = verificationConnexion)
    Bouton.pack(side = "right", padx = 5, pady = 5)

    fenetre.mainloop()






####AFFICHAGE DES EMPRUNTS

def catalogueEmprunt(numAdherent=0, Emprunt=Emprunt.getAllEmprunts(), modeAdmin=False): #idAdherent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fcatalogue.after(1000,maj)

    def retourMenu():
        fcatalogue.destroy()
        return menu(numAdherent)

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
            if (Emprunts[i][5]==0):
                Label(fcatalogue, text=str("EN COURS"), bg="cyan", width = 10).grid(row=j, column=7)
            else:
                Label(fcatalogue, text=str("RENDU"), bg="orange", width = 10).grid(row=j, column=7)
            if (modeAdmin):
                Button(fcatalogue, text="Modifier", command = rien,bg="blue", width=13,activebackground="blue").grid(row=j, column=8)

            if (modeAdmin):
                Button(fcatalogue, text="Supprimer", command = rien,bg="yellow", width=13,activebackground="red").grid(row=j, column=9)
            j=j+1

    
    fcatalogue = Tk()
    fcatalogue.title("Listes des emprunts")
    fcatalogue.grid_columnconfigure(0,weight=1)
    fcatalogue.grid_rowconfigure(20,weight=21)
    
    p = PanedWindow(fcatalogue, orient = HORIZONTAL, height=100, width=1000)
    p.grid(row=1, column=1, columnspan=11)
     
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=30))
    maj()
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(numAdherent), bg="white", anchor=CENTER, width=10))
    if (modeAdmin):
        p.add(Button(p, text="Ajouter un emprunt", bg="cyan", activebackground="cyan", borderwidth=10, width=10, command= rien))#partial(formulaireJeu,numAdh)))
    p.add(Button(p, text="Retour au menu principal", bg="orange", activebackground="orange", borderwidth=10, width=10, command= retourMenu ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fcatalogue.destroy ))

    Label(fcatalogue, text="AdhÃ©rent", bg="green", width = 25).grid(row=2, column=1)
    Label(fcatalogue, text="Jeu", bg="green", width = 25).grid(row=2, column=2)
    Label(fcatalogue, text="Extension", bg="green", width = 20).grid(row=2, column=3)
    Label(fcatalogue, text="Date du dÃ©but", bg="green", width = 15).grid(row=2, column=4)
    Label(fcatalogue, text="Date de rendu", bg="green", width = 15).grid(row=2, column=5)
    Label(fcatalogue, text="DurÃ©e prÃ©vu", bg="green", width = 10).grid(row=2, column=6)
    Label(fcatalogue, text="Emprunt en cours", bg="blue", width = 13).grid(row=2, column=7)
    
    if (modeAdmin):
        Label(fcatalogue, text="Que faire ?", bg="green", width = 24).grid(row=2, column=8, columnspan=2)

    numEmprunt=[0,0,len(Emprunt)]
    flecheH = Button(fcatalogue, text="^", command = partial(afficheEmprunts, numEmprunt, Emprunt, -20), bg="blue", width=5,activebackground="blue").grid(row=3, column=11)
    flecheB = Button(fcatalogue, text="v", command = partial(afficheEmprunts, numEmprunt, Emprunt, 20), bg="blue", width=5,activebackground="blue").grid(row=22, column=11)
    afficheEmprunts(numEmprunt, Emprunt)
    
        
    fcatalogue.mainloop()
