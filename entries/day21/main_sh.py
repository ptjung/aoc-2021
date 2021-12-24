from functools import lru_cache
from itertools import product

@lru_cache(maxsize = None)
def i(cond, x, y):
    return x if cond else y

@lru_cache(maxsize = None)
def get_wins(pos_a, pos_b, score_a = 0, score_b = 0, player = False):

    if score_a >= SCORE_CAP:
        return 1, 0
    if score_b >= SCORE_CAP:
        return 0, 1

    wins_a, wins_b = 0, 0
    player_alt = not player
    for steps in ROLL_SUMS:
        new_pos = (i(player, pos_b, pos_a) + steps - 1) % 10 + 1
        nxt_a, nxt_b = get_wins(i(player, pos_a, new_pos), i(player, new_pos, pos_b), score_a + new_pos * player_alt, score_b + new_pos * player, player_alt)
        wins_a += nxt_a
        wins_b += nxt_b
    return wins_a, wins_b

if __name__ == "__main__":
    SCORE_CAP = 21
    ROLL_SUMS = tuple(map(sum, product(range(1, 4), repeat = 3)))

    with open('input.txt', 'r') as f:
        print(max(get_wins(*map(lambda e: int(e.split()[-1]), f.read().strip().split('\n')))))