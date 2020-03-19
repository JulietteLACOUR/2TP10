from salarie import Salarie

class DirecteurDeFiliale(Salarie):

    def __init__(self, nom = "Alain", prenom = "LACOUR", salaire = 10, id = 0, anneeNomination = 1999):
        Salarie.__init__(self, nom, prenom, salaire, id)
        self._AN = anneeNomination

    def afficher(self):
        print("* [id=", self._Id, "]", self._N, "et", self._P, ", Salaire :", self._S, ", Statut : Directeur , Année de nomination :", self._AN)
