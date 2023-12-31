"""Solution of day1 - AoC2023."""
import sys
from os import system
from copy import deepcopy
import sympy as sp


def solve(data, mode):
    hailstones = [line.replace(' ','').split('@') for line in data.splitlines()]
    hailstones = [[tuple(map(int,line[0].split(','))),
                   tuple(map(int,line[1].split(',')))] 
                  for line in hailstones]

    ans = [0,0]
    if mode == 'teste':
        inf = 7
        sup = 27
    else:
        inf = 200000000000000
        sup = 400000000000000
    eq = []
    hail_eq = []
    total = 0
    vxmax = vymax = vzmax = -10**10
    vxmin = vymin = vzmin = 10**10
    xr, yr, zr, vrx, vry, vrz, t0, t1, t2 = sp.symbols('xr, yr, zr, vrx, vry, vrz, t0, t1, t2')
    t = [t0,t1,t2]
    for id, hail in enumerate(hailstones):
        p0, v0 = hail
        p0x, p0y, p0z = p0
        v0x, v0y, v0z = v0

        m0 = v0y/v0x
        y0 = p0y - m0*p0x
        eq.append((id, p0x, v0x, m0, y0))

        if id < 3:
            # assumindo que tn temos qie
            # p0x + v0x*t0 = rx + vrx*t0
            # p1x + v1x*t1 = rx + vrx*t1
            # p2x + v2x*t2 = rx + vrx*t2
            hail_eq.append(sp.Eq(xr + vrx*t[id],p0x + v0x*t[id]))
            hail_eq.append(sp.Eq(yr + vry*t[id],p0y + v0y*t[id]))
            hail_eq.append(sp.Eq(zr + vrz*t[id],p0z + v0z*t[id]))
    for part in [1, 2]:
           
        if part==1:
            list_solve = [1 for idEq1, p0, v0, m0, y00 in eq[:-1] for idEq2, p1, v1, m1, y01 in eq[idEq1+1:]
                        if ((m0 != m1) and
                            (inf<=(y00-y01)/(m1-m0)<=sup and
                            inf<=y00 + m0*((y00-y01)/(m1-m0))<=sup) and
                            ((y00-y01)/(m1-m0) - p0)/v0 > 0 and
                            ((y00-y01)/(m1-m0) - p1)/v1 > 0)]
            ans[part-1] = sum(list_solve)
        else:
            ans[part-1] = sum(sp.solve(hail_eq, xr, yr, zr, vrx, vry, vrz, t0, t1, t2)[0][:3])

        
        print(f'part{part}: {ans[part-1]}')
    
if __name__ == "__main__":
    nday = 24
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


