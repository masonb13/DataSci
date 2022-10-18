import csv
import numpy as np

from sympy import Q

f = open("iterations.CSV", 'w')
writer = csv.writer(f, lineterminator = '\n')
Q = [.99,.999]
P = [.1,.2]

for q in Q:
    for p in P:
        writer.writerow(["--Q={}".format(q)," --P={}".format(p)])

f.close()