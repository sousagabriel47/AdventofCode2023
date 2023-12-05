"""Solution of day1 - AoC2023."""
import sys



def solve(data):
    data = data.splitlines()
    winners = [line.split(':')[1].split('|')[0].split() for line in data]
    mynum = [line.split(':')[1].split('|')[1].split() for line in data]
    total = 0
    for part in [1,2]:
        next_win = []
        next_nums = []
        next_cards = [1 for _,_ in enumerate(winners)]
        for idGame, numbers in enumerate(zip(winners, mynum)):
            win, my = numbers
            point = 0
            for mynumber in my:
                if mynumber in win:
                    if part == 1:
                        if point:
                            point *= 2
                        else:
                            point = 1
                    else:
                        point += 1
            if part == 1:
                total += point
            if part == 2:
                if point:
                    for idF in range(1,point+1):
                    
                        next_cards[idF + idGame] += 1 * next_cards[idGame]

                total = sum(next_cards)
        print(f'part{part}: {total}')


if __name__ == "__main__":
    nday = 4
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


