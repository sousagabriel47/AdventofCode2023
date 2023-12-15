"""Solution of day1 - AoC2023."""
import sys

def solve(data):
    hash_list = data.split(',')

    for part in [1, 2]:
        ans = 0
        for hash in hash_list:
            v = 0
            prev = 0
            for ch in hash:
                ch_v = ord(ch)
                v = ((prev + ch_v)*17) % 256
                prev = v
            #print(hash, v)
            ans += v
        print(f'part{part}: {ans}')




if __name__ == "__main__":
    nday = 15

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


