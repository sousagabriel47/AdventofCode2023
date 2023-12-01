"""Solution of day1 - AoC2023."""
import sys

def read_data(data):
    data = data.splitlines()
    digs = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for part in [1,2]:
        sum_data = []
        for line in data:
            num = []
            int_num = 0
            for idx, ch in enumerate(line):
                if part == 1: 
                    if ord(ch) <= 57:
                        num.append(ch)
                else:
                    if ord(ch) <= 57:
                        num.append(ch)
                    else:
                        for number in digs.keys():
                            if number in line:
                                len_num = len(number)
                                #print(number, line[idx:idx+len_num])
                                if line[idx:idx+len_num] == number:
                                    #print(line[idx:idx+len_num], digs[number])
                                    num.append(digs[number])
            
            
            #print(line, num)
            if len(num):
                if len(num) > 1:
                    int_num = int(num[0]+num[-1])
                else:
                    int_num = int(num[0]+num[0])
            if int_num == 0:
                print(line, num)
            
            sum_data.append(int_num)
        #print(sum_data)
        print(f'part{part}: {sum(sum_data)}')




if __name__ == "__main__":
    nday = 1
    with open(f'./solution/data/{sys.argv[1]}/{nday}','r') as f:
        data = f.read()
    read_data(data)


