def is_num(s):
    for c in s:
        if c not in '0123456789':
            return False
    return True

def rec_prod(elem):
    if type(elem) == int:
        return elem
    return 3 * rec_prod(elem[0]) + 2 * rec_prod(elem[1])

def arr_nestinds(arr, nestinds):
    if not nestinds:
        return []
    ref = arr
    for e in nestinds:
        if e >= len(ref):
            return None
        ref = ref[e]
    return ref

def pair_as_list(pair):
    ret, stack, acc = [], [], []
    for char in pair[1:-1] + ',':
        acc.append(char)
        if char == '[':
            stack.append(char)
        elif char == ']':
            stack.pop()
        if char == ',' and not stack:
            result = ''.join(acc[:-1])
            if is_num(result):
                ret.append(int(result))
            else:
                ret.append(pair_as_list(result))
            acc = []
    return ret

def fetch(inp_list, for_explode, depth = []):
    #global cpair
    for ind, nst_elem in enumerate(inp_list):
        next_depth = depth + [ind]
        if type(nst_elem) == int:
            if nst_elem >= 10 and not for_explode:
                # split
                return (True, next_depth)
        else:
            if len(depth) < 3:
                stop, d = fetch(nst_elem, for_explode, next_depth)
                if stop:
                    return (stop, d)
            elif for_explode:
                # explode
                return (True, next_depth)
    return (False, None)

def explode(v, left, nestinds, ret):
    right, sval = not left, (0, 1)[left]
    parent = arr_nestinds(ret, nestinds[:len(nestinds) - nestinds[::-1].index(sval) - 1 if sval in nestinds else 0])

    if parent:
        # case 1: a parent of this item has slot
        #print('l:', parent, nestinds[:len(nestinds) - nestinds[::-1].index(1) - 1 if 1 in nestinds else 0])
        if type(parent[right]) == int:
            parent[right] += v
        else:
            next_item = parent[right]
            while type(next_item[left]) != int:
                next_item = next_item[left]
            next_item[left] += v
    elif nestinds[0] == int(left):
        if type(ret[right]) == int:
            # case 2: uncle ret[0] has slot
            ret[right] += v
        else:
            # case 3: uncle ret[0, 1, 1, 1, ...] has slot
            next_item = ret[right]
            while type(next_item[left]) != int:
                next_item = next_item[left]
            next_item[left] += v

def add_pairs(pair1, pair2):
    ret = [pair_as_list(pair1), pair_as_list(pair2)]
    while True:
        found, depth = fetch(ret, True)
        if found:
            mutable = arr_nestinds(ret, depth[:-1])
            val_l, val_r = mutable[depth[-1]]
            explode(val_l, True, depth, ret)
            explode(val_r, False, depth, ret)
            mutable[depth[-1]] = 0
            continue
        found, depth = fetch(ret, False)
        if not found:
            break
        mutable, ind = arr_nestinds(ret, depth[:-1]), depth[-1]
        mutable[ind] = [mutable[ind] // 2, mutable[ind] // 2 + mutable[ind] % 2]
    return ret

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        pairs = f.read().strip().split('\n')
        max_magn = 0
        for i in range(len(pairs)):
            for j in range(len(pairs)):
                if i != j:
                    max_magn = max(max_magn, rec_prod(add_pairs(pairs[i], pairs[j])))
        print(max_magn)