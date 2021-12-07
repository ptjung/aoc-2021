if __name__ == "__main__":
    DAY_COUNT = 256

    with open('input.txt', 'r') as f:
        init = tuple(map(int, f.read().strip().split(',')))

        init_val_cnt = {}
        for e in init:
            init_val_cnt[e] = init_val_cnt.get(e, 0) + 1

        states = [len(init), *((0,) * (DAY_COUNT - 1))]
        for i in range(1, len(states)):
            states[i] = states[i - 1] + init_val_cnt.get(i, 0)
            if i >= 8:
                states[i] += states[i - 7] - states[i - 8]
            if i >= 10:
                states[i] += states[i - 9] - states[i - 10]

        for i, e in enumerate(states):
            print("After {} days: {}".format(i + 1, e))