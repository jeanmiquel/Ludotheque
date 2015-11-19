Class Extension:

 def __init__(self, id_Ext=int, nameExt="", quantiteExt=int, jeuExt= Jeu):
      self.id_Ext = id_Ext
      self.nameExt = nameExt
      self.quantiteExt = quantiteExt
      self.jeuExt = jeuExt

 def getId_Ext(self):
      return self.id_Ext

 def getNameExt(self):
      return self.nameExt

 def getQuantiteExt(self):
      return self.quantiteExt

 def getJeuExt(self):
      return self.jeuExt

 def estDispo(self):
      return (self.quantiteExt != 0)

 def creerExtension(name: string, jeu: Jeu):
      return new Extension(,name, 1, jeu)

 def ajoutExemplaireExt(self):
      self.quantiteExt = self.quantiteExt + 1
      return self
