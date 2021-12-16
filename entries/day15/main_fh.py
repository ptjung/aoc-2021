def run_sum(arr):
    ret = []
    s = 0
    for e in arr:
        s += e
        ret.append(s)
    return ret


if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        inp = tuple(tuple(map(int, x)) for x in f.read().strip().split('\n'))

        dp = [run_sum(list(inp[0]))] + [[0 for c in range(len(inp[r]))] for r in range(len(inp) - 1)]

        for i, r in enumerate(run_sum(tuple(inp[r][0] for r in range(len(inp))))):
            dp[i][0] = r

        for r in range(1, len(dp)):
            for c in range(1, len(dp[r])):
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + inp[r][c]

        print(dp[-1][-1] - dp[0][0])