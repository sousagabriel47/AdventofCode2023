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
    for part in [1]:
        inf = 200000000000000
        sup = 400000000000000
        x, y = sp.symbols('x,y')
        eq = []
        total = 0
        for id, hail in enumerate(hailstones):
            p0, v0 = hail
            p0x, p0y, p0z = p0
            v0x, v0y, v0z = v0
            m0 = v0y/v0x
            y00 = p0y - m0*p0x
            eq.append((id, p0x, v0x, sp.Eq(m0*x - y, -y00)))
        
        # list_solve = [(sp.solve((eq1, eq2),(x, y))) 
        #               for idEq1, p0, v0, eq1 in iter(eq) 
        #               for idEq2, p1, v1, eq2 in iter(eq[idEq1+1:])]
        # print(list_solve)
        for idEq1, p0, v0, eq1 in eq:
            for idEq2, p1, v1, eq2 in eq[idEq1+1:]:
                a = sp.solve((eq1, eq2),(x, y))
                if a:
                    t0 = (a[x] - p0)/v0
                    t1 = (a[x] - p1)/v1
                    print(idEq1, idEq2, a[x], a[y], t0, t1)
                    if ((inf<=a[x]<=sup and inf<=a[y]<=sup) and
                        t0 > 0 and
                        t1 > 0):
                        total += 1
        ans[part-1] = total
            # print(hail, y00, m0)
            # eq0 = sp.Eq(m0*x + y, y00)
            # for hail2 in [h for h in hailstones if h != hail]:
            #     p1, v1 = hail2
            #     p1x, p1y, p1z = p1
            #     v1x, v1y, v1z = v1
            #     m1 = v1y/v1x
            #     y01 = p1y - m1*p1x
            #     print(hail2, y01, m1)
                
            #     eq1 = sp.Eq(m1*x + y, y01)
            #     an = sp.solve((eq0, eq1),(x, y))
            #     print(an)
            #     if m0 != m1:
            #         x = (y01 - y00)/(m0 - m1)


        print(f'part{part}: {ans[part-1]}')
    
if __name__ == "__main__":
    nday = 24
    mode = sys.argv[1]
    with open(f'./solution/data/{mode}/{nday}','r') as f:
        data = f.read()
    solve(data, mode)


