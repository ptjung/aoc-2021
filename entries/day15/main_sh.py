from heapq import heapify, heappush, heappop

def run_sum(arr):
    ret = []
    s = 0
    for e in arr:
        s += e
        ret.append(s)
    return ret

def get_new_inp(inp):
    INC_MAP = ((-1, 0, 1, 2, 3), (0, 1, 2, 3, 4), (1, 2, 3, 4, 5), (2, 3, 4, 5, 6), (3, 4, 5, 6, 7))

    inp_max_r, inp_max_c = len(inp), len(inp[0])
    ret = [[0 for _j in range(5 * inp_max_c)] for _i in range(5 * inp_max_r)]
    for r in range(len(ret)):
        for c in range(len(ret[r])):
            inc_val = INC_MAP[(r - r % inp_max_r) // inp_max_r][(c - c % inp_max_c) // inp_max_c]
            ret[r][c] = (inp[r % inp_max_r][c % inp_max_c] + inc_val) % 9 + 1
    return ret

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        inp = get_new_inp(tuple(tuple(map(int, x)) for x in f.read().strip().split('\n')))
        inp_max_r, inp_max_c = len(inp), len(inp[0])
        inp_max_ir, inp_max_ic = inp_max_r - 1, inp_max_c - 1

        explored = set()
        graph = [[float('inf') for c in range(inp_max_c)] for r in range(inp_max_r)]
        heap = [(0, (0, 0))]
        heapify(heap)

        def explore_node(node_val, r, c):
            if (r, c) not in explored and 0 <= r < inp_max_r and 0 <= c < inp_max_c:
                new_val = min(graph[r][c], node_val + inp[r][c])
                heappush(heap, (new_val, (r, c)))
                graph[r][c] = new_val
                explored.add((r, c))

        while heap:
            nval, (r, c) = heappop(heap)
            if r == inp_max_ir and c == inp_max_ic:
                print(nval)
                break
            explore_node(nval, r - 1, c)
            explore_node(nval, r + 1, c)
            explore_node(nval, r, c - 1)
            explore_node(nval, r, c + 1)
