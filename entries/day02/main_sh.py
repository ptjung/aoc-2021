if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        nums = ((lambda a, b: (a, int(b)))(*n.split()) for n in f.read().strip().split('\n'))

        dispt, depth, aim = 0, 0, 0
        for cmd, mag in nums:
            if cmd == 'forward':
                dispt += mag
                depth += aim * mag
            elif cmd == 'down':
                aim += mag
            elif cmd == 'up':
                aim -= mag

        print(dispt * depth)