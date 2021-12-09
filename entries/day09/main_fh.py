if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        init = tuple(tuple(map(int, x)) for x in f.read().strip().split('\n'))
        mr, mc = len(init), len(init[0])

        s = 1
        for r in range(mr):
            for c in range(mc):
                if (r == 0 or init[r][c] < init[r - 1][c]) and \
                   (c == 0 or init[r][c] < init[r][c - 1]) and \
                   (r == mr - 1 or init[r][c] < init[r + 1][c]) and \
                   (c == mc - 1 or init[r][c] < init[r][c + 1]):
                    s += init[r][c] + 1

        print(s)