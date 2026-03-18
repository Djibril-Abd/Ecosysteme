import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Nombres initiaux des proies et prédateurs avant la simulation
x0 = 40.0
y0 = 9.0

# Initialisation respectivement des taux de croissance naturel des proies, de prédation,\\
# de mortalité naturel des prédateurs et de reproduction des prédateurs par proie consommée

alpha = 1.0
beta =0.1
gamma =1.5
delta =0.075


N = 1000
t = 0.01

x = []
y  =[]
xi = x0
yi = y0
for i in range(0,N):
    a = xi + t*(alpha*xi - beta*xi*yi)
    x.append(a)
    xi = x[i]

    b = yi + t*(delta*xi*yi - gamma*yi)
    y.append(b)
    yi = y[i]

plt.plot(x,label = "Proies")
plt.plot(y,label = "Prédateurs")
plt.title("Evolution de la population")
plt.legend()
plt.grid()
plt.show()