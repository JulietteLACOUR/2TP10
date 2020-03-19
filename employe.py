from abc import ABC, abstractmethod

from salarie import Salarie

class Employe(Salarie):

    def __init__(self, nom = "Alain", prenom = "LACOUR", salaire = 10, id = 0, anneeEmbauche = 1999, nbJdT = 300):
        Salarie.__init__(self, nom, prenom, salaire, id)
        self._AE = anneeEmbauche
        self._NbJdT = nbJdT

    @abstractmethod
    def afficher(self):
        pass
