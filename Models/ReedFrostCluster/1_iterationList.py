import csv
import numpy as np

f = open("iterations.CSV", 'w')
writer = csv.writer(f, lineterminator = '\n')
Q = np.linspace(.8,.999,101)
P = np.linspace(0,.8,101)

for q in Q:
    for p in P:
        f.write("--export=ALL,Q={},P={}\n".format(q,p))

f.close()