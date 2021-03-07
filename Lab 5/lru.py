q = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]


def finder(param, page, q, start):
    id = []
    for i in page:
        for j in range(start, -1, -1):
            if i == q[j]:
                id.append(j)
                break
    id = (sorted(id))

    return id[0]


def pageid(last, page):
    for i in page:
        if i == last:
            return page.index(i)


def fifo(q):

    print(q[0], '-', '-')
    print(q[0], q[1], '-')
    page = [q[0], q[1], q[2]]
    print(page)

    length = len(q)
    count = 3
    pagecount = 3
    for i in range(3, length):
        if q[i] in page:
            print('---')
            count = count + 1
        else:
            toBeRemoved = finder(q[i], page, q, count)
            last = (q[toBeRemoved])
            pageRemove = pageid(last, page)
            page[pageRemove] = (q[i])
            print(page)
            count = count + 1
            pagecount += 1

    print('Page fault:', pagecount)
    return pagecount


fifo(q)
