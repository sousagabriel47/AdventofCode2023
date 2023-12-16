"""Solution of day1 - AoC2023."""
import sys

def solve(data):
    hash_list = data.split(',')
    boxes = {}
    for part in [1, 2]:
        ans = 0
        for hash in hash_list:
            if part == 1:
                #print(hash, calc_hash(hash))
                ans += calc_hash(hash)
            else:
                hash_label = hash[:-1] if hash[-1] == '-' else hash[:-2]
                hash_box = calc_hash(hash_label)
                cmd = hash[-1] if hash[-1] == '-' else hash[-2]
                focal = 0 if hash[-1] == '-' else int(hash[-1])
                if cmd == '=':
                    if hash_box in boxes.keys():
                        if hash_label in [label for label, _ in boxes[hash_box]]:
                            if [hash_label,focal] not in boxes[hash_box]:
                                boxes[hash_box] = [[label, f] if hash_label != label else [label, focal] for label, f in boxes[hash_box]]
                            
                        else:
                            boxes[hash_box].append([hash_label, focal])
                                             
                    else:
                        boxes[hash_box]=[[hash_label, focal]]
                elif '-':
                    if hash_box in boxes.keys():
                        if hash_label in [label for label, _ in boxes[hash_box]]:
                            boxes[hash_box] = [[label,focal] for label, focal in boxes[hash_box] if label != hash_label]



                #print(hash, hash_box, cmd, focal, boxes)
        if part == 2:
            for box,lens in boxes.items():
                for i,len in enumerate(lens):
                    ans += (box+1) * (i+1) * len[1]
                    
                
        print(f'part{part}: {ans}')

def calc_hash(hash):
    v = 0
    prev = 0
    for ch in hash:
        ch_v = ord(ch)
        v = ((prev + ch_v)*17) % 256
        prev = v
    return v


if __name__ == "__main__":
    nday = 15

    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


