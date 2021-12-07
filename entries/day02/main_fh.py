if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        nums = ((lambda a, b: (a, int(b)))(*n.split()) for n in f.read().strip().split('\n'))

        dispt, depth = 0, 0
        for cmd, mag in nums:
            if cmd == 'forward':
                dispt += mag
            elif cmd == 'down':
                depth += mag
            elif cmd == 'up':
                depth -= mag

        print(dispt * depth)