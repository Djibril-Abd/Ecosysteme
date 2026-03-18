from simulation.world import *
from visualisation.diplay import *
import config as cg
import time

class Simulation():

    display = Display()
    def __init__(self,long : int,larg : int):
        self.monde = Monde(long,larg)
        self.step_cpt = 0
        self.monde.initialiser_population()
        self.monde.compter_animal()

    def step(self):
        self.monde.step()
        self.step_cpt +=1
    
    def run(self):
        self.display.render(self.monde)
        while self.step_cpt <= cg.MAX_STEPS and len(self.monde.animals) > 0:
            print("Itération"+str(self.step_cpt))
            self.step()
            #self.display.render(self.monde)
            #time.sleep(2)

    
    
