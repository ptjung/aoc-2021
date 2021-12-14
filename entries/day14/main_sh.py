from copy import deepcopy

if __name__ == "__main__":
    STEPS = 40

    with open('input.txt', 'r') as f:
        string, instructs = (lambda s, i: (s, {a: (a[0] + b, b + a[1], b) for a, b in map(lambda e: e.split(' -> '), i.split('\n'))}))(*f.read().strip().split('\n\n'))
        unique_pairs = set(instructs.keys()).union({k2 for k1 in instructs for k2 in instructs[k1][:-1]})

        pair_cnts, char_cnts = {k: string.count(k) for k in unique_pairs}, {c: string.count(c) for c in string}

        for _ in range(STEPS):
            temp_pair_cnts = deepcopy(pair_cnts)
            for k1 in pair_cnts:
                orig_pair_cnt_val = temp_pair_cnts[k1]
                pair_cnts[instructs[k1][0]] += orig_pair_cnt_val
                pair_cnts[instructs[k1][1]] += orig_pair_cnt_val
                char_cnts[instructs[k1][2]] = char_cnts.get(instructs[k1][2], 0) + orig_pair_cnt_val
                pair_cnts[k1] -= orig_pair_cnt_val

        print((lambda e: e[-1] - e[0])(sorted(char_cnts.values())))