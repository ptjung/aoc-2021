if __name__ == "__main__":
    drag = lambda e: (e - (0, 1)[e > 0], e + 1)[e < 0]

    with open('input.txt', 'r') as f:
        (r_min, r_max), (c_min, c_max) = (lambda a, b, c, d: (tuple(map(int, c[2:-1].split('..'))), tuple(map(int, d[2:].split('..')))))(*f.read().strip().split())

        ret_max_cpos = 0

        for init_vr in range(1, 200):
            for init_vc in range(1, 200):
                posr, posc, vr, vc, max_cpos = 0, 0, init_vr, init_vc, 0
                for _ in range(500):
                    posr, posc = posr + vr, posc + vc
                    vr, vc = drag(vr), vc - 1
                    max_cpos = max(posc, max_cpos)
                    if r_min <= posr <= r_max and c_min <= posc <= c_max:
                        ret_max_cpos = max(ret_max_cpos, max_cpos)
                        break

        print(ret_max_cpos)