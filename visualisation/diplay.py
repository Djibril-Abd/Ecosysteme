from models.Proies import *
from simulation.world import *

class Display:

    def render(self, monde):
        for y in range(monde.larg):
            ligne = ""
            for x in range(monde.long):
                animaux_case = [a for a in monde.animals if a.posx == x and a.posy == y and a.est_vivant]
                nb_H = sum(1 for a in animaux_case if isinstance(a, Proies))
                nb_C = sum(1 for a in animaux_case if isinstance(a, Predateurs))
                if nb_H > 0 and nb_C > 0:
                    ligne += f"{nb_H}H+{nb_C}C"
                elif nb_H > 0:
                    ligne += f"{nb_H}H"
                elif nb_C > 0:
                    ligne += f"{nb_C}C"
                elif monde.env.verif_pousse(x, y):
                    ligne += "*"
                else:
                    ligne += "."
            print(ligne)