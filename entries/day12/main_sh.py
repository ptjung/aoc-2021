from copy import deepcopy

CAP_LETTERS = 'QWERTYUIOPASDFGHJKLZXCVBNM'

def is_big_cave(s):
    for char in s:
        if char not in CAP_LETTERS:
            return False
    return True

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        arr = [x.split('-') for x in f.read().strip().split('\n')]
        cave = {}
        for a, b in arr:
            if b != 'start':
                cave[a] = cave.get(a, []) + [b]
            if a != 'start':
                cave[b] = cave.get(b, []) + [a]

        cnt = 0

        def explore(node, explored = {}, explored_small = False):
            if node == 'end':
                global cnt
                cnt += 1
                return
            if explored_small:
                for nxt in cave[node]:
                    if is_big_cave(nxt) or nxt not in explored:
                        new_explored = deepcopy(explored)
                        new_explored[nxt] = new_explored.get(nxt, 0) + 1
                        explore(nxt, new_explored, True)
            else:
                for nxt in cave[node]:
                    nxt_is_big = is_big_cave(nxt)
                    if nxt_is_big or explored.get(nxt, 0) < 2:
                        new_explored = deepcopy(explored)
                        new_explored[nxt] = new_explored.get(nxt, 0) + 1
                        explore(nxt, new_explored, not nxt_is_big and new_explored.get(nxt, 0) >= 2)

        explore('start')

        print(cnt)