if __name__ == "__main__":
    fold_y, fold_x = lambda p: (2 * magn - p[0], p[1]), lambda p: (p[0], 2 * magn - p[1])

    with open('input.txt', 'r') as f:
        coords, instructs_raw = [x.split('\n') for x in f.read().strip().split('\n\n')]

        points = {(coord_r, coord_c) for coord_c, coord_r in map(lambda s: map(int, s.split(',')), coords)}
        instructs = tuple((lambda l, r: (l[-1] == 'y', int(r)))(*instruct.split('=')) for instruct in instructs_raw)

        for symb_bool, magn in instructs[:1]:
            points_f = set(filter(lambda p: p[not symb_bool] >= magn, points))
            points_n = set(map((fold_x, fold_y)[symb_bool], points_f))
            points = (points - points_f).union(points_n)

        print(len(points))