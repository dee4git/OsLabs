def inputTaker():
    count = int(input("How many process?"))
    xx = []
    for i in range(count):
        print("For process", i + 1, ": ")
        a = int(input("Process time: "))
        b = int(input("Priority: "))
        xx.append([int(i) + 1, b, a])
    return xx


x = [[1, 2, 21], [2, 1, 3], [3, 4, 6], [4, 3, 2]]


def avg_time(lst):
    t1 = 0
    time2 = []
    for i in range(len(lst)):
        t1 = t1 + lst[i]
        time2.append(t1)
    toatl = sum(time2[:len(time2) - 1])
    leng = len(time2)
    avg = toatl / leng
    print("Avg time: ", avg)


def priority_sch(pair):
    a = []
    b = []
    c = []
    sortedpair = (sorted(pair, key=lambda x: x[1]))
    for x, y, z in sortedpair:
        a.append(x)
        b.append(y)
        c.append(z)
    avg_time(c)
    t1 = 0
    time1 = []
    print("0P" + str(a[0]), end=" ")
    for i in range(len(c)):
        t1 = t1 + c[i]
        time1.append(t1)
        if i < len(c) - 1:
            print(str(t1) + "P" + str(a[i + 1]), end=" ")
    print(t1)
    print("")


x = [[1, 2, 21], [2, 1, 3], [3, 4, 6], [4, 3, 2]]
# priority_sch(x)
priority_sch(inputTaker())