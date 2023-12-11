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
                else:
                    closed = True
                if it < MAX__IT:
                    it += 1
                else:
                    break
            if loop:
                ans = len(caminho)/2
        

        print(f'part{part}: {ans}')
        




if __name__ == "__main__":
    nday = 10
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


