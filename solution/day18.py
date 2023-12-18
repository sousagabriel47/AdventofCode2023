"""Solution of day1 - AoC2023."""
import sys
import os
from time import sleep
from matplotlib.path import Path




def solve(data):
    movimentos = [line.split() for line in data.splitlines()]
    ans = [0,0]
    

    mov = {'R': [0,1], 'L':[0,-1], 'U': [-1,0], 'D':[1,0]}
    mov2 = ['R', 'D', 'L', 'U']
    for part in [1]:
        caminho = [[0,0]]
        for cmd, t, color in movimentos:
            
            if part==1:
                vetor = mov[cmd]
            else:
                new_cmd = mov2[int(color[-2])]
                new_t = int(color[2:-1],16)+1
                vetor = mov[new_cmd]
            steps = int(t) if part == 1 else new_t
            p = caminho[-1]
            caminho.append([p[0] + vetor[0]*steps,p[1] + vetor[1]*steps])
        # limites
        listL = [p[0] for p in caminho]
        listR = [p[1] for p in caminho]
        
        limL = [min(listL),max(listL)]
        limR = [min(listR),max(listR)]
        # create mapa
        mapa  = [list('.' * (limR[1] - limR[0] + 1)) for _ in range(limL[1] - limL[0] + 1)] 
        for p in caminho:
            mapa[p[0]-limL[0]][p[1]-limR[0]] = '#'
                



        # p = Path(caminho)
        # inside = 0
        # for iL in range(limL[0],limL[1]+1):
        #     for iR in range(limR[0],limR[1]+1):
        #         if p.contains_point((iL,iR)) or [iL,iR] in caminho:
        #             inside += 1

        # ans[part-1] = inside
        print_mapa_color(mapa)
        # print(len(caminho))
        ans[part-1] = Area(caminho)
            
        print(f'part{part}: {ans[part-1]}')

def Area(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

def print_map(mapa):
    for line in mapa:
        for ch in line:
            print(ch, end='')
        print()

def print_mapa_color(mapa):
    espelhos = '\/|-'
    CEND    = '\33[0m'
    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    print('\t','-'*len(mapa[0]))
    for i,line in enumerate(mapa):
        out = str(i) + '\t|'
        for ch in line:
            
            color = CRED if ch == '#' else CGREEN
            out += color + str(ch) + CEND
        out += '|'
        print(out.replace(' ',''))
    
    print('\t','-'*len(mapa[0]))

if __name__ == "__main__":
    nday = 18

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


