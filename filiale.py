from multinationale import *

class Filiale:
    def __init__(self, nom = "AtelierLacour-France", pays = "la France", dateDeCreation = 1999):
        self.__N = nom
        self.__P = pays
        self.__D = dateDeCreation
        self.__S = []

    def getD(self):
        return self.__D

    def getN(self):
        return self.__N

    def getP(self):
        return self.__P

    def getS(self):
       return self.__S

    def ajouterSalarie(self, s):
        self.__S.append(s)

    def supprimerSalarie(self, s):
        self.__S.remove(s)
