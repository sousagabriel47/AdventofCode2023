"""Solution of day1 - AoC2023."""
import sys

def solve(data):
    data = data.splitlines()
    
    for part in [1,2]:
        games = []
        for id, game in enumerate(data):
            red = []
            blue = []
            green = []
            cubes = game.split(':')[1].split(';')
            cubes = [cube.split(', ') for cube in cubes]
            nok = False
            for cube in cubes:

                for color in cube:
                    value, cor = color.split()
                    if cor == 'green':
                        thr = 13
                        green.append(int(value))
                    if cor == 'red':
                        thr = 12
                        red.append(int(value))
                    if cor == 'blue':
                        thr = 14
                        blue.append(int(value))
                    if int(value) > thr:
                        nok = True
                if part==1 and nok:
                    break
            if part == 1:
                if not nok:
                    games.append(id+1)
            else:
                games.append(max(red)*max(green)*max(blue))

        print(f'part{part}: {sum(games)}')




if __name__ == "__main__":
    nday = 2
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


