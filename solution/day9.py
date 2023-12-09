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
                diff = [el1 - el0 for el0, el1 in zip(last[:len_list-step],last[1:len_list-step+1])]
                predict.append(diff)
                last = predict[-1]
                step += 1
            value = 0
            if len(predict[-1]):
                predict_list = []
                if part==1:
                    for diff in predict[::-1]:
                        value = diff[-1] + value
                        predict_list.insert(0,diff + [value])
                    


                    predict_values.append(predict_list[0][-1])
                if part==2:
                    for diff in predict[::-1]:
                        value = diff[0] - value
                        
                        predict_list.insert(0,[value] + diff)
                    
                    predict_values.append(predict_list[0][0])
                for diff in predict_list:
                    print(diff)
                print(predict_values[-1])

        ans = sum(predict_values)
        print(f'part{part}: {ans}')
        #1954443242.0 
        #1953784198

        




if __name__ == "__main__":
    nday = 9
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    solve(data)


