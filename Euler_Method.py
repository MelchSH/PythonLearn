### EULER-CROMER METHOD
import matplotlib.pyplot as plt
import numpy as np


### Solver
def solve_ivp(f, t_values, y0, h, solver):
    t = np.arange(t_values[0], t_values[1] + h, h)
    y = np.zeros(len(t))
    y[0] = y0

    for n in range(len(t) - 1):
        y[n+1] = solver(f, t[n] ,y[n] ,h)
    
    return t, y

### Euler main

def euler(f,tn,yn,h):
    return yn + h*f(tn,yn)

### Define IVP

def f(t,y):
   return y*t

t_values = [0,2]
y0 = 1
h = 0.2 #step

t,y = solve_ivp(f, t_values, y0, h, euler)

print("|  t   |     y    |")
print("-------------------")
for n in range(len(t)):
    print(f"| {t[n]:0.2f} | {y[n]:1.6f} |")


fig, ax = plt.subplots()
plt.plot(t,y,"b-o")
plt.xlabel("$t$")
plt.ylabel("$y$")
plt.title("Euler Method Aproximation")
plt.grid()
plt.show()
