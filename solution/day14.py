"""Solution of day1 - AoC2023."""
import sys

def solve(data):
    mapa = [list(line) for line in data.splitlines()]

    ans = 0
    for part in [1, 2]:
        print_map(rotacao(mapa,0))
        print('rot')
        print_map(rotacao(mapa,2))
        print(f'part{part}: {ans}')

def print_map(mapa):
    for line in mapa:
        for ch in line:
            print(ch, end='')
        print()

def rotacao(mapa, n=1):
    
    nR = len(mapa[0])
    nL = len(mapa)
    new_map = mapa
    for _ in range(n):
        new_map = []
        for dR in range(nR,0,-1):
            row = [line[dR-1] for line in mapa]
            new_map.append(row)
        if n > 1:
            mapa = new_map
    return new_map

def shift_all(mapa):
    new_mapa = []
    for line in mapa:
        pass


if __name__ == "__main__":
    nday = 14

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


