if __name__ == "__main__":
    closables = {
        ')': ('(', 3),
        ']': ('[', 57),
        '}': ('{', 1197),
        '>': ('<', 25137),
    }

    closables_alt = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    with open('input.txt', 'r') as f:
        init = tuple(f.read().strip().split('\n'))

        s = []
        for l in init:
            stack, usable = [], True
            for c in l:
                if c in '([{<':
                    stack.append(c)
                elif stack and stack[-1] == closables[c][0]:
                    stack.pop()
                else:
                    usable = False
                    break
            if usable:
                score = 0
                for c in stack[::-1]:
                    score = 5 * score + closables_alt[c]
                s.append(score)

        print(sorted(s)[len(s) // 2])