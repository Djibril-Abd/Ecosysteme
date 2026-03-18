import numpy as np
from typing import Tuple,List
import math
import random
import config as cg

class Environnement():

    def __init__(self,long,larg):
        self.long = long
        self.larg = larg
        self.grille : List[List[bool]] = [[random.random() < 0.5 for j in range(0,larg)] for i in range(0,long)]
    
    def repousser(self)->None:
        for i in range(0,self.long):
            for j in range(0,self.larg):
                if random.random() < cg.P_POUSSE_PLANTES:
                    self.grille[i][j] = True

    def verif_pousse(self,x : int,y : int)->bool:
        return self.grille[x][y]
    
                       
                       