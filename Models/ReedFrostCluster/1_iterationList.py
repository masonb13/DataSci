import csv
import numpy as np

f = open("1_iterations.CSV", 'w')
writer = csv.writer(f, lineterminator = '\n')
Q = np.arange(0.95,1,0.0005)
P = np.arange(0,1,.01)

for q in Q:
    for p in P:
        f.write("--export=ALL,Q={},P={}\n".format(q,p))

f.close()