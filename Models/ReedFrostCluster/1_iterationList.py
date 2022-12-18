import csv
import numpy as np

f = open("1_iterations.CSV", 'w')
writer = csv.writer(f, lineterminator = '\n')
Q = np.round(np.arange(0.95,1,.0005),decimals=4)
P = np.round(np.arange(0,1,.01),decimals=2)

for q in Q:
    for p in P:
        f.write("--export=ALL,Q={},P={}\n".format(q,p))

f.close()