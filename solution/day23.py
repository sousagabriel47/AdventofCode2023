"""Solution of day1 - AoC2023."""
import sys
from os import system
from copy import deepcopy
sys.setrecursionlimit(int(10e6))


total = []

def solve(data, mode):
    mapa = [list(line) for line in data.splitlines()]

    forest = set()
    paths = set()
    slopes = {}

    for iL,line in enumerate(mapa):
        for iR, ch in enumerate(line):
            if ch == '#':
                forest.add((iL,iR))
            if ch == '.':
                paths.add((iL,iR))
            if ch in '^<>v':
                slopes[(iL,iR)] = ch
    nL = len(mapa)
    nR = len(mapa[0])

    start = (0,1)
    end = (nL-1,nR-2)
    mapa_len = (nL, nR)
    ans = [0,0]
    for part in [2]:
        total.clear() 
        rota_dfs(start, forest, paths, slopes, mapa_len, None, 0, end, part)
        ans[part-1] = max(total)
        print(f'part{part}: {ans[part-1]}')

def rota_dfs(p, forest, paths, slopes, mapa_len, caminho, dist, end, part):
    if caminho is None:
        caminho = set()
    caminho.add(p)

    if p == end:
        print(len(total))
        print_mapa_color(forest, paths, slopes, mapa_len, caminho, p)
        total.append(dist)
        return

    new = check_dir(p, forest, paths, slopes, mapa_len, part, caminho)
    if not dist % 500:
        print_mapa_color(forest, paths, slopes, mapa_len, caminho, p)
        print(p, dist, new)

    for nP in new:
        if nP not in caminho:
            rota_dfs(nP, forest, paths, slopes, mapa_len, deepcopy(caminho), dist+1, end, part)
        else:
            if dist>2400:
                print('NEW',nP)
        


def check_dir(p, forest, paths, slopes, mapa_len, part, caminho):
    pL = p[0]
    pR = p[1]
    directions = {('v',1,0),('>',0,1),('^',-1,0),('<',0,-1)}
    new_dir = set()
    nL, nR = mapa_len
    for ch, dL, dR in directions:
        if (((dL+pL) in range(nL)) and
            (dR+pR) in range(nR) and
            ((dL+pL, dR+pR) not in forest)):
            if part==1:
                if (dL+pL, dR+pR) in slopes:
                    if (ch == slopes[(dL+pL, dR+pR)]):
                        new_dir.add((dL+pL, dR+pR))
                else:
                    new_dir.add((dL+pL, dR+pR))
            else:
                if (dL+pL, dR+pR) not in caminho:
                    new_dir.add((dL+pL, dR+pR))
    return new_dir

def print_mapa_color(forest, paths, slopes, mapa_len, caminho, p):
    CEND    = '\33[0m'
    CWHITE  = '\33[37m'
    CRED    = '\33[31m'
    CBLUE    = '\33[34m'
    CRED2    = '\33[41m'
    CGREEN  = '\33[32m'
    CCYAN  = '\33[36m'
    system('cls')
    nL, nR = mapa_len
    for iL in range(nL):
        strline = ''
        print(iL, end='\t')
        for iR in range(nR):
            if (iL, iR) == p:
                strline += CCYAN + 'X' + CEND
            elif (iL, iR) in caminho:
                strline += CRED + 'O' + CEND
            elif (iL, iR) in paths:
                strline += CWHITE + '.' + CEND
            elif (iL, iR) in slopes:
                strline += CBLUE + slopes[(iL, iR)] + CEND
            
            if (iL, iR) in forest:
                strline += CGREEN + '#' + CEND
        print(strline.replace(' ', ''))
    
if __name__ == "__main__":
    nday = 23
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


