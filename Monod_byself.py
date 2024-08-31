from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# init variables
mumax = 0.5
Ks = 0.1
Yxs = 0.5
S0 = 10.0
X0 = 0.1

t_total = 12
delta_t = 0.1

# main dif. eq. model to solve
def monod_main(y, t, mumax, Ks, Yxs):
    X, S = y

    mu = mumax * (S/(Ks+S))
    dXdt = mu*X
    dSdt = - dXdt/Yxs 

    return np.array([dXdt,dSdt])

#additional vars. for odeint
t = np.arange(0,t_total,delta_t)
y0 = [X0, S0]

sol = odeint(monod_main,y0, t, args = (mumax, Ks, Yxs)) # solve eq system from model 

Biomass=sol[:,0]
Substrate=sol[:,1]

#Set plot
plt.plot(t,Biomass,label="Biomass")
plt.plot(t,Substrate,label="Substrate")
plt.legend()
plt.xlabel("Tiempo (hrs)")
plt.ylabel("Concentración (g/L)")
plt.title("Prueba de Cinética de E. Coli con Monod")
plt.grid()
plt.show()
