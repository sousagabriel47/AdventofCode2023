"""Solution of day1 - AoC2023."""
import sys
import os
from collections import deque
import copy
from time import sleep

def solve(data):
    mapa = [list(line) for line in data.splitlines()]
    ans = [0,0]
    
    for part in [1]:
        print_mapa_color(mapa)
        print(f'part{part}: {ans[part-1]}')



def print_mapa_color(mapa):
    espelhos = '\/|-'
    caminho = '><^v'
    especial = '*'
    CEND    = '\33[0m'
    CWHITE  = '\33[37m'
    CYEL    = '\33[93m'
    CRED    = '\33[31m'
    CRED2    = '\33[91m'
    CGREEN  = '\33[32m'
    CBLUE  = '\33[32m'
    CVIO  = '\33[32m'
    colors = [CRED2, CRED, CYEL, CYEL, CGREEN, CGREEN, CBLUE, CBLUE, CVIO, CWHITE]

    for i,line in enumerate(mapa):
        out = str(i) + '\t'
        for ch in line:
            
            color = colors[int(ch)]
            out += color + str(ch) + CEND
        print(out.replace(' ',''))

if __name__ == "__main__":
    nday = 17

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


