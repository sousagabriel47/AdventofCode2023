"""Solution of day1 - AoC2023."""
import sys
import os
from collections import deque
import copy
from time import sleep

def solve(data):
    mapa = [list(line) for line in data.splitlines()]
    ans = [0,0]
    os.system('cls')

    mov = {'>': {'.':[['>',[0,1]]],'\\':[['v',[1,0]]],'/': [['^', [-1,0]]],'|':[['^', [-1,0]],['v', [1,0]]], '-':[['>', [0,1]]]},
           '<': {'.':[['<',[0,-1]]],'\\':[['^',[-1,0]]],'/': [['v', [1,0]]],'|':[['^', [-1,0]],['v', [1,0]]], '-':[['<', [0,-1]]]},
           '^': {'.':[['^',[-1,0]]],'\\':[['<',[0,-1]]],'/': [['>', [0,1]]],'|':[['^', [-1,0]]], '-':[['<', [0,-1]],['>', [0,1]]]},
           'v': {'.':[['v',[1,0]]],'\\':[['>',[0,1]]],'/': [['<', [0,-1]]],'|':[['v', [1,0]]], '-':[['<', [0,-1]],['>', [0,1]]]}}
    nL = len(mapa)
    nR = len(mapa[0])
    color_map = copy.deepcopy(mapa)
    for part in [1]:
        caminho = deque()
        caminho_total = set()
        visit = set()
        if part==1:
            p_st = [0,0]
            v_st = [0,1]
            ch = '>'
            for i in range(2000000):
                if i == 0:
                    p, v, ch = p_st, [0,0], ch
                else:
                    if not caminho:
                        break
                    p, v, ch = caminho.popleft()
                p_atual = [p[0] + v[0], p[1] + v[1]]
                next_p = mapa[p_atual[0]][p_atual[1]]
                if (tuple(p_atual), ch) in visit:
                    continue
                visit.add((tuple(p_atual), ch))
                caminho_total.add(tuple(p_atual))
                next_list = mov[ch].get(next_p)
                for next in next_list:
                    next_ch, next_v = next
                    next_p = [next_v[0] + p_atual[0], next_v[1] + p_atual[1]]
                    if next_p[0] >= 0 and next_p[0] < nL and next_p[1] >= 0 and next_p[1] < nR:
                        caminho.append([p_atual,next_v,next_ch])
                
            ans[part-1] = len(visit)                  
                
        print(f'part{part}: {ans[part-1]}')
        x = []
        y = []
        for a, b in caminho_total:
            x.append(int(a))
            y.append(int(b))
        print(max(x),min(x))
        print(max(y),min(y))
        print(len(caminho_total))

def print_caminho(mapa, caminho):
    espelhos = '\/|-'
    for p in caminho[:-1]:
        coor, ch = p
        if mapa[coor[0]][coor[1]] not in espelhos:
            mapa[coor[0]][coor[1]] = ch
    if mapa[caminho[-1][0][0]][caminho[-1][0][1]] not in espelhos:
        mapa[caminho[-1][0][0]][caminho[-1][0][1]] = '*'
    print_mapa(mapa)

def print_mapa_color(mapa):
    espelhos = '\/|-'
    caminho = '><^v'
    especial = '*'
    CEND    = '\33[0m'
    CWHITE  = '\33[37m'
    CRED    = '\33[31m'
    CRED2    = '\33[41m'
    CGREEN  = '\33[32m'
    
    for i,line in enumerate(mapa):
        out = str(i) + '\t'
        for ch in line:
            
            color = CRED if ch in caminho else CRED2 if ch in especial else CGREEN if ch in espelhos else CWHITE
            out += color + str(ch) + CEND
        print(out.replace(' ',''))

def print_mapa(mapa):
    for i,line in enumerate(mapa):
        print(str(i), '\t', end='')
        for ch in line:
            print(ch, end='')
        print()

if __name__ == "__main__":
    nday = 16

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


