
import numpy as np
import matplotlib.pyplot as plt

def solve_ivp(f, t_values, y0, h, euler):
    t = np.arange(t_values[0], t_values[1] + h, h)
    y = np.zeros(len(t))
    y[0] = y0

    for n in range(len(t) - 1):
        y[n+1] = euler(f, t[n] ,y[n] ,h)
    
    return t, y

### Euler main

def euler(f,tn,yn,h):
    return yn + h*f(tn,yn)

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

tr, yr = calculate_rungekutta(fun,tspan,step)
te, ye = solve_ivp(fun,tspan,y0,step,euler)

print("  f runge  |  y  runge |  f euler  |  y euler  ")

for n in range(len(tr)):
    print(f"   {tr[n]:0.2f}    |  {yr[n]:0.6f} | {te[n]:0.6f}  |    {ye[n]:0.2f}")

fig, ax = plt.subplots()
plt.plot(tr,yr,"r-o",label="Runge-Kutta")
plt.plot(te,ye,"b-o",label="Euler")
plt.legend()
plt.grid()
plt.xlabel("t")
plt.ylabel("y")
plt.title("Runge-Kutta vs Euler Methods Method")
plt.show()