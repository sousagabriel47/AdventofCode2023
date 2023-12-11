"""Solution of day1 - AoC2023."""
import sys

def solve(data):
    data = data.splitlines()
    universe = [list(line) for line in data]


    #print(connections)
    ans = 0
    for part in [1,2]:
        if part == 1:
            step = 1
        else:
            step = 2
        dictExpand = expandir(universe, step)
        print(dictExpand)
        listDist = calc_dist(dictExpand)
        ans = int(sum(listDist)/2)
        print(f'part{part}: {ans}')
        
def expandir(universe, step=0):

    expand = []

    lenL = len(universe)
    lenR = len(universe[0])
    expR = []
    expL = []



    for iR in range(lenR):
        if '#' not in [line[iR] for line in universe]:
            expR.append(iR)
    
    for iL,line in enumerate(universe):
        if '#' not in line:
            expL.append(iL)


    dictGalaxies = {}
    for iL,line in enumerate(universe):
        for iR, p in enumerate(line):
            if p == '#':
                nExpL = len([eL for eL in expL if iL > eL])
                nExpR = len([eR for eR in expR if iR > eR])
                
                dictGalaxies[f'{iL}_{iR}'] = [iL + nExpL*step, iR + nExpR*step]
    return dictGalaxies

def calc_dist(dictUniverse):
    dist = []

    for p1 in dictUniverse.values():
        for p2 in dictUniverse.values():
            dist.append(abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))
    return dist

def print_map(mapa):
    for line in mapa:
        for ch in line:
            print(ch, end='')

        print()

if __name__ == "__main__":
    nday = 11
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


