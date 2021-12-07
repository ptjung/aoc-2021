if __name__ == "__main__":
    INPUT_CAP = 1000

    line_to_pnts = lambda p1, p2: (tuple(map(int, p1.split(','))), tuple(map(int, p2.split(','))))

    with open('input.txt', 'r') as f:
        inp = f.read().strip().split('\n')
        lines = [line_to_pnts(*l.split(' -> ')) for l in inp]

        grid = []
        for _ in range(INPUT_CAP):
            x = [0] * INPUT_CAP
            grid.append(x)

        for (p1_r, p1_c), (p2_r, p2_c) in lines:
            if p1_r == p2_r:
                for c in range(min(p1_c, p2_c), max(p1_c, p2_c) + 1):
                    grid[c][p1_r] += 1
            elif p1_c == p2_c:
                for r in range(min(p1_r, p2_r), max(p1_r, p2_r) + 1):
                    grid[p1_c][r] += 1
            else:
                vr = 1 if p2_r > p1_r else -1
                vc = 1 if p2_c > p1_c else -1
                for d in range(abs(p2_r - p1_r) + 1):
                    grid[p1_c + vc * d][p1_r + vr * d] += 1

        val_dict = {}
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                elem = grid[r][c]
                val_dict[elem] = val_dict.get(elem, 0) + 1

        results = sorted(filter(lambda x: x[0] > 1, val_dict.items()), reverse = True)
        print(sum(map(lambda k: k[1], results)))