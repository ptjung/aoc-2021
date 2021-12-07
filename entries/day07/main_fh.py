if __name__ == "__main__":
    INPUT_CAP = 2000

    with open('input.txt', 'r') as f:
        init = tuple(map(int, f.read().strip().split(',')))

        min_s, postn = float('inf'), 0
        for i in range(1, INPUT_CAP):
            s = sum(map(lambda n: abs(n - i), init))
            if min_s > s:
                postn = i
                min_s = s

        print(min_s)
