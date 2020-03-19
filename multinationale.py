from filiale import *
from salarie import *
from employe import *
from directeurDeFiliale import *
from employe import *
from ingenieur import*
from administratif import *
from ingenieurJunior import *
from ingenieurSenior import *




class Multinationale :
    def __init__(self, nom = "AtelierLacour", PaysOrigine = "France"):
        self.__N = nom
        self.__P = PaysOrigine
        self.__F = []

    def ajouterFiliale(self, f):
        self.__F.append(f)

    def afficher(self):
        print("-----------")
        print("- La multinationale", self.__N, "est composée de", len(self.__F), "filiales. Son pays d'origine est la", self.__P, ".")
        if len(self.__F) != 0:
            datePlusAncienne = self.__F[0].getD()
            FilialePlusAncienne = self.__F[0]
            for i in self.__F:
                if i.getD() < datePlusAncienne:
                    FilialePlusAncienne = i
            print("- La filiale la plus ancienne de cette multinationale de", self.__P, "est : ", FilialePlusAncienne.getN(), ". Elle est composée de", len(FilialePlusAncienne.getS()), "salariés.")
            total_salaries = 0
            for i in self.__F:
                total_salaries += len(i.getS())
            print("- RCAT est composé de", total_salaries, "salariés :")
            for i in self.__F:
                for j in i.getS():
                    j.afficher()
                    print("Site :", i.getP())
        print("-----------")
