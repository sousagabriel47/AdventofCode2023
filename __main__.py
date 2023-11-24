"""Aoc2023."""
import sys

if __name__ == "__main__":
    day = int(sys.argv[1])
    
    with open(f'./data/{sys.argv[2]}/{day}','r') as f:
        data = f.read()

    eval(f'from ./solution import Solution_day{day}')
    solution = eval(f'Solution_day{day}(data)')