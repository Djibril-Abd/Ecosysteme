import numpy as np
from abc import ABC
from typing import Tuple,List
import math
from simulation.world import *
import config as cg
import random

class Animal(ABC):
    
    p_rep : float = 0.0
    def __init__(self, x : int,y : int, energie : float = cg.ENERGIE_BASE):
        self.posx : int = x
        self.posy : int = y
        self.energie = cg.ENERGIE_BASE
        self.est_vivant = True

    def deplacement(self)->None:
        dx = np.random.randint(-1,2)
        dy = np.random.randint(-1,2)
        self.posx = (self.posx + dx + cg.MONDE_LONGUEUR) % cg.MONDE_LONGUEUR
        self.posy = (self.posy + dy + cg.MONDE_LARGEUR) % cg.MONDE_LARGEUR
        self.energie = self.energie - cg.COUT_DEPLACEMENT

    def verifie_mort(self)->None:
        if self.energie <= 0.0:
            self.est_vivant = False

    def recherche_voisins(self,animals : List["Animal"]):
        
        liste_voisin : List[Tuple[int,"Animal"]] = []
        for i,animal in enumerate(animals):
            if animal is not self:
               if abs(animal.posx - self.posx) <= 1 and abs(animal.posy - self.posy) <= 1:
                   liste_voisin.append((i,animal))
        return liste_voisin
    
    def can_reproduce(self)->bool:
        return self.energie >= cg.MIN_REPRODUCTION
    
    def reproduce(self,animals : List["Animal"]):

        liste_voisins : List[Tuple[int,"Animal"]] = self.recherche_voisins(animals)
        for i,a in liste_voisins:
            if type(a) is type(self):
                if self.can_reproduce() and a.can_reproduce() and random.random() <= self.p_rep:
                    self.energie -= cg.COUT_REPRODUCTION
                    animals[i].energie -= cg.COUT_REPRODUCTION
                    return type(self)(self.posx,self.posy,cg.ENERGIE_BASE)
        return None

    def manger(self,monde : "Monde") -> None:
        pass