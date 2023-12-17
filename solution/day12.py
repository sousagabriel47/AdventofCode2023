"""Solution of day1 - AoC2023."""
import sys

def solve(data):
    data = data.splitlines()
    record = [line.split() for line in data]
    reg = [line[0] for line in record]
    padrao = [list(map(int,line[1].split(','))) for line in record]

    ans = 0
    for part in [1]:
        for r, p in zip(reg, padrao):
            nX = r.count('?')
            l_padroes = ['#'*n for n in p]
            print(r, nX, l_padroes)
        print(f'part{part}: {ans}')


if __name__ == "__main__":
    nday = 12

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


