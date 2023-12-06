"""Solution of day1 - AoC2023."""
import sys



def solve(data):
    data = data.splitlines()
    lineT = data[0].split(':')[1].split()
    lineD = data[1].split(':')[1].split()

    

    
    for part in [1,2]:
        total = 1
        if part == 1:
            races = [[int(t),int(d)] for t, d in zip(lineT, lineD)]
        else:
            races = [[int(''.join(lineT)),int(''.join(lineD))]]

        for t,d in races:
            buttons = [(t - tCarga)*tCarga for tCarga in range(1, t+1) if (t - tCarga)*tCarga > d]
            print(f'{d} --> {len(buttons)}')
            if len(buttons):
                total *= len(buttons)
        print(f'part{part}: {total}')


if __name__ == "__main__":
    nday = 6
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


