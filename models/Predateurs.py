from models.Animal import *
from models.Proies import *
from simulation.world import *
import config as cg
import numpy as np

class Predateurs(Animal):

    def __init__(self, x : int,y : int, energie : float = cg.ENERGIE_BASE):
        super().__init__(x, y, energie)
        self.p_rep = cg.P_REPRODUCTION_PREDATEURS
    
    def manger(self,world : "Monde")->bool:
        proies = self.recherche_voisins([a for a in world.animals if isinstance(a,Proies)])
        for _,proie in proies:
                if np.random.random() <= cg.P_PREDATION:
                    self.energie += proie.energie
                    proie.est_vivant = False
                    print(f"Prédateur mange la proie à ({proie.posx},{proie.posy}). énergie actuelle = {self.energie}")
                    break
