import csv
import numpy as np

f = open("2_combination.CSV", 'w')
writer = csv.writer(f, lineterminator = '\n')
Q = np.arange(0.95,1,0.0005)
P = np.arange(0,1,.01)
for q in Q:
    for p in P:
        with open("ReedFrostCluster\Data\ReedFrostCluster\{}_{}.csv".format(p,q)) as h:
            reader = csv.reader(h)
            for line in reader:
                if line != ["SimNum","P","Q","time","I"]:
                    line = str(line[0]) + "," + str(line[1]) + "," + str(line[2]) + "," + str(line[3]) + "," + str(line[4]) + "\n"
                    f.write(line)
