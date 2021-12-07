if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        nums = tuple(int(n) for n in f.read().strip().split('\n'))
        increments = 0
        for i in range(3, len(nums)):
            if nums[i - 3] < nums[i]:
                increments += 1
        print(increments)