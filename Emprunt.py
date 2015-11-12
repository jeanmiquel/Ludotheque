import Jeu
import Adherent
import EnsEmprunts

class Emprunt:

  def __init__(self, emprunt_id=None, Jeu_id=None, user_id=None, dateDebut="", dateFin=""):
    
      self.emprunt_id = emprunt_id
      self.Jeu_id = Jeu_id
      self.user_id = user_id
      self.dateDebut = dateDebut
      self.dateFin = dateFin
      
#### GETTERS #####

  def get_emprunt_id(self):
    return self.emprunt_id
    
  def get_user_id(self):
    return self.user_id
    
  def get_Jeu_id(self):
    return self.Jeu_id
    
  def get_dateDebut(self):
    return self.dateDebut
    
  def get_DateFin(self):
    return self.dateFin
    
  def get_Duree(self):
    return (self.dateFin - self.dateDebut)

#### FONCTIONS ####

  def estEnRetard(e: Emprunt):
    return (#currentDate > e.get_DateFin)
    
  def rendre(self):                                     #supprime l'emprunt de l'ensemble des emprunts
    EnsEmprunt.rendre(self)
  
