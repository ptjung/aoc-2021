def prod(arr):
    s = 1
    for e in arr:
        s *= e
    return s

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        init = tuple(tuple(map(int, x)) for x in f.read().strip().split('\n'))
        mr, mc = len(init), len(init[0])

        s = []
        for r in range(mr):
            for c in range(mc):
                if (r == 0 or init[r][c] < init[r - 1][c]) and \
                   (c == 0 or init[r][c] < init[r][c - 1]) and \
                   (r == mr - 1 or init[r][c] < init[r + 1][c]) and \
                   (c == mc - 1 or init[r][c] < init[r][c + 1]):
                    q, exp = [(r, c)], set()
                    while q:
                        e = q.pop()
                        if e in exp:
                            continue
                        exp.add(e)
                        cr, cc = e
                        if cr > 0 and init[cr - 1][cc] < 9:
                            q.append((cr - 1, cc))
                        if cr < mr - 1 and init[cr + 1][cc] < 9:
                            q.append((cr + 1, cc))
                        if cc > 0 and init[cr][cc - 1] < 9:
                            q.append((cr, cc - 1))
                        if cc < mc - 1 and init[cr][cc + 1] < 9:
                            q.append((cr, cc + 1))
                    s.append(len(exp))

        print(prod(sorted(s)[-3:]))