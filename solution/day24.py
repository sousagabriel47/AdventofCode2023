"""Solution of day1 - AoC2023."""
import sys
from os import system
from copy import deepcopy



def solve(data, mode):
    hailstones = [line.replace(' ','').split('@') for line in data.splitlines()]
    hailstones = [[tuple(map(int,line[0].split(','))),
                   tuple(map(int,line[1].split(',')))] 
                  for line in hailstones]

    ans = [0,0]
    for part in [1]:
        t0 = 7
        t1 = 27
        
        for hail in hailstones:
            p0, v0 = hail
            p0x, p0y, p0z = p0
            v0x, v0y, v0z = v0
            for hail2 in [h for h in hailstones if h != hail]:
                p1, v1 = hail2
                p1x, p1y, p1z = p1
                v1x, v1y, v1z = v1
                print(v0x*t2 + p0x, v0y*t2 + p0y)
                rX0 = range(p0x + t0*v0x, p0x + t1*v0x+1)
                rX1 = range(p1x + t0*v1x, p1x + t1*v1x+1)
                if (v0x - v1x):
                    t = (p1x - p0x)/(v0x - v1x)
                    print(hail, hail2, t, t*v0y + p0y, t*v1y + p1y)
                # p0X + t*v0X = p1X + t*v1X --> t*(v0X - v1X) = p1X - p0X --> t = (p1X - p0X)/(v0X - v1X)
                # print(f'Hail0: X[{p0x + t0*v0x}:{p0x + t1*v0x}] --> Hail1: X[{p1x + t0*v1x}:{p1x + t1*v1x}]') 
                # print(f'Hail0: Y[{p0x + t0*v0x}:{p0x + t1*v0x}] --> Hail1: Y[{p1x + t0*v1x}:{p1x + t1*v1x}]') 


        print(f'part{part}: {ans[part-1]}')
    
if __name__ == "__main__":
    nday = 24
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


