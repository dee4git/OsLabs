q = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]


def finder(param, page, q, start):
    id = []
    for i in page:
        for j in range(start, len(q)):
            if i == q[j]:
                id.append(j)
                break
    id = (sorted(id))
    return id[2]


def pageid(last, page):
    for i in page:
        if i == last:
            return page.index(i)


def optimal(q):
    # print(q[0], '-', '-')
    # print(q[0], q[1], '-')
    page = [q[0], q[1], q[2]]
    # print(page)
    pagecount = 3
    length = len(q)
    count = 0
    for i in range(3, length):
        if q[i] in page:
            pass
            # print('---')
        else:
            toBeRemoved = finder(q[i], page, q, q.index(q[i]))
            last = (q[toBeRemoved])
            pageitemremove = pageid(last, page)
            page[pageitemremove] = (q[i])
            # print(page)
            count = count + 1
            if count > 2:
                count = 0
            pagecount += 1
    # print('Page fault:', pagecount)
    return pagecount


optimal(q)
