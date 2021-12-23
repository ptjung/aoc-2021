def get_ind(img, r, c):
    # this function is hard-coded for efficiency
    ret_sum = 0
    if (r + 1, c + 1) in img:
        ret_sum += 1
    if (r + 1, c) in img:
        ret_sum += 2
    if (r + 1, c - 1) in img:
        ret_sum += 4
    if (r, c + 1) in img:
        ret_sum += 8
    if (r, c) in img:
        ret_sum += 16
    if (r, c - 1) in img:
        ret_sum += 32
    if (r - 1, c + 1) in img:
        ret_sum += 64
    if (r - 1, c) in img:
        ret_sum += 128
    if (r - 1, c - 1) in img:
        ret_sum += 256
    return ret_sum

if __name__ == "__main__":
    ITERATIONS = 2
    _TRIM_SAFE_LEN = 5

    with open('input.txt', 'r') as f:
        algo, img_lst = (lambda a, b: (a, b.strip().split('\n')))(*f.read().strip().split('\n\n'))
        max_arr_rng = range(-(2 * ITERATIONS + _TRIM_SAFE_LEN), 2 * ITERATIONS + len(img_lst) + _TRIM_SAFE_LEN + 1)
        rng_bound_min, rng_bound_max = max_arr_rng[0] + _TRIM_SAFE_LEN, max_arr_rng[-1] - _TRIM_SAFE_LEN
        in_rng = lambda d: rng_bound_min <= d <= rng_bound_max

        img_set = {(r, c) for r in range(len(img_lst)) for c in range(len(img_lst[r])) if img_lst[r][c] == '#'}

        for i in range(ITERATIONS):
            check_lst = {(r, c) for r in  max_arr_rng for c in max_arr_rng}
            new_img_set = set()
            for r, c in check_lst:
                if algo[get_ind(img_set, r, c)] == '#' :
                    new_img_set.add((r, c))
            if i % 2:
                img_set = set(filter(lambda rc_pair: in_rng(rc_pair[0]) and in_rng(rc_pair[1]), new_img_set))
            else:
                img_set = new_img_set

        print(len(img_set))