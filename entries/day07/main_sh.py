if __name__ == "__main__":
    INPUT_CAP = 2000

    with open('input.txt', 'r') as f:
        init = tuple(map(int, f.read().strip().split(',')))

        diffs = [0] * INPUT_CAP
        for i in range(1, len(diffs)):
            diffs[i] = diffs[i - 1] + i

        min_s, postn = float('inf'), 0
        for i in range(1, len(diffs)):
            s = sum(map(lambda n: diffs[abs(n - i)], init))
            if min_s > s:
                postn = i
                min_s = s

        print(min_s)
