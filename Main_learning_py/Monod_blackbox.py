import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the Monod model parameters
mu_max = 0.5  # maximum growth rate (1/h)
Ks = 0.1  # half-saturation constant (mg/L)
Y = 0.5  # yield coefficient (mg cells/mg substrate)
k_d = 0.01  # death rate (1/h)

# Define the initial conditions
X0 = 0.1  # initial biomass concentration (mg/L)
S0 = 10.0  # initial substrate concentration (mg/L)

# Define the time span
t_end = 24  # hours
dt = 0.01  # time step
t = np.arange(0, t_end, dt)

# Define the Monod model equations
def monod_model(y, t, mu_max, Ks, Y, k_d):
    X, S = y
    mu = mu_max * S / (Ks + S)
    dXdt = mu * X - k_d * X
    dSdt = -Y * mu * X
    return [dXdt, dSdt]

# Solve the ODE system
y0 = [X0, S0]
sol = odeint(monod_model, y0, t, args=(mu_max, Ks, Y, k_d))

# Extract the solution
X = sol[:, 0]
S = sol[:, 1]

# Plot the results
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(t, X)
plt.xlabel('Time (h)')
plt.ylabel('Biomass Concentration (mg/L)')
plt.title('Bacterial Growth')

plt.subplot(1, 2, 2)
plt.plot(t, S)
plt.xlabel('Time (h)')
plt.ylabel('Substrate Concentration (mg/L)')
plt.title('Substrate Consumption')

plt.tight_layout()
plt.show()