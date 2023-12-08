"""Solution of day1 - AoC2023."""
import sys
from math import lcm

MAX_STEP = 1000000

def solve(data):
    data = data.splitlines()
    list_cmds = data[0]
    list_nodes = data[2:]
    for clean in ['=', '(', ')', ',']:
        list_nodes = [node.replace(clean,'') for node in list_nodes]
    list_nodes = [node.split() for node in list_nodes]
    nodes = {node: {'L': destL, 'R': destR} for node, destL, destR in list_nodes}
    #print(nodes)
    for part in [1,2]:
        step = 0
        len_cmd = len(list_cmds)
        if part == 1:
            atual_node = 'AAA'
            end_node = 'ZZZ'
            for step in range(MAX_STEP):
                cmd = list_cmds[step % len_cmd]
                next_node = nodes[atual_node][cmd]

                # if step % 100 == 0:
                #     print(f'{atual_node}:{cmd} -> {next_node}')
                atual_node = next_node

                if next_node == 'ZZZ':
                    ans = step+1
                    break
        else:
            atual_node_list = [node for node in nodes.keys() if node[2] == 'A']
            end_node = 'Z'
            steps = [0 for _ in range(len(atual_node_list))]
            for step in range(MAX_STEP):
                cmd = list_cmds[step % len_cmd]
                next_node_list = [nodes[atual_node][cmd] for atual_node in atual_node_list]
                check_list = [next[2] == end_node for next in next_node_list]
                steps = [step+1 if next else el_step for el_step, next in zip(steps, check_list)]

                # for atual, next in zip(atual_node_list, next_node_list):
                #     print(f'{atual}:{cmd} -> {next}', end = '|')
                # print(check_list,steps)
                atual_node_list = next_node_list

                if all([atual_step != 0 for atual_step in steps]):
                    ans = lcm(*steps)
                    break
                
        print(f'part{part}: {ans}')

        




if __name__ == "__main__":
    nday = 8
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


