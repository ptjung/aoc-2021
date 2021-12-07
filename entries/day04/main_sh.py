def check_bingo(grid, drawn):
    for r in grid:
        for cell in r:
            if cell not in drawn:
                break
        else:
            return True

    for c in range(5):
        for cell in [grid[r][c] for r in range(5)]:
            if cell not in drawn:
                break
        else:
            return True

    return False

def get_gsum(grid, drawn):
    total = 0
    for r in grid:
        for c in r:
            if c not in drawn:
                total += c
    return total


if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        drawn = list(map(int, f.readline().strip().split(',')))[::-1]

        grids, cgrid = [], []
        for l in (*f.read().strip().split('\n'), ''):
            if not l:
                grids.append(cgrid)
                cgrid = []
            else:
                cgrid.append(list(map(int, l.split())))

        cdrawn = set()
        boards_won = set()
        res = []
        while drawn and len(boards_won) < len(grids):
            elem = drawn.pop()
            cdrawn.add(elem)
            for i, g in enumerate(grids):
                if i not in boards_won and check_bingo(g, cdrawn):
                    res = elem * get_gsum(g, cdrawn)
                    boards_won.add(i)

        print(res)