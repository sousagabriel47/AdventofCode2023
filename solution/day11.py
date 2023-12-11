"""Solution of day1 - AoC2023."""
import sys

def solve(data):
    data = data.splitlines()
    universe = [list(line) for line in data]


    #print(connections)
    ans = 0
    for part in [1,2]:
        if part == 1:
            universe_expand = expandir(universe)
        print(f'part{part}: {ans}')
        
def expandir(universe):

    expand = []

    lenL = len(universe)
    lenR = len(universe[0])
    dupL = 0
    dupR = 0
    r = []
    for iR in range(lenR):
        if '#' not in [line[iR] for line in universe]:
            r.append(iR)
            # newline = universe[iR]
            # newline.insert(iR + dupR,'.')
            # expand.append(newline)
            dupR += 1
    for iR in range(lenR):
        newline = universe[iR]
        newline.insert(iR + dupR,'.')
        expand.append(newline)
        dupR += 1
    
    
    print(r)
    print_map(expand)
    print('-----------')
    for iL,line in enumerate(universe):
        if '#' not in line:
            expand.append(line)
            expand.append(line)
            dupL += 1
        else:
            expand.append(line)



    print(dupL, dupR)
    print_map(expand)

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


