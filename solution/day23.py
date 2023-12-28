"""Solution of day1 - AoC2023."""
import sys
from collections import deque
from time import sleep
from os import system

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

    start = (0,1)
    end = (22,21)
    
    ans = [0,0]
    for part in [1]:
        caminho = []
        rotas = deque([(start, 0, [])])
        total =[]
        
        while rotas:
            p, dist, caminho = rotas.popleft()

            print(dist)

            if p in caminho:
                continue
            caminho.append(p)
            
            # if p == end:
            #     total.append(dist)
            #     continue

            new_dir = check_dir(p, mapa, slopes)
            
            if new_dir:
                for new in new_dir:
                    rotas.append((new, dist+1, caminho))
            print_mapa_color(mapa, caminho)
        for c in total:
            print(c)

        #print(total)
        print(f'part{part}: {ans[part-1]}')

def check_dir(p, mapa, slopes):
    pL = p[0]
    pR = p[1]
    directions = {(1,0),(0,1),(-1,0),(0,-1)}
    new_dir = []
    nL, nR = len(mapa), len(mapa[0])
    for dL, dR in directions:
        if (((dL+pL) in range(nL)) and
            (dR+pR) in range(nR) and
            (mapa[dL+pL][dR+pR] != '#')):
            if mapa[dL+pL][dR+pR] in '^<>v':
                if ((mapa[dL+pL][dR+pR] == '>' and (dL,dR)==(0,1)) or
                    (mapa[dL+pL][dR+pR] == 'v' and (dL,dR)==(1,0)) or
                    (mapa[dL+pL][dR+pR] == '<' and (dL,dR)==(0,-1)) or 
                    (mapa[dL+pL][dR+pR] == '^' and (dL,dR)==(-1,0))):
                    new_dir.append((dL+pL, dR+pR))
            else:
                new_dir.append((dL+pL, dR+pR))
    return new_dir

def print_mapa_color(mapa, caminho):
    CEND    = '\33[0m'
    CWHITE  = '\33[37m'
    CRED    = '\33[31m'
    CBLUE    = '\33[34m'
    CRED2    = '\33[41m'
    CGREEN  = '\33[32m'
    system('cls')
    for iL,line in enumerate(mapa):
        strline = ''
        print(iL, end='\t')
        for iR, ch in enumerate(line):
            if (iL, iR) in caminho:
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


