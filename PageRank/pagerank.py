import networkx as nx
import numpy as np
import operator
import os
import shutil
import sys

import time

# Check file length
def file_len():
    with open("web-Google.txt") as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def create_graph():
    G = nx.DiGraph()
    return G

def add_node(G, n):
    if G.has_node(n):
        pass
    else:
       G.add_node(n)

def add_edge(G, fromN, toN):
    if G.has_edge(fromN,toN):
        pass
    else:
        G.add_edge(fromN, toN)

# Read file and put nodes into graph 
def graph_file(G, file_len):
    i = 0
    file = open("web-Google.txt", "r")
    print("Putting nodes into graph...\n")

    for line in file:
        line = line.rstrip()
        if line[0] == "#":
            continue
        line_arr = line.split("\t")
        add_node(G, int(line_arr[0]))
        add_node(G, int(line_arr[1]))
        add_edge(G, int(line_arr[0]), int(line_arr[1]))
        i += 1
    file.close()
    print("\nGraphing completed.\n")

# Calculate PageRank using graph with the following parameters  
"""
G: A NetworkX graph.
prob: Probability to deal with dead-ends and spider traps, usually between 0.8 and 0.9. Allow each random surfer with a probability to teleport to a random page.
personalization: Personalization vector which consists of a dictionary with a key for every graph node and nonzero personalization value for each node. 
max_ite: Maximum number of iterations in power method eigenvalue solver. 
tol: Error tolerance used to check convergence in power method solver. 
startV: Starting value of PageRank iteration for each node.   
weight: Edge data key.
dangling: The outedges to be assigned to any "dangling" nodes, i.e., nodes without any outedges. The dict key is the node the outedge points to and the dict value is the weight of that outedge.  
"""
def pagerank(G, prob = 0.85, personalization = None, max_ite = 1000, tol = 1.0e-9, 
    startV = None, weight = 'weight', dangling = None):
    
    if len(G) == 0:
        return {}

    # Copy G into stochastic graph
    SG = nx.stochastic_graph(G, weight=weight)
    SNoN = SG.number_of_nodes()

    # Choose start vector
    if startV is None:
        x = dict.fromkeys(SG, 1.0 / SNoN)
    else:
        s = float(sum(startV.values()))
        x = dict((k, v / s) for k, v in startV.items())
    
    # Assign personalization vector
    if personalization is None:
        p = dict.fromkeys(SG, 1.0 / SNoN)
    else:
        s = float(sum(personalization.values()))
        p = dict((k, v / s) for k, v in personalization.items())

    # If no dangling vector then use personalization vector
    if dangling is None:        
        dangling_weight = p
    else:
        s = float(sum(dangling.values()))
        dangling_weight = dict((k, v / s) for k, v in dangling.items())
    dangling_nodes = [n for n in SG if SG.out_degree(n, weight = weight) == 0.0]

    i = 0

    # Iterate power 
    for _ in range(max_ite):  
        xlast = x
        x = dict.fromkeys(xlast.keys(), 0)
        dangling_sum = prob * sum(xlast[n] for n in dangling_nodes)
        for n in x:
            for nbr in SG[n]:
                x[nbr] += prob * xlast[n] *SG[n][nbr][weight]
            x[n] += dangling_sum * dangling_weight.get(n, 0) + (1.0 - prob) * p.get(n, 0)
        # Check convergence
        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < SNoN * tol:
            return x
        i += 1
    raise nx.PowerIterationFailedConvergence(max_ite)    

def main():

    start_time = time.time()
    no_file_line = file_len()
    tmp = sys.stdout
               
    G = create_graph()
    graph_file(G,no_file_line)
    print ("Ranking...")
    pr = pagerank(G)

    sys.stdout = open("output.txt", "w")
    print(sorted(pr.items(), key = operator.itemgetter(1), reverse = True))
        
    sys.stdout = open("runtime.txt", "w")
    print("Runtime: %s seconds" % (time.time() - start_time))
    sys.stdout = tmp
    print("Ranking completed. Check output.txt for the list of PageRank for each node, runtime.txt for runtime.")
    sys.stdout.close()

if __name__ == "__main__":
    main()