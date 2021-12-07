def bit_sum(bits, i):
    s = 0
    for b in bits:
        if b[i] == '0':
            s -= 1
        elif b[i] == '1':
            s += 1
    return s

def compute_rating(nums, alt):
    i = 0
    while len(nums) > 1:
        nums = tuple(b for b in nums if b[i] == '01'[(bit_sum(nums, i) >= 0) ^ alt])
        i += 1
    return sum(2 ** i for i, e in enumerate(nums[0][::-1]) if e == '1')

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        nums = tuple(f.read().strip().split('\n'))
        o2_gen_rating, co2_scr_rating = compute_rating(nums, False), compute_rating(nums, True)
        print(o2_gen_rating * co2_scr_rating)