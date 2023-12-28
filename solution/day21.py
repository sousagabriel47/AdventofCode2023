"""Solution of day1 - AoC2023."""
import sys
from copy import copy
from functools import cache

def solve(data, mode):
    mapa = [list(line) for line in data.splitlines()]

    rocks = set()
    st_pos = []
    nL = len(mapa)
    nR = len(mapa[0])
    for iL in range(nL):
        for iR in range(nR):
            if mapa[iL][iR] == '#':
                rocks.add((iL,iR))
            elif mapa[iL][iR] == 'S':
                st_pos.append((iL, iR))



    base_rocks = copy(rocks)
    ans = [0,0]
    mapa_len = ((0, nL), (0, nR))
    base_len = copy(mapa_len)
    for part in [1,2]:
        garden = set(st_pos)
        garden_din = []
        if part == 1:
            for _ in range(64):
                garden = next_garden(garden, rocks, mapa_len, part)
            if mode == 'teste':
                print_mapa_color(mapa_len, rocks, garden)
            ans[part-1] = len(garden)
        else:
            for _ in range(400):
                garden = next_garden(garden, rocks, mapa_len, part)
                garden_din.append(len(garden))      
                dir = check_expansao(mapa_len,garden)
                if dir:
                    rocks, mapa_len = expandir_rocks(mapa_len, base_len, base_rocks, rocks, dir)
                
                #print_mapa_color(mapa_len, rocks, garden)
            
            transitorio = 0
            total = 26501365
            step = total - transitorio
            step2 = step%nL - 1
            serie = []
            diff = []
            diff2 = []



            for el in garden_din[transitorio+step2::nL]:
                serie.append(el)
            for i in range(1, len(serie)):
                diff.append(serie[i]-serie[i-1])
            for i in range(1, len(diff)):
                diff2.append(diff[i]-diff[i-1])
            A = diff2[0]//2
            B = serie[1] - serie[0] - 3*A
            C = serie[0] - A - B
            n = total//step
            n = total // nL + 1
            ans[part-1] = A*n**2 + B*n + C

            #   605241154569194 low
            #   605241195433695 low
            #   605247138198755 2STAR
            #   605247179063458 high


            
        print(f'part{part}: {ans[part-1]}')


def expandir_rocks(mapa_len, base_len, base_rocks, atual_rocks, dir_exp = []):
    #[minL,maxL]    [minR,maxR]


    lenL, lenR = mapa_len
    minL, maxL = lenL
    minR, maxR = lenR


    baseL, baseR = base_len

    deltaL = baseL[1] - baseL[0]
    deltaR = baseR[1] - baseR[0]


    if 'D' in dir_exp:
        for i in range(int((maxR - minR)/deltaR)):
            new = {(rL - deltaL + minL, rR + minR + i*deltaR) for rL, rR in base_rocks}
            atual_rocks = {*atual_rocks, *new}
        minL = minL - deltaL


    if 'U' in dir_exp:
        for i in range(int((maxR - minR)/deltaR)):
            new = {(rL + maxL,  rR + minR + i*deltaR) for rL, rR in base_rocks}
            atual_rocks = {*atual_rocks, *new}
        maxL = maxL + deltaL

    if 'L' in dir_exp:
        for i in range(int((maxL - minL)/deltaL)):
            new = {(rL + minL + i*deltaL, rR - deltaR + minR) for rL, rR in base_rocks}
            atual_rocks = {*atual_rocks, *new}
        minR = minR - deltaR
    if 'R' in dir_exp:
        for i in range(int((maxL - minL)/deltaL)):
            new = {(rL + minL + i*deltaL, rR + maxR) for rL, rR in base_rocks}
            atual_rocks = {*atual_rocks, *new}
        maxR = maxR + deltaR





    lenL, lenR = mapa_len
    lenL = (minL, maxL)
    lenR = (minR, maxR)

    next_len = (lenL, lenR)
    return atual_rocks, next_len

def check_expansao(mapa_len, garden):
    dir_exp = []
    lenL, lenR = mapa_len
    minL, maxL = lenL
    minR, maxR = lenR
    gardenL = [p[0] for p in garden]
    gardenR = [p[1] for p in garden]
    D_LIM = 0
    if (min(gardenL) - D_LIM) <= minL:
        dir_exp.append('D')
    if (max(gardenL) + D_LIM) >= maxL:
        dir_exp.append('U')
    if (min(gardenR) - D_LIM) <= minR:
        dir_exp.append('L')
    if (max(gardenR) + D_LIM) >= maxR:
        dir_exp.append('R')

    return dir_exp

def print_mapa_color(mapa_len, rocks, garden):
    CEND    = '\33[0m'
    CWHITE  = '\33[37m'
    CRED    = '\33[31m'
    CRED2    = '\33[41m'
    CGREEN  = '\33[32m'

    lenL, lenR = mapa_len
    minL, maxL = lenL
    minR, maxR = lenR
    print()
    print()

    for iL in range(minL, maxL):
        line = ''
        print(iL, end='\t')
        for iR in range(minR, maxR):
            if [iL, iR] in rocks:
                line += CRED + '#' + CEND
            elif [iL, iR] in garden:
                line += CGREEN + 'O' + CEND
            else:
                line += CWHITE + '.' + CEND
        print(line.replace(' ', ''))
           
def next_garden(last_garden, rocks, mapa_len, part):
    next = set()
    lenL, lenR = mapa_len
    minL, maxL = lenL
    minR, maxR = lenR

    for garden in last_garden:
        pL, pR = garden
        for mL, mR in ((1,0),(0,1),(-1,0),(0,-1)):
            if (((pL+mL, pR+mR) not in rocks) and 
                ((pL+mL, pR+mR) not in next)):
                if part == 1:
                    if (((pL + mL) in range(minL, maxL)) and
                        ((pR + mR) in range(minR, maxR))):
                        next.add((pL+mL, pR+mR))
                else:
                    next.add((pL+mL, pR+mR))
                        
    return next

if __name__ == "__main__":
    nday = 21
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


