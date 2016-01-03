from Tkinter import *
from tkMessageBox import *
from datetime import *
import datetime
from functools import partial
from Jeu import Jeu
from Adherent import Adherent






#FORMULAIRE DE JEU

def formulaireJeu():
    """Retourne un tuple tirer d'un formulaire.
    (nomJeu, anneeJeu, ageJeu, nbJoueurJeu, quantiteJeu, auteurJeu, illustrateurJeu,
    editeurJeu, estEmpruntableJeu, synopsisJeu)"""
    FJ = Tk()
    def CallBackFJ(): #Fonction de confirmation DANS la fonction de fenetre.
        if askyesno("Confirmation", "Enregister le jeu ?"):
            return FJ.quit() #Ferme si "oui"
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
    nomJeu.set("Nom du jeu")
    NJI = Entry(FJ,textvariable=nomJeu,width=40)
    NJI.pack()
    #Annee Jeu (graduation)
    AnJ.pack()
    AnJI = Spinbox(FJ, from_=1960, to = date.today().year)
    AnJI.pack()
    #Age joueurs(Champs Ã  remplir)
    AgJ.pack()
    AgJI = Spinbox(FJ, from_=0, to = 20)
    AgJI.pack()
    #Nombre de joueurs (graduation)
    NbJ.pack()
    nbJoueurJeu="00-00"
    NbJI = Entry(FJ, textvariable=nbJoueurJeu, width=45)
    NbJI.pack()
    #Quantite d'exemplaire du jeu (gradutation)
    QJ.pack()
    QJI = Spinbox(FJ, from_=0, to=999)
    QJI.pack()
    #Auteur du jeu (champs Ã  remplir)
    AJ.pack()
    auteurJeu="Auteur du jeu"
    AJI = Entry(FJ, textvariable=auteurJeu, width = 45)
    AJI.pack()
    #Illustrateur du jeu (champs Ã  remplir)
    IJ.pack()
    illustrateurJeu="Illustrateur du jeu"
    IJI = Entry(FJ, textvariable=illustrateurJeu, width = 45)
    IJI.pack()
    #Editeur du jeu (champs Ã  remplir)
    EJ.pack()
    editeurJeu="Editeur du jeu"
    EJI = Entry(FJ, textvariable=editeurJeu, width = 45)
    EJI.pack()
    #Empruntable ou non ? (case Ã  cocher)
    Emp.pack()
    Empbool = IntVar()
    EmpI = Checkbutton(FJ, text="Est-il empruntable?", variable = Empbool)
    EmpI.pack()
    #Synospis du jeu (Champs Ã  remplir)
    SJ.pack()
    synopsisJeu = "Description sommaire du jeu."
    SJI = Entry(FJ, textvariable=synopsisJeu, width = 45)
    SJI.pack()
    #Fin : Confirmation de l'ajout du jeu
    AddJ.pack()
    AddJI = Button(FJ, text="Confirmer", command = CallBackFJ)
    AddJI.pack()
    #Lancement de la fenetre
    FJ.mainloop()
    #On recupere les donnÃ©es de chaque entrÃ©e.
    DonneesJeu = (NJI.get(), AnJI.get(), AgJI.get(),NbJI.get(),
                  QJI.get(),AJI.get(),IJI.get(),EJI.get(), bool(Empbool.get()), SJI.get())
    #Enfin on detruit la fenetre
    FJ.destroy()
    return DonneesJeu










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
    fconnexion.title("Connexion à la Ludothéque")
    
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
        
def menu(numAdh=0): #numIdAdhérent
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
        return catalogue(numAdh)

    def LanceProfil():
        fmenu.destroy()
        return formulaireAdherent(numAdh)
        
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
    pt.add(Button(pt, text="Mes emprunts et réservation", command = rien, bg="green", width=38,activebackground="green", borderwidth=10))
    pt.add(Button(pt, text="Bonus", command = rien,bg="blue", width=38,activebackground="blue", borderwidth=10))
    
    fmenu.mainloop()

    










#PANNEAU D'ADMINISTRATION


def panneauAdmin(numAdh=0): #numIdAdhérent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fpanneauadmin.after(1000,maj)

    def retourMenu():
        fpanneauadmin.destroy()
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
    pd.add(Button(pd, text="Gestion des Adhérents", width=38, command = rien, bg="yellow", activebackground="yellow", borderwidth=10))
    pd.add(Button(pd, text="Gestion des Jeux", width=38, command = rien, bg="red", activebackground="red", borderwidth=10))


    pt = PanedWindow(fpanneauadmin,orient=HORIZONTAL, height=350, width=600)
    pt.grid(row=3)
    pt.add(Button(pt, text="Gestion des Emprunts", command = rien, bg="green", width=38,activebackground="green", borderwidth=10))
    pt.add(Button(pt, text="Gestion des réservations", command = rien,bg="blue", width=38,activebackground="blue", borderwidth=10))

    fpanneauadmin.mainloop()










def test(): #tuple de jeu + numIdAdhérent
    def maj():
        # on arrive ici toutes les 1000 ms
        t=datetime.datetime.today()
        heure.set(t.strftime('%m/%d/%Y  %H:%M:%S'))
        fpanneauadmin.after(1000,maj)

    def retourMenu():
        fcatalogue.destroy()
        return menu()

    def afficheJeu():
        fcatalogue.destroy()
        return ficheJeu()
    
    def lancerEmprunt(i):
        fcatalogue.destroy()
        return emprunter(i)
    
    fcatalogue = Tk()
    fcatalogue.title("Les jeux de la ludothèque")
    fcatalogue.grid_columnconfigure(0,weight=1)
    fcatalogue.grid_rowconfigure(20,weight=21)
    
    """p = PanedWindow(fcatalogue, orient = HORIZONTAL, height=100, width=800)
    p.grid(row=1)
     
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=30))
    maj()
    
    p.add(Label(p, text="Bonjour Pseudo", bg="white", anchor=CENTER, width=30))
    p.add(Button(p, text="Retour au menu principal", bg="orange", activebackground="orange", borderwidth=10, width=30, command= retourMenu ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fcatalogue.destroy ))"""
    

    #pTitre = PanedWindow(fcatalogue, orient = HORIZONTAL, height = 30, width=1150)
    #pTitre.grid(row=2)
    #pTitre.add(
    Label(fcatalogue, text="Nom", bg="green", width = 15).grid(row=2, column=1)
    Label(fcatalogue, text="Année", bg="green", width = 15).grid(row=2, column=2)
    Label(fcatalogue, text="Age Min.", bg="green", width = 15).grid(row=2, column=3)
    Label(fcatalogue, text="Nb Joueur", bg="green", width = 15).grid(row=2, column=4)
    Label(fcatalogue, text="Disponibilité", bg="green", width = 15).grid(row=2, column=5)
    Label(fcatalogue, text="Auteur", bg="green", width = 15).grid(row=2, column=6)
    Label(fcatalogue, text="Illustrateur", bg="green", width = 15).grid(row=2, column=7)
    Label(fcatalogue, text="Editeur", bg="green", width = 15).grid(row=2, column=8)
    Label(fcatalogue, text="Action", bg="green", width = 15).grid(row=2, column=9)
    Label(fcatalogue, text="Action", bg="green", width = 15).grid(row=2, column=10)
    Label(fcatalogue, text="Action", bg="green", width = 15).grid(row=2, column=11)

    scrollbar = Scrollbar(fcatalogue)
    scrollbar.grid(row=3, column=12)
    listeNom = Listbox(fcatalogue, yscrollcommand=scrollbar.set)
    listeAnnee = Listbox(fcatalogue, yscrollcommand=scrollbar.set)
    listeAge = Listbox(fcatalogue, yscrollcommand=scrollbar.set)
    listeNbj = Listbox(fcatalogue, yscrollcommand=scrollbar.set)
    listeDispo = Listbox(fcatalogue, yscrollcommand=scrollbar.set)
    listeAuteur = Listbox(fcatalogue, yscrollcommand=scrollbar.set)
    listeIllus = Listbox(fcatalogue, yscrollcommand=scrollbar.set)
    listeEditeur = Listbox(fcatalogue, yscrollcommand=scrollbar.set)
    listeDetail = Listbox(fcatalogue, yscrollcommand=scrollbar.set)
    listeEmprunt = Listbox(fcatalogue, yscrollcommand=scrollbar.set)
    listeReserv = Listbox(fcatalogue, yscrollcommand=scrollbar.set)

    for i in range(3,200):
        #p = PanedWindow(fcatalogue, orient = HORIZONTAL, height = 20, width=1150)
        #p.grid(row=i)
        """p.add(Label(p, text="Nom", bg="orange", width = 15))
        p.add(Label(p, text="Année", bg="orange", width = 15))
        p.add(Label(p, text="Age Min.", bg="orange", width = 15))
        p.add(Label(p, text="Nb Joueur", bg="orange", width = 15))
        p.add(Label(p, text="Disponibilité", bg="orange", width = 15))
        p.add(Label(p, text="Auteur", bg="orange", width = 15))
        p.add(Label(p, text="Illustrateur", bg="orange", width = 15))
        p.add(Label(p, text="Editeur", bg="orange", width = 15))
        p.add(Button(p, text="Détail", command = afficheJeu,bg="blue", width=5,activebackground="blue"))
        p.add(Button(p, text="Emprunt", command = partial(lancerEmprunt, i),bg="green", width=5,activebackground="green"))
        p.add(Button(p, text="Reserv", command = rien,bg="red", width=5,activebackground="red"))"""
        listeNom.insert(END, "Nom")
        listeAnnee.insert(END, 2000+i)
        listeAge.insert(END, 8+i)
        listeNbj.insert(END, "12-18")
        listeDispo.insert(END, "DISPO")
        listeAuteur.insert(END, "Martin")
        listeIllus.insert(END, "JP")
        listeEditeur.insert(END, "MB")
        listeDetail.insert(END, "FicheJeu")
        listeEmprunt.insert(END, "Emprunt")
        listeReserv.insert(END, "Reserve")

    def yview(h, i, j=-1):
        if (j==-1):
            listeNom.yview(h, i) 
            listeAge.yview(h, i)
            listeNbj.yview(h, i)
            listeDispo.yview(h, i)
            listeAuteur.yview(h, i)
            listeIllus.yview(h, i)
            listeEditeur.yview(h, i)
            listeDetail.yview(h, i)
            listeEmprunt.yview(h, i)
            listeReserv.yview(h, i)
            listeAnnee.yview(h, i)
        else:
            listeNom.yview(h, i, j) 
            listeAge.yview(h, i, j)
            listeNbj.yview(h, i, j)
            listeDispo.yview(h, i, j)
            listeAuteur.yview(h, i, j)
            listeIllus.yview(h, i, j)
            listeEditeur.yview(h, i, j)
            listeDetail.yview(h, i, j)
            listeEmprunt.yview(h, i, j)
            listeReserv.yview(h, i, j)
            listeAnnee.yview(h, i,j)

    listeNom.grid(row=3, column=1)
    listeAnnee.grid(row=3, column=2)
    listeAge.grid(row=3, column=3)
    listeNbj.grid(row=3, column=4)
    listeDispo.grid(row=3, column=5)
    listeAuteur.grid(row=3, column=6)
    listeIllus.grid(row=3, column=7)
    listeEditeur.grid(row=3, column=8)
    listeDetail.grid(row=3, column=9)
    listeEmprunt.grid(row=3, column=10)
    listeReserv.grid(row=3, column=11)
    
    scrollbar.config(command= yview)
        
    fcatalogue.mainloop()










#CATALOGUE DES JEUX


def catalogue(numAdherent=0, Jeux=Jeu.getAllJeu()): #idAdherent
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
        return ficheJeu(i)
    
    def lancerEmprunt(i):
        fcatalogue.destroy()
        return emprunter(i)

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
            Button(fcatalogue, text="Détail", command = partial(afficheFicheJeu,Jeux[i][0]) ,bg="blue", width=13,activebackground="blue").grid(row=j, column=9)
            Button(fcatalogue, text="Extensions", command = rien,bg="red", width=13,activebackground="red").grid(row=j, column=10)
            Button(fcatalogue, text="Emprunt", command = partial(lancerEmprunt, i),bg="green", width=13,activebackground="green").grid(row=j, column=11)
            Button(fcatalogue, text="Reserv", command = rien,bg="red", width=13,activebackground="red").grid(row=j, column=12)
            j=j+1

    
    fcatalogue = Tk()
    fcatalogue.title("Les jeux de la ludothèque")
    fcatalogue.grid_columnconfigure(0,weight=1)
    fcatalogue.grid_rowconfigure(20,weight=21)
    
    p = PanedWindow(fcatalogue, orient = HORIZONTAL, height=100, width=800)
    p.grid(row=1, column=1, columnspan=11)
     
    heure = StringVar()
    p.add(Label(p, textvariable=heure, bg="red", anchor=CENTER,width=30))
    maj()
    
    p.add(Label(p, text="Bonjour "+Adherent.getPseudo(numAdherent), bg="white", anchor=CENTER, width=30))
    p.add(Button(p, text="Retour au menu principal", bg="orange", activebackground="orange", borderwidth=10, width=30, command= retourMenu ))
    p.add(Button(p, text="Quitter", bg="white", activebackground="black", borderwidth=10, width=10, command = fcatalogue.destroy ))

    Label(fcatalogue, text="Nom", bg="green", width = 25).grid(row=2, column=1)
    Label(fcatalogue, text="Année", bg="green", width = 10).grid(row=2, column=2)
    Label(fcatalogue, text="Age Min.", bg="green", width = 10).grid(row=2, column=3)
    Label(fcatalogue, text="Nb Joueur", bg="green", width = 10).grid(row=2, column=4)
    Label(fcatalogue, text="Disponibilité", bg="green", width = 15).grid(row=2, column=5)
    Label(fcatalogue, text="Auteur", bg="green", width = 15).grid(row=2, column=6)
    Label(fcatalogue, text="Illustrateur", bg="green", width = 15).grid(row=2, column=7)
    Label(fcatalogue, text="Editeur", bg="green", width = 15).grid(row=2, column=8)
    Label(fcatalogue, text="Action", bg="green", width = 15).grid(row=2, column=9)
    Label(fcatalogue, text="Action", bg="green", width = 15).grid(row=2, column=10)
    Label(fcatalogue, text="Action", bg="green", width = 15).grid(row=2, column=11)
    Label(fcatalogue, text="Action", bg="green", width = 15).grid(row=2, column=12)

    numJeu=[0,0,len(Jeux)]
    flecheH = Button(fcatalogue, text="^", command = partial(afficheJeu, numJeu, Jeux, -20), bg="blue", width=5,activebackground="blue").grid(row=3, column=13)
    flecheB = Button(fcatalogue, text="v", command = partial(afficheJeu, numJeu, Jeux, 20), bg="blue", width=5,activebackground="blue").grid(row=22, column=13)
    afficheJeu(numJeu, Jeux)
    
        
    fcatalogue.mainloop()















#AFFICHAGE JEU COTE UTILISATEUR

def ficheJeu(numJeu): #idAdherent + idJeu
    
    def retourCatalogue():
        fficheJeu.destroy()
        return catalogue()

    def lancerEmprunt(i):
        fficheJeu.destroy()
        return emprunter(i)
    
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

    Label(fficheJeu, text="Année de parution : ", bg="green", width = 15).grid(row=3, column=1)
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

    Label(fficheJeu, text="Quantité en stock : ", bg="green", width = 15).grid(row=6, column=1)
    Label(fficheJeu, text=str(Jeu.getQuantiteJeu(numJeu)), bg="orange", width = 15).grid(row=6, column=2)
    
    Label(fficheJeu, text="Auteur : ", bg="green", width = 15).grid(row=7, column=1)
    Label(fficheJeu, text=str(Jeu.getAuteurJeu(numJeu)), bg="orange", width = 15).grid(row=7, column=2)

    Label(fficheJeu, text="Illustrateur : ", bg="green", width = 15).grid(row=8, column=1)
    Label(fficheJeu, text=str(Jeu.getIllustrateurJeu(numJeu)), bg="orange", width = 15).grid(row=8, column=2)
    
    Label(fficheJeu, text="Editeur : ", bg="green", width = 15).grid(row=9, column=1)
    Label(fficheJeu, text=str(Jeu.getEditeurJeu(numJeu)), bg="orange", width = 15).grid(row=9, column=2)

    Label(fficheJeu, text="Synopsis : ", bg="green", width = 15).grid(row=10, column=1)
    Label(fficheJeu, text=str(Jeu.getSynopsisJeu(numJeu)), bg="orange", width = 15).grid(row=10, column=2)

    Label(fficheJeu, text="Action", bg="green", width = 15).grid(row=7, column=3)
    Button(fficheJeu, text="Voir ses extensions", command = rien,bg="green", width=15,activebackground="green").grid(row=8, column=3)
    Button(fficheJeu, text="Emprunt", command = partial(lancerEmprunt, numJeu),bg="green", width=15,activebackground="green").grid(row=9, column=3)
    Button(fficheJeu, text="Reserv", command = rien,bg="red", width=15,activebackground="red").grid(row=10, column=3)

    fficheJeu.mainloop()













#INTERFACE D'EMPRUNT D'UN JEU

def emprunter(numAdh=0, numJeu=0): #idJeu/extension + idAdherent + booléen + booléen
    def CallBackEmprunt(): #Fonction de confirmation DANS la fonction de fenetre.
        if askyesno("Confirmation", "Êtes-vous sûr de vouloir emprunt ce jeu ?"):
            return fEmprunt.quit() #Ferme si "oui"
        else : return

    def retourJeu(numJeu):
        fEmprunt.destroy()
        return ficheJeu(numJeu)

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
    pd.add(Label(pd, text="Date de début : ", anchor=CENTER, width= 20))
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


def reserver(numJeu): #idJeu/extension + idAdherent + booléenJeu (Vrai si l'id en param est un Jeu, Faux si c'est une extension
    # + booléenExtension (Par défaut à faux, vrai si on ne réserve qu'UNE extension)
    def CallBackEmprunt(): #Fonction de confirmation DANS la fonction de fenetre.
        if askyesno("Confirmation", "Êtes-vous sûr de vouloir emprunt ce jeu ?"):
            return fResa.quit() #Ferme si "oui"
        else : return

    def retourJeu(numJeu):
        fResa.destroy()
        return ficheJeu(numJeu)

    def retourCatalogue():
        fResa.destroy()
        return catalogue()
        
    fResa = Tk()
    fResa.title("Emprunt du jeu " + str(numJeu))
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
    pd.add(Label(pd, text="Date de début : ", anchor=CENTER, width= 20))
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
    

    Button(fResa, text ="Emprunter !", command = CallBackEmprunt).grid(row=4)

    fResa.mainloop()

    donneesEmprunt = [ddd.get(), ddm.get(), ddy.get(), dfd.get(), dfm.get(), dfy.get()]

    fResa.destroy()

    return donneesEmprunt















#MODIFICATION/CREATION D'UN ADHERENT


def formulaireAdherent(numAdh=0): #numAdhérent + booléen pour savoir si mode Admin ou pas + booléen savoir si création ou modification
    
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

    Label(fAdh, text="Prénom : ").grid(row=4, column=1, columnspan=2)
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

    Label(fAdh, text="Numéro : ").grid(row=11, column=1, columnspan=2)
    numAdh = StringVar()
    numAdh.set("0000")#Adherent.getNumTelephone(numAdh))
    entryNumAdh = Entry(fAdh,textvariable=numAdh,width=40)
    entryNumAdh.grid(row=11, column=3, columnspan=2)

    Label(fAdh, text="Adresse Mail : ").grid(row=12, column=1, columnspan=2)
    mailAdh = StringVar()
    mailAdh.set("lol@lol")#Adherent.getMail(numAdh))
    entryMailAdh = Entry(fAdh,textvariable=mailAdh,width=40)
    entryMailAdh.grid(row=12, column=3, columnspan=2)    

   
    #admAdh = Checkbutton(FJ, text="Est-il empruntable?", variable = Empbool)
    
    Button(fAdh, text="Enregistrer", command = partial(CallBackFormulaireAdh,numAdh)).grid(row=13, column=1, columnspan=4)
   
    #Lancement de la fenetre
    fAdh.mainloop()
    #On recupere les donnÃ©es de chaque entrÃ©e.
    #DonneesJeu = (NJI.get(), AnJI.get(), AgJI.get(),NbJI.get(), QJI.get(),AJI.get(),IJI.get(),EJI.get(), bool(Empbool.get()), SJI.get())
    #Enfin on detruit la fenetre
    fAdh.destroy()

    #Mettre à jour les données
    
    menu(1)

