ALPHA = {chr(x) for x in range(65, 91)}

if __name__ == "__main__":
    STEPS = 10

    with open('input.txt', 'r') as f:
        string, instructs = (lambda s, i: (s, {a: b + a[1] for a, b in map(lambda e: e.split(' -> '), i.split('\n'))}))(*f.read().strip().split('\n\n'))

        for _ in range(STEPS):
            new_string = [string[0]]
            for i in range(len(string) - 1):
                str_pair = string[i:i + 2]
                new_string.append(instructs.get(str_pair, str_pair))
            string = ''.join(new_string)

        print((lambda e: e[-1] - e[0])(sorted(filter(lambda n: n, (string.count(c) for c in ALPHA)))))