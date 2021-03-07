import numpy as np

print('Enter option:  ')
print('1.Custom input ')
print('2.Run now with saved values ')
option = int(input())


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


def fcfs(q, head):
    q = q[::-1]
    q.append(head)
    q = q[::-1]

    for i in range(len(q) - 1):
        if i < len(q) - 2:
            print("(", end="")
            print(str(q[i + 1]) + '-' + str(q[i]), end=")")
            print("+", end="")
    print("(", end="")
    print(str(q[i + 1]) + '-' + str(q[i]), end=")")
    print()
    print('PATH', q)


lst = [head]


def fcfs2(q, head):
    for i in range(len(q) - 1):
        if i < len(q) - 2:
            print("(", end="")
            print(str(q[i + 1]) + '-' + str(q[i]), end=")")
            print("+", end="")
    print("(", end="")
    print(str(q[i + 1]) + '-' + str(q[i]), end=")")


def sstf(q, head):
    if len(q) == 0:
        fcfs2(lst[:len(lst):], head)
        print()
        print('PATH: ', lst)
        exit()

    a = np.array(q)
    # print('B: ', a,head)
    newhead = (a[np.abs(a - head).argmin()])
    index = np.where(a == newhead)
    lst.append(newhead)
    new_a = np.delete(a, index)
    # print('A: ',new_a,newhead)
    return sstf(new_a, newhead)


if option == 2:
    print('FCFS:')
    (fcfs(q, head))
    print()
    print('SSTF:')
    (sstf(q, head))
elif option == 1:
    print('FCFS:')
    (fcfs(inputTaker(), int(input('Enter Head: '))))
    print()
    print('SSTF:')
    (sstf(inputTaker(), int(input('Enter Head: '))))
else:
    print('Wrong option chosen.')
