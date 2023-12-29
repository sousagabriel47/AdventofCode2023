"""Solution of day1 - AoC2023."""
import sys
from os import system
from copy import deepcopy
sys.setrecursionlimit(int(10e6))

D_VERT = {}
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
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    VERTICES = set()
    VERTICES.add(start)
    VERTICES.add(end)

    for pL, pR in paths:
        vizinhos = 0
        for dL, dR in direction:
            if ((dL + pL, pR + dR) in paths or 
                (dL + pL, pR + dR) in slopes.keys()):
                vizinhos += 1
        if vizinhos > 2:
            VERTICES.add((pL, pR))



    mapa_len = (nL, nR)
    ans = [0,0]
    for part in [1,2]:
        total.clear() 
        # if part==1:
        #     rota_dfs(start, forest, paths, slopes, mapa_len, None, 0, end, part)
        # else:
        for p in VERTICES:
            D_VERT[p] = []
            dfs_vertices(p, p, forest, paths, slopes, mapa_len, None, 0, VERTICES, part)
        rota_dfs(start, None, 0, end)

        ans[part-1] = max(total)
        print(f'part{part}: {ans[part-1]}')

def dfs_vertices(p, start, forest, paths, slopes, mapa_len, caminho, dist, end_list, part):
    if caminho is None:
        caminho = set()
    caminho.add(p)

    if p in end_list and p != start:
        D_VERT[start].append((p,dist))
        return

    new = check_dir(p, forest, paths, slopes, mapa_len, part, caminho)

    for nP in new:
        if nP not in caminho:
            dfs_vertices(nP, start, forest, 
                 paths, slopes, mapa_len, 
                 (caminho), dist+1, end_list, part)


def rota_dfs(p, caminho, dist, end):
     
    if caminho is None:
         caminho = set()
    caminho.add(p)

    if p == end:
        #print(len(total))
        total.append(dist)
        print(dist, max(total))
        return
    #print(caminho)
    for nP,nDist in D_VERT[p]:
        if nP not in caminho:
            rota_dfs(nP, deepcopy(caminho), nDist+dist, end)

    #6582 low

    # for nP in new:
    #     if nP not in caminho:
    #         rota_dfs(nP, forest, paths, slopes, mapa_len, deepcopy(caminho), dist+1, end, part)
        


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


