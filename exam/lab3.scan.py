import numpy as np

# print('Enter option:  ')
# print('1.Custom input ')
# print('2.Run now with saved values ')
option = 2


def inputTaker():
    count = int(input("How many process?"))
    xx = []
    for i in range(count):
        print("For process", i + 1, ": ")
        a = int(input("Process time: "))
        xx.append(a)
    print('list of processes: ', xx)
    return xx


q = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53


def printer(q):
    for i in range(len(q) - 1):
        if i < len(q) - 2:
            print("(", end="")
            print(str(q[i + 1]) + '-' + str(q[i]), end=")")
            print("+", end="")
    print("(", end="")
    print(str(q[i + 1]) + '-' + str(q[i]), end=")")
def printer2(q):
    for i in range(len(q) - 1):
        if i < len(q) - 2:
            print("(", end="")
            print(str(q[i]) + '-' + str(q[i + 1]), end=")")
            print("+", end="")
    print("(", end="")
    print(str(q[i]) + '-' + str(q[i + 1]), end=")")


def scan(q, head, low, up):
    l = []
    u = []
    q = sorted(q)
    for i in q:
        if i < head:
            l.append(i)
        else:
            u.append(i)
    l.append(head)
    l = l[::-1]
    l.append(0)
    path = l + u
    print(path)
    printer2(l)
    print('+',end='')
    printer(u)



if option == 2:
    print('Scan:')
    (scan(q, head=53, low=0, up=199))
    print()
    # print('SSTF:')
# elif option == 1:
#     print('FCFS:')
#     (fcfs(inputTaker(), int(input('Enter Head: '))))
#     print()
#     print('SSTF:')
#     (sstf(inputTaker(), int(input('Enter Head: '))))
else:
    print('Wrong option chosen.')
