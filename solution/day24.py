"""Solution of day1 - AoC2023."""
import sys
from os import system
from copy import deepcopy



def solve(data, mode):
    hailstones = [line for line in data.splitlines()]
    ans = [0,0]
    for part in [1,2]:
        print(f'part{part}: {ans[part-1]}')
    
if __name__ == "__main__":
    nday = 24
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


