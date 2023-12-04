"""Solution of day1 - AoC2023."""
import sys

def solve(data):
    data = data.splitlines()
    schematic = [list(line) for line in data]

    symb = ['*','#','+','$']
    directions = [[0,0],[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    lenL = len(schematic)
    lenR = len(schematic[0])
    
    numbers = {}

    for iL, line in enumerate(schematic):
        num = ''
        coord = []
        for iR, point in enumerate(line):
            if point.isdigit():
                num += point
                coord.append([iL,iR])
            else:
                if num != '':
                    for cL, cR in coord:
                        numbers[f'{cL}_{cR}'] = {}
                        numbers[f'{cL}_{cR}']['num'] = int(num)
                        numbers[f'{cL}_{cR}']['coords'] = coord
                num = ''
                coord = []
        if num != '':
            for cL, cR in coord:
                numbers[f'{cL}_{cR}'] = {}
                numbers[f'{cL}_{cR}']['num'] = int(num)
                numbers[f'{cL}_{cR}']['coords'] = coord


    for part in [1, 2]:

        sum_dig = 0
        check = []
        for iL, line in enumerate(schematic):
            for iR, point in enumerate(line):
                if part == 1:
                    if not point.isdigit() and point != '.':
                        #print(point, iL, iR, end=' -> ')
                        for dL,dR in directions:
                            pL, pR = [iL + dL, iR + dR]
                            if pL >= 0 and pR >= 0 and pL <= (lenL - 1) and pR <= (lenR - 1) and [pL, pR] not in check:
                                #print(schematic[pL][pR], end='')
                                if schematic[pL][pR].isdigit():
                                    #print(f'{pL}_{pR}', numbers[f'{pL}_{pR}']['num'], end=', ')
                                    check.extend(numbers[f'{pL}_{pR}']['coords'])
                                    sum_dig += numbers[f'{pL}_{pR}']['num']
                                    #print(check, end='')
                        #print()
                if part == 2:
                    if point == '*':
                        print(point, iL, iR, end=' -> ')
                        gear_ratio = 1
                        gear = 0
                        for dL,dR in directions:
                            pL, pR = [iL + dL, iR + dR]
                            if pL >= 0 and pR >= 0 and pL <= (lenL - 1) and pR <= (lenR - 1) and [pL, pR] not in check:
                                #print(schematic[pL][pR], end='')
                                if schematic[pL][pR].isdigit():
                                    print(f'{pL}_{pR}', numbers[f'{pL}_{pR}']['num'], end=', ')
                                    check.extend(numbers[f'{pL}_{pR}']['coords'])
                                    gear_ratio *= numbers[f'{pL}_{pR}']['num']
                                    gear += 1
                                    #print(check, end='')
                        if gear >= 2:
                            sum_dig += gear_ratio
                        print()
        print(f'part{part}: {sum_dig}')




if __name__ == "__main__":
    nday = 3
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


