"""Solution of day1 - AoC2023."""
import sys

def solve(data):
    padroes = data.split('\n\n')
    padroes = [list(map(list,padrao.splitlines())) for padrao in padroes]

    ans = 0
    dict_reflection = {}
    for part in [1, 2]:
        reflection = []
        for id, padrao in enumerate(padroes):
            if part==1:
           
                vert = check_vertical(padrao, part)
                hort = check_horizontal(padrao, part)
                
                dict_reflection[id] = [vert, hort]
                print_refletion(padrao,[vert, hort])
            else:
                vert = check_vertical(padrao, part, dict_reflection[id][0])
                hort = check_horizontal(padrao, part, dict_reflection[id][1])
                if vert + hort == 0:
                    print_refletion(padrao,[vert, hort])

            reflection.append(vert + hort*100)
        ans = sum(reflection)
        print(f'part{part}: {ans}')

def print_refletion(padrao, reflection):
    v, h = reflection
    if v != 0:
        pos = v-1
        for i in range(len(padrao[0])):
            if i != pos and i!= pos+1:
                print(' ', end='')
            if i == pos:
                print('>', end='')
            if i == pos+1:
                print('<', end='')
        print()
        for line in padrao:
            for ch in line:
                print(ch, end='')
            print()
        
        for i in range(len(padrao[0])):
            if i != pos and i!= pos+1:
                print(' ', end='')
            if i == pos:
                print('>', end='')
            if i == pos+1:
                print('<', end='')
        print()
    elif h!=0:
        pos = h-1
        
        for i,line in enumerate(padrao):
            if i != pos and i!= pos+1:
                print(' ', end='')
            if i == pos:
                print('V', end='')
            if i == pos+1:
                print('^', end='')
            for ch in line:
                print(ch, end='')
            if i != pos and i!= pos+1:
                print(' ', end='')
            if i == pos:
                print('V', end='')
            if i == pos+1:
                print('^', end='')
            
            print()



def check_vertical(padrao, part, ignore=0):
    nrow = 0
    nR = len(padrao[0])
    check = False
    count_smudge = 0
    for iR in range(1,nR):
        if iR == ignore:
            continue

        r1 = [line[iR] for line in padrao]
        r2 = [line[iR-1] for line in padrao]

        

        if part == 1:
            check_smudge = r1 == r2
        if part == 2:
            check_smudge, count_smudge = smudge(r1, r2)
            
        if check_smudge:
            
            dRTotal = iR if iR < nR/2 else nR - iR
            check = True
            if iR < nR - 1:
                for dR in range(1,dRTotal):

                    if part==1:
                        c = [line[iR + dR] for line in padrao] == [line[iR-1 - dR] for line in padrao]
                    if part==2:
                        c, s = smudge([line[iR + dR] for line in padrao], [line[iR-1 - dR] for line in padrao])
                        count_smudge += s
                    if  not c or count_smudge > 1:
                        check = False
                        break
        if check:
            nrow = iR
            break
    return nrow

def check_horizontal(padrao, part, ignore=0):
    nline = 0
    nL = len(padrao)
    check = False
    count_smudge = 0
    for iL in range(1,nL):
        if iL == ignore:
            continue

        l1 = padrao[iL]
        l2 = padrao[iL - 1]
        #print(nL, l1, l2, l1==l2)
        if part == 1:
            check_smudge = l1 == l2
        if part == 2:
            check_smudge, count_smudge = smudge(l1, l2)
        if check_smudge:
            dLTotal = iL if iL < nL/2 else nL - iL
            check = True
            
            if iL < nL - 1:
                for dL in range(1,dLTotal):
                    #print('\t',iL+dL,count_smudge, padrao[iL + dL], padrao[iL - 1 - dL], padrao[iL + dL] != padrao[iL - 1 - dL])
                    if part==1:
                        c = padrao[iL + dL] == padrao[iL - 1 - dL]
                    if part==2:
                        c, s = smudge(padrao[iL + dL], padrao[iL - 1 - dL])
                        count_smudge += s
                    if  not c or count_smudge > 1:
                        check = False
                        break
        if check:
            nline = iL
            break
    return nline

def smudge(l1, l2):

    if l1 == l2:
        return True, 0

    for i, p in enumerate(zip(l1, l2)):
        p1, p2 = p
        if p1 != p2:
            return [e1 == e2 for e1, e2 in zip(l1, l2)].count(False) == 1, 1

    return False, 0
            

if __name__ == "__main__":
    nday = 13

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


