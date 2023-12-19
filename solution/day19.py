"""Solution of day1 - AoC2023."""
import sys
import os
from time import sleep
from matplotlib.path import Path




def solve(data):
    work_list, in_list = data.split('\n\n')
    ans = [0,0]
    print(work_list.splitlines())
    
    in_list = in_list.splitlines()


    work_list = {work.split('{')[0]: work.split('{')[1].replace('}','') for work in work_list.splitlines()}
    in_list = [input.replace('{','').replace('}','').split(',') for input in in_list]
    print(work_list)

    
    for part in [1,2]:
        
            
        print(f'part{part}: {ans[part-1]}')


if __name__ == "__main__":
    nday = 19

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


