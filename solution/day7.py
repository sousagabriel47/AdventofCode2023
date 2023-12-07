"""Solution of day1 - AoC2023."""
import sys



def solve(data):
    data = data.splitlines()
    

    for part in [1, 2]:
        if part == 1:
            hand_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        else:
            hand_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

        hands = [line.split() for line in data]
        hand_order = hand_order[::-1]
        hand_order_num = ['{:01X}'.format(n) for n in range(len(hand_order))]

        rank = []
        for hand,bid in hands:
            cards = set(hand)
            cards_conut = ['0','0','0','0','0']
            j_count = 0
            for id,card in enumerate(cards):
                if part == 1:
                    cards_conut[id] = str(hand.count(card))
                else:
                    if card == 'J':
                        j_count += hand.count(card)
                    else:
                        cards_conut[id] = str(hand.count(card))
            cards_conut = sorted(cards_conut, reverse=True)
            cards_conut[0] = str(j_count + int(cards_conut[0]))
            rank.append([''.join(cards_conut), hand, bid])
        
        rank = sorted(rank, key=lambda x:x[0])

        tipos = {hand[0]: [] for hand in rank}
        for hand in rank:
            tipos[hand[0]].append(hand[1:])
        bid_list = []
        for hands in tipos.values():
            bid_aux = []
            for hand,bid in hands:
                con_hand = ''
                for ch in hand:
                    con_hand += hand_order_num[hand_order.index(ch)]
                bid_aux.append([con_hand, bid])
            bid_list.extend([bid for _, bid in sorted(bid_aux, key=lambda x: int(x[0], 16))])
        
        winners = [int(bid) * r for r,bid in enumerate(bid_list, 1)]
        print(f'part{part}: {sum(winners)}')

        




if __name__ == "__main__":
    nday = 7
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


