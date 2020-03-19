from abc import ABC, abstractmethod

from employe import *

class Ingenieur(Employe):

    def __init__(self, nom = "Alain", prenom = "LACOUR", salaire = 10, id = 0, anneeEmbauche = 1999, nbJdT = 300, nbHdP = 300, nbHdG = 300):
        Employe.__init__(self, nom, prenom, salaire, id, anneeEmbauche, nbJdT)
        self._NbHdP = nbHdP
        self._NbHdG = nbHdG

    @abstractmethod
    def afficher(self):
        pass
