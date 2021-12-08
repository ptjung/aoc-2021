if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        init = tuple(map(lambda s: (lambda a, b: (a.split(), b.split()))(*s.split(' | ')), f.read().strip().split('\n')))
        findable = {2, 4, 3, 7}

        times = 0
        for inp, out in init:
            times += len(tuple(filter(lambda x: len(x) in findable, out)))

        print(times)