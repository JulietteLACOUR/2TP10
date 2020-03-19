from employe import *

class Administratif(Employe):

    def __init__(self, nom = "Alain", prenom = "LACOUR", salaire = 10, id = 0, anneeEmbauche = 1999, nbJdT = 300, service = 1999):
        Employe.__init__(self,nom, prenom, salaire, id, anneeEmbauche, nbJdT)
        self._St = service


    def afficher(self):
        print("* [id=", self._Id, "]", self._N, "et", self._P, ", Salaire :", self._S, ", Statut : Administratif , Année d'embauche :", self._AE, "Nombre de jours de travail :", self._NbJdT, ", Service :", self._St)

