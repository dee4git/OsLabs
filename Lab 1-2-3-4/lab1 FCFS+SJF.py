from statistics import mean
# try:
#     count= int(input("How many Processes?[int]: ",))
#
#     lst=[]
#     for i in range (count):
#         a= int(input("Enter Process "+str(i+1)+" time : "))
#         lst.append(a)
# except ValueError:
#     print("Enter a number please.")
time1 = []
time2 = []


def fcfs(lst):
    # print("_______List of Programs_________")
    # for i in range (len(lst)):
    #     print("Program: ", i, "     Time: ",lst[i])
    print("_______FCFS_______")
    t1 = 0
    for i in range(len(lst)):
        t1 = t1 + lst[i]
        time1.append(t1)
    print(time1)
    toatl = sum(time1[:len(time1) - 1])
    leng = len(time1)
    avg = toatl / leng
    print("Avg time: ", avg)
    print(lst)
    gant1(lst)


def gant1(lst):
    t1 = 0
    print("0P1 ", end=" ")
    for i in range(len(lst)):
        t1 = t1 + lst[i]
        time1.append(t1)
        if i < len(lst)-1:
            print(str(t1) + "P" + str(i + 2), end=" ")
    print(t1)
    print("")


def pairmaker(lst):
    pair=[]
    for i in range (len(lst)):
        (pair.append([i,lst[i]]))
        # print(pair)
    return pair


def scfs(lst):
    print("_______SCFS_______")
    pair= pairmaker(lst)
    gant2(pair)
    lst=sorted(lst)
    t1 = 0
    for i in range(len(lst)):
        t1 = t1 + lst[i]
        time2.append(t1)
    toatl = sum(time2[:len(time2) - 1])
    print(time2[:len(time2) - 1])
    leng = len(time2)
    avg = toatl / leng
    print("Avg time: ", avg)


def gant2(pair):
    a=[]
    b=[]
    sortedpair=(sorted(pair,key = lambda x: x[1]))
    # print(sortedpair)
    for x,y in sortedpair:
        a.append(x+1)#procces names
        b.append(y)
    print('Process: a: ',a)
    print('Time: b: ',b)

    t1 = 0
    print("0P"+str(a[0]), end=" ")
    for i in range(len(b)):
        t1 = t1 + b[i]
        time1.append(t1)
        if i < len(b) - 1:
            print(str(t1) + "P" + str(a[i+1]), end=" ")
    print(t1)
    print("")


x = [21, 3, 6, 2]
#fcfs(x)
scfs(x)
# 1,21 2,3 3,6 4,2
# 4,2  2,3 3,6 1,21