HEX_MAP = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

TID_FN_MAP = {
    '000': sum,
    '001': (lambda arr: (lambda f,a,i,s: f(f,a,i,s))(lambda f,a,i,s: f(f,a,i+1,s*a[i]) if i < len(a) else s, arr, 0, 1)), # feel free to feel disappointed in me
    '010': min,
    '011': max,
    '101': (lambda arr: (0, 1)[arr[0] > arr[1]]),
    '110': (lambda arr: (0, 1)[arr[0] < arr[1]]),
    '111': (lambda arr: (0, 1)[arr[0] == arr[1]]),
}

def bin_int(s):
    s, ret = list(s)[::-1], 0
    for i, c in enumerate(s):
        if c == '1':
            ret += 2 ** i
    return ret

def get_version_sum(p_str, start = 0):
    vsn, tid = bin_int(p_str[start:start + 3]), p_str[start + 3:start + 6]
    if tid == '100':
        orig_p_ind, p_ind, builder = start, start, []
        p_ind += 6
        while p_str[p_ind] != '0':
            # above line does not care if string is multiple of 4
            builder.append(p_str[p_ind + 1:p_ind + 5])
            p_ind += 5
        builder.append(p_str[p_ind + 1:p_ind + 5])
        p_ind += 5
        return (bin_int(''.join(builder)), p_ind)
    len_tid_mode = p_str[start + 6] == '0'
    sp_ind_left = start + (22 if len_tid_mode else 18)
    len_tid_arg = bin_int(p_str[start + 7:sp_ind_left])

    sp_vals, sp_count, p_ind = [], 0, sp_ind_left
    while (len_tid_mode and p_ind < sp_ind_left + len_tid_arg) or (not len_tid_mode and sp_count < len_tid_arg):
        sp_val, p_ind = get_version_sum(p_str, p_ind)
        sp_vals.append(sp_val)
        sp_count += 1
    return (TID_FN_MAP[tid](sp_vals), p_ind)

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        inp_hex_cleaned = ''.join(tuple(map(lambda e: HEX_MAP[e], f.read().strip())))
        print(get_version_sum(inp_hex_cleaned)[0])