"""Solution of day1 - AoC2023."""
import sys

def solve(data):
    data = data.splitlines()
    history = []
    for line in data:
        history.append([int(el) for el in line.split()])
    ans = 0
    for part in [1,2]:
        predict_values = []
        for id, line in enumerate(history):
            predict = [line]
            len_list = len(line)
            step = 1
            last = predict[-1]
            
            while not all([el == 0 for el in last]):
                diff = [abs(el0 - el1) for el0, el1 in zip(last[:len_list-step],last[1:len_list-step+1])]
                predict.append(diff)
                last = predict[-1]
                step += 1
            value = 0

            if len(predict[-1]):
                for diff in predict:
                    print(diff)
                for diff in predict[-2:0:-1]:
                    value = diff[-1] + value
                
                signal = (predict[0][-1]-predict[0][-2])/abs(predict[0][-1]-predict[0][-2])
                predict_values.append(predict[0][-1] + signal*value)
                print(predict_values[-1])
        ans = sum(predict_values)
        print(f'part{part}: {ans}')

        




if __name__ == "__main__":
    nday = 9
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


