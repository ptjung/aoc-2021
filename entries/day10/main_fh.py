if __name__ == "__main__":
    closables = {
        ')': ('(', 3),
        ']': ('[', 57),
        '}': ('{', 1197),
        '>': ('<', 25137),
    }

    with open('input.txt', 'r') as f:
        init = tuple(f.read().strip().split('\n'))

        s = 0
        for l in init:
            stack = []
            for c in l:
                if c in '([{<':
                    stack.append(c)
                elif stack and stack[-1] == closables[c][0]:
                    stack.pop()
                else:
                    s += closables[c][1]
                    break

        print(s)