from models.Animal import *
from models.Environnement import *
from simulation.world import *
import config as cg
import numpy as np

class Proies(Animal):

    def __init__(self, x, y, energie = cg.ENERGIE_BASE):
        super().__init__(x, y, energie)
        self.p_rep = cg.P_REPRODUCTION_PROIES
    
    def manger(self, monde : "Monde"):

        x = self.posx
        y = self.posy
        if monde.env.verif_pousse(x,y):
            self.energie = min(cg.MAX_ENERGIE,self.energie + cg.GAIN_NOURRITURE)
            monde.env.grille[x][y] = False
            return True
        return False
