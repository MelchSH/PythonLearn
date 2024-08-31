### Main operations in mass balance steady state

import numpy as np

inlet1_flow = 10 #kg/h
inlet1_conc = 0.050 #g/L
inlet2_flow = 10
inlet2_conc = 0.020
outlet1_flow = 30
outlet1_conc = float


outlet1_conc = abs(- inlet1_conc*inlet1_flow + inlet2_flow * inlet2_conc/outlet1_flow)

print(outlet1_conc)