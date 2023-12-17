"""Solution of day1 - AoC2023."""
import sys
import os

def solve(data):
    mapa = [list(line) for line in data.splitlines()]
    ans = [0,0]
    os.system('cls')
    for part in [1]:
        caminho = []
        if part==1:
            p_st = [0,0]
            v_st = '>'
            caminho.append([p_st,v_st])
        print_caminho(mapa, caminho)
                    
                
        print(f'part{part}: {ans[part-1]}')

def print_caminho(mapa, caminho):
    for p in caminho:
        print(p)
        coor, v = p
        mapa[coor[0]][coor[1]] = v
    print_mapa_color(mapa)

def print_mapa_color(mapa):
    espelhos = '\/|-'
    caminho = '><^V'
    CEND    = '\33[0m'
    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    
    for i,line in enumerate(mapa):
        out = str(i) + '\t'
        for ch in line:
            
            color = CRED if ch in espelhos else CGREEN if ch in caminho else CBLACK
            out += color + str(ch) + CEND
        print(out.replace(' ',''))

if __name__ == "__main__":
    nday = 16

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


