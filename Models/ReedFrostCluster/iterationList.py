import csv
import numpy as np

f = open("iterations.CSV", 'w')
writer = csv.writer(f, lineterminator = '\n')
Q = [.99,.999]
P = [.1,.2]

for q in Q:
    for p in P:
        f.write("--export=ALL,Q={},P={}\n".format(q,p))

f.close()