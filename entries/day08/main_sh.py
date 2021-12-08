def str_to_key(s):
    return ''.join(sorted(s))

def map_to_config(inp):
    num_to_segments = [(0, 1, 2, 4, 5, 6), (2, 5), (0, 2, 3, 4, 6), (0, 2, 3, 5, 6), (1, 2, 3, 5), (0, 1, 3, 5, 6), (0, 1, 3, 4, 5, 6), (0, 2, 5), (0, 1, 2, 3, 4, 5, 6), (0, 1, 2, 3, 5, 6)]

    arr = tuple(map(set, list(sorted(inp, key = len))))
    config = [None] * 7
    config[0] = tuple(arr[1] - arr[0])[0]
    config[6] = tuple(((arr[6] - arr[1].union(arr[2])).intersection(arr[7] - arr[1].union(arr[2])).intersection((arr[8] - arr[1].union(arr[2])))))[0]
    config[4] = tuple(arr[9] - arr[1].union(arr[2]).union({config[6]}))[0]
    config[5] = tuple(filter(lambda x: x[1] == 9, tuple([(c, len(tuple(filter(lambda s: c in s, arr)))) for c in 'abcdefg'])))[0][0]
    config[2] = tuple(arr[0] - {config[5]})[0]
    config[3] = tuple(arr[3].intersection(arr[4]).intersection(arr[5]) - set(config))[0]
    config[1] = tuple(arr[8] - set(config))[0]

    config_kvp = {}
    for string in inp:
        for i, indices in enumerate(num_to_segments):
            if set(string) == (set(map(lambda x: config[x], indices))):
                config_kvp[str_to_key(string)] = str(i)
                break

    return config_kvp


if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        init = tuple(map(lambda s: (lambda a, b: (a.split(), b.split()))(*s.split(' | ')), f.read().strip().split('\n')))

        times = 0
        for inp, out in init:
            config = map_to_config(inp)
            times += int(''.join(map(lambda k: config[str_to_key(k)], out)))

        print(times)