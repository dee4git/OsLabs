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

global time

global start

alltimes = []
def wait2(single):
    print(single)
    t=0
    #single=single[::]
    if single[0][0]==1:
        for i in range(len(single)-1):
            print('First Process waits: ',str(single[i+1][2])+'-'+str(single[i][1])+'='+str(single[i+1][2]-single[i][1]))
            alltimes.append(single[i+1][2]-single[i][1])
        print('Total: ',sum(alltimes))
    else:
        temp = sum(alltimes)
        fist=single[0]
        firsttime=fist[2]
        print('First arrival wait time  :',firsttime)
        alltimes.append(firsttime)
        for i in range(len(single)-1):
            print('After that Process waits: ',str(single[i+1][2])+'-'+str(single[i][1])+'='+str(single[i+1][2]-single[i][1]))
            alltimes.append(single[i+1][2]-single[i][1])
        print('Total: ', sum(alltimes)-temp)

    return sum(alltimes)

def waitTime(wait,p):
    print('____Wait time calculation details_____')
    print('____List of Programs: Format[Process:end:start]_____')
    print(wait)
    print('____Starting calculation_____')

    single=[]
    wait = (sorted(wait, key=lambda x: x[0]))
    l=len(wait)
    count=1
    while count!=p+1:
        for i in wait:
            if i[0]==count:
                single.append(i)
        count=count+1

        total=wait2(single)
        single=[]
    print('_____End of calculation___________')
    print('Total wait:',total,'Process Count:',p)
    print('Avg Time: ',total/p)




def round_robin(lst, q):
    lst = (sorted(lst, key=lambda x: x[2]))

    print('0', end="")
    time = 0
    done = 0
    wait = []
    while done != len(lst):
        for i in lst:
            # print("LOL: ",i)
            # print('working with: ', i, end="--->")
            if (i[1] == 0):
                pass
            elif (i[1] - q) > 0:
                i[1] = i[1] - q
                temp = time
                time = time + q
                wait.append([i[0], time, temp])
                print('P' + str(i[0]), time, end="")
            elif (i[1] - q) <= 0:
                temp = time
                time = time + i[1]
                wait.append([i[0], time, temp, ])
                i[1] = 0
                print('P' + str(i[0]), time, end="")
                done += 1
    print()
    waitTime(wait,len(lst))

#pqrs
x = [[2, 3, 2], [3, 6, 3], [4, 2, 4], [1, 21, 1]]
# round_robin(inputTaker(), int(input(" Enter Quantum: ")))
round_robin(x,100)