q = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]


def fifo(q):
    print(q[0], '-', '-')
    print(q[0], q[1], '-')
    page = [q[0], q[1], q[2]]
    print(page)
    pagecount = 3
    length = len(q)
    count = 0
    for i in range(3, length):
        if q[i] in page:
            print('---')
        else:
            page[count] = (q[i])
            print(page)
            count = count + 1
            if count > 2:
                count = 0
            pagecount += 1
    print('Page fault:', pagecount)


fifo(q)
