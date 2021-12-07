def bit_sum(bits):
    s = 0
    for b in bits:
        if b == '0':
            s -= 1
        else:
            s += 1
    return s

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        nums = tuple(f.read().strip().split('\n'))

        quants = tuple(tuple(nums[r][c] for r in range(len(nums))) for c in range(len(nums[0]) - 1, -1, -1))

        gamma_r, eps_r = 0, 0
        for i, quant in enumerate(quants):
            res = bit_sum(quant)
            if res > 0:
                gamma_r += 2 ** i
            elif res < 0:
                eps_r += 2 ** i

        print(gamma_r * eps_r)