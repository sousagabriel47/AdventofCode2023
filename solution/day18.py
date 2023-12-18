"""Solution of day1 - AoC2023."""
import sys
import os
from time import sleep
import matplotlib.pyplot as plt
from matplotlib.path import Path




def solve(data):
    movimentos = [line.split() for line in data.splitlines()]
    ans = [0,0]
    

    mov = {'R': [0,1], 'L':[0,-1], 'U': [-1,0], 'D':[1,0]}

    for part in [1]:
        if part==1:
            caminho = [[0,0]]
            for cmd, t, color in movimentos:
                vetor = mov[cmd]
                for _ in range(int(t)):
                    p = caminho[-1]
                    caminho.append([p[0] + vetor[0],p[1] + vetor[1]])
            # limites
            listL = [p[0] for p in caminho]
            listR = [p[1] for p in caminho]
            
            limL = [min(listL),max(listL)]
            limR = [min(listR),max(listR)]
            # # create mapa
            # mapa  = [list('.' * (limR[1] - limR[0] + 1)) for _ in range(limL[1] - limL[0] + 1)] 
            # for p in caminho:
            #     mapa[p[0]-limL[0]][p[1]-limR[0]] = '#'
            
            # #lines
            # p_count = []
            # inside = 0
            # for iL, line in enumerate(mapa):
            #     prev = '.'
            #     v = 0
            #     p_count.append([])
            #     for iR, ch in enumerate(line):
            #         if prev != ch and ch == '.':
            #             v += 1
            #         prev = ch
            #         p_count[iL].append(v%10)
                    

            p = Path(caminho)
            print(len(caminho))
            inside = 0
            for iL in range(limL[0],limL[1]):
                for iR in range(limR[0],limR[1]):
                    if [iL, iR] in caminho:
                        continue
                    if p.contains_point((iL,iR)):
                        inside += 1

            ans[part-1] = inside


            
        print(f'part{part}: {ans[part-1]}')

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


