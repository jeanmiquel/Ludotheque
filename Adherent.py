class Adherent:

    def __init__(self,user_id=None,name="",pseudo="",password="",numTel="",adresse="",abonnementValide=False,empruntEnCours=False,reservationEnCours=False,nbRetard=0):
        
        self.user_id = user_id
        self.name = name
        self.pseudo = pseudo
        self.password = password
        self.numTel = numTel
        self.adresse = adresse
        self.abonnementValide = abonnementValide
        self.empruntEnCours = empruntEnCours
        self.reservationEnCours = reservationEnCours
        self.nbRetard = nbRetard
        self.abonnementValide = abonnementValide
        self.empruntEnCours = empruntEnCours
        self.reservationEnCours = reservationEnCours
        self.nbRetard = nbRetard

##### GETTERS ########

    def get_user_id(self):
        return self.user_id
    def get_name(self):
        return self.name
    def get_pseudo(self):
        return self.pseudo
    def get_password(self):
        return self.password
    def get_numTel(self):
        return self.numTel
    def get_adresse(self):
        return self.adresse
    def get_abonnementValide(self):
        return self.abonnementValide
    def get_empruntEnCours(self):
        return self.empruntEnCours
    def get_reservationEnCours(self):
        return self.reservationEnCours
    def get_nbRetard(self):
        return self.nbRetard
        
        
##### SETTERS #####

    def set_name(self, name):
        self.name = name
    def set_pseudo(self, pseudo):
        self.pseudo = pseudo
    def set_password(self, password):
        self.password = password
    def set_numTel(self, numTel):
        self.numTel = numTel
    def set_adresse(self, adresse):
        self.adresse = adresse
    def get_abonnementValide(self):
        return self.abonnementValide
    def get_empruntEnCours(self):
        return self.empruntEnCours
    def get_reservationEnCours(self):
        return self.reservationEnCours
    def get_nbRetard(self):
        return self.nbRetard
