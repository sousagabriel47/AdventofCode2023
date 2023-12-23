"""Solution of day1 - AoC2023."""
import sys
from copy import copy


def solve(data, mode):
    mapa = [list(line) for line in data.splitlines()]

    rocks = []
    st_pos = []
    nL = len(mapa)
    nR = len(mapa[0])
    for iL in range(nL):
        for iR in range(nR):
            if mapa[iL][iR] == '#':
                rocks.append([iL,iR])
            elif mapa[iL][iR] == 'S':
                st_pos.append([iL, iR])




    ans = [0,0]

    for part in [1,2]:
        garden = st_pos
        if mode == 'teste':
            print_mapa_color(nL, nR, rocks, garden)
        if part == 1:
            for _ in range(64):
                
                new_garden = next_garden(garden, rocks, nL, nR, part)
                garden = copy(new_garden)
            
            if mode == 'teste':
                print_mapa_color(nL, nR, rocks, garden)
                
            ans[part-1] = len(garden)
        else:
            garden_size = []
            for step in range(200):
                new_garden = next_garden(garden, rocks, nL, nR, part)
                print(step, len(new_garden))
                garden_size.append(len(new_garden))
                garden = copy(new_garden)
                

        print(f'part{part}: {ans[part-1]}')


def print_mapa_color(nL, nR, rocks, garden):
    CEND    = '\33[0m'
    CWHITE  = '\33[37m'
    CRED    = '\33[31m'
    CRED2    = '\33[41m'
    CGREEN  = '\33[32m'
    for iL in range(nL):
        line = ''
        print(iL, end='\t')
        for iR in range(nR):
            if [iL, iR] in rocks:
                line += CRED + '#' + CEND
            elif [iL, iR] in garden:
                line += CGREEN + 'O' + CEND
            else:
                line += CWHITE + '.' + CEND
        print(line.replace(' ', ''))
            
def next_garden(last_garden, rocks, nL, nR, part):
    next = []
    for garden in last_garden:
        pL, pR = garden
        for mL, mR in [[1,0],[0,1],[-1,0],[0,-1]]:
            if (([pL+mL, pR+mR] not in rocks) and 
                ([pL+mL, pR+mR] not in next)):
                if part == 1:
                    if (((pL + mL) in range(nL)) and
                        ((pR + mR) in range(nR))):
                        next.append([pL+mL, pR+mR])
                else:
                    next.append([pL+mL, pR+mR])
                        
    return next

if __name__ == "__main__":
    nday = 21
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


