"""Solution of day1 - AoC2023."""
import sys
from os import system
from copy import deepcopy
from collections import deque



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

    total_nodes = len(all_nodes)
    pairs = set()
    for conn, listconn in G.items():
        for conn2 in listconn:
            if ((conn2,conn) not in pairs and (conn, conn2) not in pairs): 
                pairs.add((conn, conn2))


    for part in [1]:
        dist = []
        for st, end in pairs:
            d, n_visit = bfs(new_graph(G, [(st, end)]), st, end)
            dist.append([d, (st, end)])
        remove_pair = [p[1] for p in sorted(dist, key=lambda x:x[0])[-3:]]
        dualG = new_graph(G, remove_pair)
        t1, t2 = remove_pair[0]
        _, n1 = bfs(dualG, t1, '')
        _, n2 = bfs(dualG, t2, '')
        
        print(f'part{part}: {n1*n2}')

def new_graph(G, pairs):
    if len(pairs)>1:
        newG = {}
        copyG = deepcopy(G)
        for pair in pairs:
            n, v = pair
            for no, vert in copyG.items():
                if no == n and len(vert) > 1:
                    newG[no] = {vt for vt in vert if vt!=v}
                elif no == v and len(vert) > 1:
                    newG[no] = {vt for vt in vert if vt!=n}
                else:
                    newG[no] = vert
            copyG=deepcopy(newG)
    else:
        newG = {}
        n, v = pairs[0]
        for no, vert in G.items():
            if no == n and len(vert) > 1:
                newG[no] = {vt for vt in vert if vt!=v}
            elif no == v and len(vert) > 1:
                newG[no] = {vt for vt in vert if vt!=n}
            else:
                newG[no] = vert
    return newG

def bfs(G, start, end):
    fila = deque([[start, 0]])
    visit = set()
    nodes = set()
    while fila:
        p, d = fila.popleft()
        if p == end:
            break
        
        nodes.add(p)
        if len(visit) > len(G)*10:
            break

        if (p, d) in visit:
            continue
        visit.add((p, d))
        fila.extend([[n, d+1] for n in G[p] if (p, d+1) not in visit])
    return d, len(nodes)

if __name__ == "__main__":
    nday = 25
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


