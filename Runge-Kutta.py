### RUNGE-KUTTA APPROXIMATION METHOD


import numpy as np
import matplotlib.pyplot as plt


def calculate_rungekutta(fun,t,h):
    t = np.arange(tspan[0],tspan[1] + h,h)
    y = np.zeros(len(t))
    y[0] = y0

    for n in range(len(t)-1):
        k1 = fun(t[n],y[n])
        k2 = fun(t[n]+ h/2, y[n] + h*(k1/2))
        k3 = fun(t[n]+h/2, y[n]+h*(k2/2))
        k4 = fun(t[n]+h,y[n]+h*k3)
        y[n+1] = y[n] + (h/6)*(k1+ 2*k2+ 2*k3+ k4)
        t[n+1] = t[n] + h
    return t, y

def fun(t,y):
    return t*y

y0 = 1
tspan = [0,2]
step = 0.2

t, y = calculate_rungekutta(fun,tspan,step)

print("  f  |  y  ")

for n in range(len(t)):
    print(f"{t[n]:0.2f} | {y[n]:0.6f}")

fig, ax = plt.subplots()
plt.plot(t,y,"r-o",label="Runge-Kutta Approximation")
plt.grid()
plt.xlabel("t")
plt.ylabel("y")
plt.title("Runge-Kutta Approximation Method")
plt.show()