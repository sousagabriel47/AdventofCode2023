"""Solution of day1 - AoC2023."""
import sys



def solve(data):
    data = data.splitlines()
    winners = [line.split(':')[1].split('|')[0].split() for line in data]
    mynum = [line.split(':')[1].split('|')[1].split() for line in data]
    total = 0
    for part in [2]:
        next_win = []
        next_nums = []
        next_cards = [[idGame] for idGame,_ in enumerate(winners)]
        list_cards = []
        organize_cards = []
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
            if part == 2:
                if point:
                    list_cards.append(idGame)
                    for idF in range(1,point+1):
                        next_cards[idGame].append(idF + idGame) 
                        list_cards.append(idF + idGame) 

            print(f'Card {idGame}: {point} {next_cards[idGame]}')
            total += point

        for cards in next_cards:
            print(lista_unica(next_cards, cards))
        print(organize_cards)
        print(f'part{part}: {total}')


def lista_unica(next_cards, lista):
    l = []
    if len(lista) == 1:
        return next_cards[lista[0]]
    else:
        for el in lista:
            l.append(el)
            l.append(lista_unica(next_cards, lista[1:]))
    return l


if __name__ == "__main__":
    nday = 4
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


