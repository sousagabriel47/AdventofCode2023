"""Solution of day1 - AoC2023."""
import sys
from os import system
from copy import deepcopy
import sympy as sp


def solve(data, mode):
    connections = {line.split(': ')[0]: set(line.split(': ')[1].split())
                   for line in data.splitlines()}


    ans = [0,0]

    all_nodes = set()
    for conn, listconn in connections.items():
        all_nodes.add(conn)
        for conn2 in listconn:
            all_nodes.add(conn2)
    G = {}
    for node in all_nodes:
        G[node] = set()
        for conn, listconn in connections.items():
            if node == conn:
                for conn2 in listconn:
                    G[node].add(conn2)
            if node in listconn:
                G[node].add(conn)

    print(len(all_nodes))
    print(len(G))
    for conn, listconn in G.items():
        print(conn, listconn)
    

    for part in [1, 2]:
           
        print(f'part{part}: {ans[part-1]}')
    
if __name__ == "__main__":
    nday = 25
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


