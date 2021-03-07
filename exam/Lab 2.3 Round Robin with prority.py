global time

global start

def inputTaker():
    count = int(input("How many process?"))
    xx = []
    for i in range(count):
        print("For process", i + 1, ": ")
        a = int(input("Process time: "))
        b = int(input("Priority: "))
        xx.append([int(i)+1, a, b])
    print('Format: [Process No: Burst Time: Priority]',xx)
    return xx

def round_robin(lst, q):
    print('0', end="")
    time = 0
    done = 0
    lst = (sorted(lst, key=lambda x: x[2]))
    while done != len(lst):
        for i in lst:
            # print("LOL: ",i)
            # print('working with: ', i, end="--->")
            if (i[1] == 0):
                pass
            elif (i[1] - q) > 0:
                i[1] = i[1] - q
                time = time + q
                print('P' + str(i[0]), time, end="")
            elif (i[1] - q) <= 0:
                time = time + i[1]
                i[1] = 0
                print('P' + str(i[0]), time, end="")
                done += 1


x = [[2, 3, 2], [3, 6, 3], [4, 2, 4], [1, 21, 1]]
round_robin(x,5)
