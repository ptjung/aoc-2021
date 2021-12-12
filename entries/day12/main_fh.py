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
            cave[a] = cave.get(a, []) + [b]
            cave[b] = cave.get(b, []) + [a]

        cnt = 0

        def explore(node, explored = set()):
            if node == 'end':
                global cnt
                cnt += 1
                return
            for nxt in cave[node]:
                if nxt not in explored or is_big_cave(nxt):
                    explore(nxt, explored.union({node}))

        explore('start')

        print(cnt)