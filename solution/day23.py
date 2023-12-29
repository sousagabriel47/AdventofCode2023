"""Solution of day1 - AoC2023."""
import sys
from collections import deque
from time import sleep
from os import system
from copy import deepcopy
from functools import cache
sys.setrecursionlimit(int(10e6))


total = []

def solve(data, mode):
    mapa = [list(line) for line in data.splitlines()]

    forest = set()
    paths = set()
    slopes = set()

    for iL,line in enumerate(mapa):
        for iR, ch in enumerate(line):
            if ch == '#':
                forest.add((iL,iR))
            if ch == '.':
                paths.add((iL,iR))
            if ch in '^<>v':
                slopes.add((ch,iL,iR))
    nL = len(mapa)
    nR = len(mapa[0])

    start = (0,1)
    end = (nL-1,nR-2)
    
    ans = [0,0]
    for part in [2]:
        total.clear() 
        rota_dfs(start, mapa, None, 0, end, part)
        ans[part-1] = max(total)
        print(f'part{part}: {ans[part-1]}')

@cache
def rota_dfs(p, mapa, caminho, dist, end, part):
    if caminho is None:
        caminho = set()
    caminho.add(p)

    if p == end:
        print(len(total))
        total.append(dist)
        return

    new = check_dir(p, mapa, part, caminho)
    if dist > 2400:
        #print_mapa_color(mapa, caminho, p)
        print(p, dist, new)

    for nP in new:
        if nP not in caminho:
            rota_dfs(nP, mapa, deepcopy(caminho), dist+1, end, part)
        else:
            if dist>2400:
                print('NEW',nP)
        


def check_dir(p, mapa, part, caminho):
    pL = p[0]
    pR = p[1]
    directions = {(1,0),(0,1),(-1,0),(0,-1)}
    new_dir = set()
    nL, nR = len(mapa), len(mapa[0])
    for dL, dR in directions:
        if (((dL+pL) in range(nL)) and
            (dR+pR) in range(nR) and
            (mapa[dL+pL][dR+pR] != '#')):
            if part==1:
                if mapa[dL+pL][dR+pR] in '^<>v':
                    if ((mapa[dL+pL][dR+pR] == '>' and (dL,dR)==(0,1)) or
                        (mapa[dL+pL][dR+pR] == 'v' and (dL,dR)==(1,0)) or
                        (mapa[dL+pL][dR+pR] == '<' and (dL,dR)==(0,-1)) or 
                        (mapa[dL+pL][dR+pR] == '^' and (dL,dR)==(-1,0))):
                        new_dir.add((dL+pL, dR+pR))
                else:
                    new_dir.add((dL+pL, dR+pR))
            else:
                if (dL+pL, dR+pR) not in caminho:
                    new_dir.add((dL+pL, dR+pR))
    return new_dir

def print_mapa_color(mapa, caminho, p):
    CEND    = '\33[0m'
    CWHITE  = '\33[37m'
    CRED    = '\33[31m'
    CBLUE    = '\33[34m'
    CRED2    = '\33[41m'
    CGREEN  = '\33[32m'
    CCYAN  = '\33[36m'
    system('cls')
    for iL,line in enumerate(mapa):
        strline = ''
        print(iL, end='\t')
        for iR, ch in enumerate(line):
            if (iL, iR) == p:
                strline += CCYAN + 'X' + CEND
            elif (iL, iR) in caminho:
                strline += CRED + 'O' + CEND
            elif ch == '#':
                strline += CGREEN + '#' + CEND
            elif ch in '^<>v':
                strline += CBLUE + ch + CEND
            else:
                strline += CWHITE + '.' + CEND
        print(strline.replace(' ', ''))
    
if __name__ == "__main__":
    nday = 23
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


