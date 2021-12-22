def ori(x, y, z):
    """
    some notes:

    - 6 faces (i.e. xyz-permutations), into 4 rotations for each face (determines negative signs) = 24 orientations
    - given (x, y, z), even # of swaps between elements will yield an even # of negative elements in the coordinate
    """
    return (
        # 1 swap
        (x, z, -y),
        (x, -z, y),
        (-x, z, y),
        (-x, -z, -y),

        # 1 swap
        (y, x, -z),
        (y, -x, z),
        (-y, x, z),
        (-y, -x, -z),

        # 1 swap
        (z, y, -x),
        (z, -y, x),
        (-z, y, x),
        (-z, -y, -x),

        # 0 swaps
        (x, y, z),
        (x, -y, -z),
        (-x, -y, z),
        (-x, y, -z),

        # 2 swaps
        (y, z, x),
        (y, -z, -x),
        (-y, -z, x),
        (-y, z, -x),

        # 2 swaps
        (z, x, y),
        (z, -x, -y),
        (-z, -x, y),
        (-z, x, -y),
    )

def find_scan_ori(scan_culm, scan_alt, loc_ref):
    for scan_ori in zip(*map(lambda c: ori(*c), scan_alt)):
        diff_cnter = {}
        for ori_x, ori_y, ori_z in scan_ori:
            for culm_x, culm_y, culm_z in scan_culm:
                diff_v = (ori_x - culm_x, ori_y - culm_y, ori_z - culm_z)
                diff_cnter[diff_v] = diff_cnter.get(diff_v, 0) + 1
                if diff_cnter[diff_v] >= BEACON_CNT_REQ:
                    origin_loc = (loc_ref[0] + diff_v[0], loc_ref[1] + diff_v[1], loc_ref[2] + diff_v[2])
                    beacon_locs = set(map(lambda v: (v[0] - diff_v[0], v[1] - diff_v[1], v[2] - diff_v[2]), scan_ori))
                    return origin_loc, beacon_locs
    return None, None

if __name__ == "__main__":
    BEACON_CNT_REQ = 12

    with open('input.txt', 'r') as f:
        scans = list(map(lambda b: set(map(lambda c: tuple(map(int, c.split(','))), b.split('\n')[1:])), f.read().strip().split('\n\n')[::-1]))

        scans_found = [((0, 0, 0), (0, 0, 0), scans.pop())]
        beacon_locs = scans_found[0][2]

        while scans:
            orig_scans_cnt = len(scans_found)
            for ind, scan_new in enumerate(scans):
                for culm_loc_ref, _, scan_culm in scans_found:
                    diff_v, beacon_locs_found = find_scan_ori(scan_culm, scan_new, culm_loc_ref)
                    if diff_v:
                        beacon_locs = beacon_locs.union(beacon_locs_found)
                        scans_found.append((diff_v, culm_loc_ref, beacon_locs_found))
                        del scans[ind]
                        break
                if len(scans_found) > orig_scans_cnt:
                    break

        max_manh_dist = 0
        scanner_locs = tuple((v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]) for i, (v1, v2, _) in enumerate(scans_found))

        for i, scan_i in enumerate(scanner_locs):
            for j in range(i + 1, len(scanner_locs)):
                scan_j = scanner_locs[j]
                max_manh_dist = max(max_manh_dist, abs(scan_i[0] - scan_j[0]) + abs(scan_i[1] - scan_j[1]) + abs(scan_i[2] - scan_j[2]))

        print(max_manh_dist)