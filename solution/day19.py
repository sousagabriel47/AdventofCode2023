"""Solution of day1 - AoC2023."""
import sys
import os
from time import sleep
from matplotlib.path import Path
import copy



def solve(data):
    work_list, in_list = data.split('\n\n')
    ans = [0,0]
    
    in_list = in_list.splitlines()


    work_list = {work.split('{')[0]: work.split('{')[1].replace('}','').split(',') for work in work_list.splitlines()}
    in_list = [input.replace('{','').replace('}','').split(',') for input in in_list]

    work_dict = {}
    for step, cond in work_list.items():
        work_dict[step] = []
        for c in cond:
            work_dict[step].append(c.split(':'))

    for part in [1,2]:
        no = 'in'
        if part == 1:
            for input in in_list:
                x,m,a,s = [int(el[2:]) for el in input]
                out = ''
                
                no = 'in'
                print(x,m,a,s, end=' --> ')
                while no not in 'AR':
                    print(no, end=',')
                    for teste in work_dict[no]:
                        if len(teste) == 2:
                            if eval(teste[0]):
                                no = teste[1]
                                break
                        else:
                            no = teste[0]
                            break
                print(no)
                if no == 'A':
                    ans[part-1] += x + m + a + s
        else:
            ranges = [[{'x':[1, 4000], 'm':[1, 4000], 'a':[1, 4000], 's':[1, 4000]},'in']]
            
            while not all([irange[1] in 'AR' for irange in ranges]):
                #iteracao
                valores, no = ranges.pop(0)
                test_list = [valores]            

                if no not in 'AR':
                    for teste in work_dict[no]:
                        # teste = ['s<1351','px']
                        value_teste = test_list.pop(0)
                        if len(teste) == 2:
                            var_test = teste[0][0]
                            limite = int(teste[0][2:])
                            cond = teste[0][1]
                            next_no = teste[1]
                            v_min, v_max = value_teste[var_test]
                            if v_min <= limite and limite <= v_max:
                                # v_min ... limite ... v_max
                                # cond > False: [v_min,limite] True [limite+1,v_max]
                                # cond < False: [limite,v_max] True [v_min,limite-1]
                                if cond == '>':
                                    #saida False
                                    value_teste.update({var_test : [v_min, limite]})
                                    test_list.append(value_teste)
                                    # saida True
                                    value_teste[var_test] = [limite+1, v_max]
                                    ranges.append([value_teste,next_no])
                                elif cond == '<':
                                    #saida False
                                    value_teste[var_test] = [limite,v_max]
                                    test_list.append(value_teste)
                                    # saida True
                                    value_teste_ok = copy.copy(value_teste)
                                    value_teste_ok[var_test] = [v_min,limite-1]
                                    ranges.append([value_teste_ok,next_no])
                                    
                            else:
                                test_list.append(value_teste) 
                        else:
                            ranges.append([value_teste,teste[0]])
            for irange in ranges:
                print(irange)
            

        print(f'part{part}: {ans[part-1]}')


if __name__ == "__main__":
    nday = 19

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


