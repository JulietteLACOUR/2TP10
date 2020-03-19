from multinationale import Multinationale
from filiale import *
from salarie import *
from employe import *
from directeurDeFiliale import *
from employe import *
from ingenieur import*
from administratif import *
from ingenieurJunior import *
from ingenieurSenior import *



M = Multinationale("RCAT", "Tunisie")
F1 = Filiale("RCAT-Belgique", "Belgique", 1998)
F2 = Filiale("RCAT-Maroc", "Maroc", 20)
F3 = Filiale("RCAT-Tunisie", "Tunisie", 1455)
F4 = Filiale("RCAT-Angleterre", "Angleterre", 2015)

M.ajouterFiliale(F1)
M.ajouterFiliale(F2)
M.ajouterFiliale(F3)
M.ajouterFiliale(F4)

S1 = DirecteurDeFiliale("Pichon", "Gérald", 8, 1, 27)
F3.ajouterSalarie(S1)

S2 = Administratif("Rif", "Quentin", 6, 3, 1980, 345, "RH")
S3 = IngenieurSenior("Hardy", "Marine", 6, 30, 1988, 400, 5000, 490, "chef")
F3.ajouterSalarie(S2)
F3.ajouterSalarie(S3)

S4 = IngenieurJunior("Camil", "Richard", 6, 79, 1998, 50, 800, 410, 3)
S5 = Administratif("Titre", "Milo", 4, 8, 2000, 385, "comptabilité client")
F1.ajouterSalarie(S4)
F1.ajouterSalarie(S5)

S6 = IngenieurSenior("Cadylle", "Christine", 7, 890, 1888, 499, 5700, 970, "chef d'équipe")
F2.ajouterSalarie(S6)
M.afficher()

F3.supprimerSalarie(S2)
M.afficher()

F3.supprimerSalarie(S3)
F1.ajouterSalarie(S3)
M.afficher()
