from ingenieur import *

class IngenieurSenior(Ingenieur):

    def __init__(self, nom = "Alain", prenom = "LACOUR", salaire = 10, id = 0, anneeEmbauche = 1999, nbJdT = 300, nbHdP = 300, nbHdG = 300, responsabilite = None):
        Ingenieur.__init__(self, nom, prenom, salaire, id, anneeEmbauche, nbJdT,nbHdP,nbHdG)
        self._R = responsabilite

    def afficher(self):
        print("* [id=", self._Id, "]", self._N, "et", self._P, ", Salaire :", self._S, ", Statut : Ingénieur-senior, Année d'embauche :", self._AE, "Nombre de jours de travail :", self._NbJdT, ", Nombre d'heures de projet :", self._NbHdP, ", Nombre d'heures de gestion :", self._NbHdG, ", Responsabilité : ", self._R)
