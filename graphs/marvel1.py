'''
Created on 09/04/2018

@author: gvega
'''

import csv
from numpy import char
characters=[]
books=["AAAAAA"]
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def make_link2(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    if node2 in G[node1]:
        (G[node1])[node2] += 1
    else:
        (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    if node1 in G[node2]:
        (G[node2])[node1] += 1
    else:
        (G[node2])[node1] = 1
    return G



def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    global characters
    global books
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for (node1, node2) in tsv: 
        if node1 not in characters:
            characters.append(node1)
        if node2 not in books:
            books.append(node2)
        make_link(G, node1, node2)
    return G

# Read the marvel comics graph
marvelG = read_graph('..\\file')

# distance from start (original)
def distance(G, v1, v2):
    distance_from_start = {}
    open_list = [v1]
    distance_from_start[v1] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                if neighbor == v2: return distance_from_start[v2]
                open_list.append(neighbor)
    return False

# path from start (after modification on distance())
def path(G, v1, v2):
    #distance_from_start = {}
    path_from_start = {} # modification
    open_list = [v1]
    #distance_from_start[v1] = 0
    path_from_start[v1] = [v1] # modification
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            #if neighbor not in distance_from_start:
            if neighbor not in path_from_start: # modification
                #distance_from_start[neighbor] = distance_from_start[current] + 1
                path_from_start[neighbor] = path_from_start[current] + [neighbor] # modification
                #if neighbor == v2: return distance_from_start[v2]
                if neighbor == v2: return path_from_start[v2] # modification
                open_list.append(neighbor)
    return False

from_node = "A"
to_node = "ZZZAX"

#print(books)

print( distance(marvelG, from_node, to_node))
print( path(marvelG, from_node, to_node))

charG={}
for char1 in characters:
    for book in marvelG[char1]:
        for char2 in marvelG[book]:
            if char1 > char2:
                 make_link2(charG, char1, char2)

print(charG['HUMAN TORCH/JOHNNY S']['THING/BENJAMIN J. GR'])
print(charG['SPIDER-MAN/PETER PAR']['WATSON-PARKER, MARY '])
print(charG['INVISIBLE WOMAN/SUE ']['MR. FANTASTIC/REED R'])
print(charG['CAPTAIN AMERICA']['IRON MAN/TONY STARK '])