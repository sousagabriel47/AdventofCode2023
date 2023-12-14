"""Solution of day1 - AoC2023."""
import sys

MAX__IT = 10e4

def solve(data):
    data = data.splitlines()
    pipe_map = [list(line) for line in data]

    connections = {}
    conn_types = {'|': [[-1,0],[1,0]],
                  '-': [[0,-1],[0,1]],
                  'L': [[-1,0],[0,1]],
                  'J': [[-1,0],[0,-1]],
                  '7': [[1,0],[0,-1]],
                  'F': [[1,0],[0,1]],
                  'S': [[-1,0],[1,0],[0,1],[0,-1]]}
    st_pos = ''
    for iL, line in enumerate(pipe_map):
        for iR, p in enumerate(line):
            if p != '.':
                if p == 'S':
                    st_key = f'{iL}_{iR}'
                    st_pos = [iL, iR]
                if p in conn_types.keys():
                    connections[f'{iL}_{iR}'] = [[iL+cL, iR+cR] for cL, cR in conn_types[p]]

    #print(connections)
    ans = 0
    for part in [1,2]:
        if part==1:
            for st_p in connections[st_key]:
                loop = False
                closed = False
                caminho = [st_pos, st_p]
                p_dict = f'{st_p[0]}_{st_p[1]}'
                p = st_p
                it = 0
                while not(loop or closed):
                    if p_dict in connections.keys():
                        if caminho[-2] in connections[p_dict]:
                            for conn in connections[p_dict]:
                                if conn not in caminho:
                                    p = conn
                                    p_dict = f'{conn[0]}_{conn[1]}'
                                    caminho.append(conn)
                                    break
                                if len(caminho) > 2:
                                    if f'{conn[0]}_{conn[1]}' == st_key:
                                        loop = True
                                        caminho.append(conn)
                    else:
                        closed = True
                    if it < MAX__IT:
                        it += 1
                    else:
                        break
                if loop:
                    ans = (len(caminho) - 1)/2
                    break
        else:
            #stt S
            pipe_map[st_pos[0]][st_pos[1]] = 'L'
            inside_map = [list([0]*len(pipe_map[0])) for _ in range(len(pipe_map))]
            
            inside_p = 0
            #remark
            for iL,line in enumerate(pipe_map):
                for iR,p in enumerate(line):
                    if [iL, iR] not in caminho:
                        pipe_map[iL][iR] = '.'
            print_map(pipe_map)
            for iL,line in enumerate(pipe_map):
                for iR,p in enumerate(line[:-1]):
                    if p == '.':
                        pontos_line = set([pR for pL,pR in caminho if pL == iL and pR < iR])
                        v = valor_ponto(pontos_line, line[:iR+1])
                        inside_map[iL][iR] = v
                        if v % 2:
                            inside_p += 1
            ans = inside_p


            print_map(inside_map)
        print(f'part{part}: {ans}')
        

def print_map(mapa):
    for line in mapa:
        for ch in line:
            print(ch, end='')
        print()

def valor_ponto(caminho, line):
    if not caminho:
        return 0
    
    if line[-1] != '.':
        return 0
    seg_caminho = []
    for pCaminho in caminho:
        seg_caminho.append(line[pCaminho])
    while '-' in seg_caminho:
        seg_caminho.remove('-')

    if seg_caminho.count('|') == len(seg_caminho):
        return len(seg_caminho)
    v = 0
    lat = False
    prev_conner = ''
    inside = {'F': {'7': 0, 'J': 1}, 'L': {'7': 1, 'J': 0}, }
    
    for p in seg_caminho:
        if p == '|':
            v += 1
            lat = False
        if not lat:
            if p in ['F','L']:
                lat = True
                prev_conner = p
        else:
            if p in ['7','J']:
                v += inside[prev_conner][p]
                lat = False
            else:
                lat = False
                continue
    return v



if __name__ == "__main__":
    nday = 10
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


