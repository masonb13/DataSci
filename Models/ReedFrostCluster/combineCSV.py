import csv
import numpy as np

f = open("combination.CSV", 'w')
writer = csv.writer(f, lineterminator = '\n')
Q = np.linspace(.8,.999,101)
P = np.linspace(0,.8,101)
for q in Q:
    for p in P:
        with open("{}_{}.csv".format(q,p)) as h:
            reader = csv.reader(h)
            for line in reader:
                if line != "SimNum,P,Q,time,I":
                    f.write(line)
