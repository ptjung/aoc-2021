if __name__ == "__main__":
    SCORE_CAP = 1000

    roll = lambda x: (x % 100 + (x + 1) % 100 + (x + 2) % 100 + 3, (x + 2) % 100 + 1)

    with open('input.txt', 'r') as f:
        pos_a, pos_b = map(lambda e: int(e.split()[-1]), f.read().strip().split('\n'))

        nxt_roll, rolls, score_a, score_b = 0, 0, 0, 0
        while True:
            steps, nxt_roll = roll(nxt_roll)
            pos_a = (pos_a + steps - 1) % 10 + 1
            score_a += pos_a
            rolls += 3
            if score_a >= SCORE_CAP:
                print(score_b * rolls)
                break

            steps, nxt_roll = roll(nxt_roll)
            pos_b = (pos_b + steps - 1) % 10 + 1
            score_b += pos_b
            rolls += 3
            if score_b >= SCORE_CAP:
                print(score_a * rolls)
                break