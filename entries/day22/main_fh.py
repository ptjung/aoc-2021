from itertools import product

if __name__ == "__main__":
    get_rng_args = lambda a, b: (max(a, -50), min(b, 50) + 1)

    with open('input.txt', 'r') as f:
        reboot_steps = tuple(map(lambda l: (lambda b, s: (b, tuple(map(lambda v: range(*get_rng_args(*map(int, v[2:].split('..')))), s.split(',')))))(*l.split()), f.read().strip().split('\n')))

        on_cubes = set()
        for cmd, xyz_ranges in reboot_steps:
            selected_pnts = set(product(*xyz_ranges))
            if cmd == 'on':
                on_cubes.update(selected_pnts)
            else:
                on_cubes.difference_update(selected_pnts)

        print(len(on_cubes))