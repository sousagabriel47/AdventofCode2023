"""Solution of day1 - AoC2023."""
import sys


def solve(data):
    mapa = [line for line in data.splitlines()]

    ans = 0
    for part in [1, 2]:
        ans = 0
        if part == 1:
            ans,mapa_aux = shift_all(rotacao(mapa,1))
        if part == 2:
            mapa_aux = mapa
            set_load = {}
            list_load = []
            total = 1000000000
            for ciclo in range(120):
                for _ in range(4):
                    mapa_aux2 = rotacao(mapa_aux,1)
                    _,mapa_aux = shift_all(mapa_aux2)
                load = calc_load(mapa_aux)
                if load in set_load.keys():
                    set_load[load] += 1
                else:
                    
                    set_load[load] = 1
                list_load.append(load)
            repeat = []
            for st in range(len(list_load)):
                for s in range(len(list_load) + st):
                    if len(list_load[st:st+s])>2 and list_load[st:st+s] == list_load[st+s:st+2*s]:
                        repeat = list_load[st:st+s]
                        break
                if repeat:
                    break
            ans = repeat[(total - st -1) % s]
        print(f'Part{part}: {ans}')

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
        for dR in range(nR):
            row = [line[dR] for line in mapa[::-1]]
            new_map.append(row)
        if n > 1:
            mapa = new_map
    return new_map

def calc_load(mapa):
    load = 0
    nL = len(mapa)
    for iL,line in enumerate(mapa):
        load += (nL - iL) * line.count('O')
    return load     

def shift_all(mapa):
    new_mapa = []
    for line in mapa:
        new_line = []
        for seg in ''.join(line).split('#'):
            if 'O' not in seg:
                new_line.append(''.join(seg))
            else:
                new_line.append(''.join(sorted(seg)))
        new_mapa.append('#'.join(new_line))
    
    nR = len(new_mapa[0])
    load = 0
    for dR in range(nR):
        load += (dR+1) * ([line[dR] for line in new_mapa].count('O'))
    return load, new_mapa


if __name__ == "__main__":
    nday = 14

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


