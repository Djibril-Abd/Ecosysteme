from models.Animal import *
from models.Predateurs import *
from models.Proies import *
from models.Environnement import *
import config as cg
import numpy as np

class Monde():

    def __init__(self,long : int, larg : int):
        self.long = long
        self.larg = larg
        self.animals : List["Animal"] = []
        self.env = Environnement(long,larg)
        self.hist_pro_pre : List[int] = []

    def initialiser_population(self):

        for _ in range(cg.NB_PROIES):
            x = np.random.randint(0,cg.MONDE_LONGUEUR)
            y = np.random.randint(0,cg.MONDE_LARGEUR)
            self.animals.append(Proies(x,y))
        
        for _ in range(cg.NB_PREDATEUR):
            x = np.random.randint(0,cg.MONDE_LONGUEUR)
            y = np.random.randint(0,cg.MONDE_LARGEUR)
            self.animals.append(Predateurs(x,y))
    

    def compter_animal(self):

        nb_proies = sum(1 for a in self.animals if isinstance(a, Proies))
        nb_predateurs = sum(1 for a in self.animals if isinstance(a, Predateurs))

        self.hist_pro_pre.append([nb_proies, nb_predateurs])


    def remove_dead(self)->None:
        self.animals = [p for p in self.animals if p.est_vivant]

    def step(self)->None:

        animal_nouv : List["Animal"] = []
        for a in self.animals:
            a.verifie_mort()
            a.deplacement()

            if a.est_vivant:
                a.manger(self)
                enfant = a.reproduce(self.animals)
                if enfant is not None:
                    animal_nouv.append(enfant)

        self.animals.extend(animal_nouv)
        self.remove_dead()
        self.env.repousser()
        self.compter_animal()

