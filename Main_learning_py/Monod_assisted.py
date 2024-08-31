import matplotlib.pyplot as plt;
import numpy as np;
from scipy.integrate import odeint

mumax = 0.5
Yxs = 0.5
Ks = 0.1
Kd = 0.01
S0 = 10.0
X0 = 0.1

S = S0
X = X0

t_final = 24
delta_t = 0.01
time = np.arange(0,t_final,delta_t)
tspan = (0,t_final)

def monod(y,t, mumax, Ks, Yxs, Kd):
    X,S = y

    mu= mumax*(S/(Ks+S))

    dXdt = mu*X - Kd*X
    dSdt = - (mu*X)/Yxs

    return np.array([dXdt, dSdt])

y0 = [X0, S0]
integrate_SandX = odeint(monod,y0,time,args=(mumax, Ks, Yxs, Kd))

Biomass = integrate_SandX[:,0]
Subst = integrate_SandX[:,1]


plt.plot(time, Biomass, label="Biomass")
plt.plot(time,Subst,label="Substrate")

plt.show()