import csv
import numpy as np

f = open("combination.CSV", 'w')
writer = csv.writer(f, lineterminator = '\n')
Q = np.linspace(.8,.999,101)
P = np.linspace(0,.8,101)
for q in Q:
    for p in P:
        with open("C:\\Users\\Mase\\Desktop\\ReedFrostCluster\\{}_{}.csv".format(p,q)) as h:
            reader = csv.reader(h)
            for line in reader:
                if line != "SimNum,P,Q,time,I":
                    line = str(line[0]) + "," + str(line[1]) + "," + str(line[2]) + "," + str(line[3]) + "," + str(line[4]) + "\n"
                    f.write(line)
