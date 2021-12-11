if __name__ == "__main__":
    STEPS = 100
    FLASH_RC = tuple((r, c) for r in range(-1, 2) for c in range(-1, 2) if (r, c) != (0, 0))

    with open('input.txt', 'r') as f:
        arr = [list(map(int, x)) for x in f.read().strip().split('\n')]
        max_r, max_c = len(arr), len(arr[0])

        flashes = 0
        for _ in range(STEPS):
            stack = [(r, c) for r in range(max_r) for c in range(max_c)]

            while stack:
                r, c = stack.pop()
                arr[r][c] += 1
                if arr[r][c] == 10:
                    for vr, vc in FLASH_RC:
                        if 0 <= r + vr < max_r and 0 <= c + vc < max_c:
                            stack.append((r + vr, c + vc))

            for  r in range(max_r):
                for c in range(max_c):
                    if arr[r][c] >= 10:
                        flashes += 1
                        arr[r][c] = 0

        print(flashes)