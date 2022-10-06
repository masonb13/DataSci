# Mason Bursac Lehigh Uncertainty Lab

# Imports
import argparse
import networkx as nx
import random
import csv

# Define argparse
parser = argparse.ArgumentParser()
parser.add_argument('--SIMNUM',type=int)
parser.add_argument('--P',type=float)
parser.add_argument('--Q',type=float)
args = parser.parse_args()

# removes p percent of edges
def removeRandom(G, p):
    num = int(len(G.edges)*p)
    G.remove_edges_from(random.sample(G.edges(), k=num))

#simulates one time interval of infection
def infect(G, q):
    choices = ['s','i']
    I = []
    R = []
    infected = list(dict((n,d['val']) for n,d in G.nodes().items() if d['val'] == 'i'))
    susceptible = list(dict((n,d['val']) for n,d in G.nodes().items() if d['val'] == 's'))
    for i in susceptible:
        neighbors = list(G.adj[i]) # find all nodes connected to node i with ['val'] == 'i'
        infectedNeighbors = list(set(neighbors).intersection(set(infected)))
        p = (1-q**len(infectedNeighbors)) #---------------------------------------------------------------------------
        choose = random.choices(choices, weights=(1-p, p), k=1)
        if choose[0] == 'i':
            I.append(i)
    return [I, infected]    #new infected, old infected now recovered

#sets n nodes to infected randomly to start the model
def start(G, n):
    num = random.sample(range(len(G)), k=n)
    for i in num:
        G.nodes[i]['val'] = 'i'

def brokenNetworkModel():
    #paramaters
    s = 2000
    p = args.P #change prob here -------------------------------------------------------------
    numGen = 30
    q = args.Q
    i = 2

    #build network and infect first interval
    G = nx.complete_graph(s)   
    nx.set_node_attributes(G, "s", "val")
    removeRandom(G, p)
    I = [i]
    start(G,i)

    #infect numGen intervals of the network
    for i in range(numGen):
        output = infect(G,q)
        I.append(len(output[0]))

        for j in output[0]:
            G.nodes[j]['val'] = 'i'
        for r in output[1]:
            G.nodes[r]['val'] = 'r'

    return I


# Run numRep models
numRep = 1
name = str(args.SIMNUM) + ".csv"
Header = ["SimNum", "P", "Q", "time", "I"]

f = open(name, 'w')
writer = csv.writer(f, lineterminator = '\n')
writer.writerow(Header)

for i in range(numRep):
    I = brokenNetworkModel()
    for i in range(len(I)):
        writer.writerow([args.SIMNUM,args.P, args.Q, i, I[i]])

f.close()

