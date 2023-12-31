"""Solution of day1 - AoC2023."""
import sys
from os import system
from copy import deepcopy
import sympy as sp


def solve(data, mode):
    connections = {line.split(': ')[0]: line.split(': ')[1].split() 
                   for line in data.splitlines()}

    for conn, listcon in connections.items():
        print(conn, listcon)    
    ans =[0,0]
    new_connections = {}
    for conn, listcon in connections.items():
        for conn2 in listcon:
            if conn2 not in connections.keys():
                new_connections[conn2] = []
                new_connections[conn2].append(conn)
            else:
                if conn not in connections[conn2]:
                    new_connections[conn2] = []
                    new_connections[conn2].append(conn)

    for conn, listcon in sorted(new_connections.items(),key=lambda x:len(listcon)):
        if conn not in connections.keys():
            connections[conn] = listcon
        else:
            connections[conn].extend(listcon)
    print('depois')
    for conn, listcon in connections.items():
        print(conn, listcon)    

    for part in [1, 2]:
           
        print(f'part{part}: {ans[part-1]}')
    
if __name__ == "__main__":
    nday = 25
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


