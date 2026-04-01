import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from simulation.engine import *
import config as cg

si = Simulation(cg.MONDE_LONGUEUR,cg.MONDE_LARGEUR)
si.run()

#sns.displot(data = si.monde.hist_pro_pre)

proies_hist = [h[0] for h in si.monde.hist_pro_pre]
predateurs_hist = [h[1] for h in si.monde.hist_pro_pre]

plt.plot(proies_hist, label="Proies")
plt.plot(predateurs_hist, label="Prédateurs")
plt.xlabel("Itérations")
plt.ylabel("Population")
plt.title("Evolution de la population")
plt.legend()
plt.show()