"""Solution of day1 - AoC2023."""
import sys



def solve(data):
    data = data.split('\n\n')
    total = 0

    seeds = [int(s) for s in data[0].split(':')[1].split()]
    transform = {}
    for t in data[1:]:
        params = t.splitlines()
        name = params[0].split()[0]
        transform[name] = {}
        for idT, ranges in enumerate(params[1:]):
            transform[name][idT] = {}
            st_dest, st_source, length = [int(n) for n in ranges.split()]
            transform[name][idT]['interval'] = [st_source,st_source + length - 1]
            transform[name][idT]['delta'] = st_dest - st_source
    for part in [1, 2]:
        if part == 2:
            total = 0
            for idSeed, seed in enumerate(seeds[::2]):
                step = seeds[idSeed*2+1]
                new_seeds = []
                print(seed, step)
                total += step
                for i in range(step):
                    new_seeds.append(seed + i)
                
                print(min(calc_location(transform, new_seeds)))
        if part == 1:
            location = calc_location(transform, seeds)
        print(f'part{part}: {min(location)}')

def calc_location(transform, seeds):

    out = [[0]*8 for _ in range(len(seeds))]
    for i,seed in enumerate(seeds):
        out[i][0] = seed
    idTransform = 0
    for _, params in transform.items():
        list_nums = [line[idTransform] for line in out]
        for idSeed, num in enumerate(list_nums):
            check = False
            for intervals in params.values():
                if (intervals['interval'][0] <= num and
                    num <= intervals['interval'][1]):
                    check = True
                    out[idSeed][idTransform+1] = num + intervals['delta']
            if not check:
                out[idSeed][idTransform+1] = num
        idTransform += 1
    return [line[-1] for line in out]

if __name__ == "__main__":
    nday = 5
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


