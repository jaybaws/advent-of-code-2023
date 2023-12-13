import numpy as np

M, X_AXIS, Y_AXIS, ans1, ans2 = [], 1, 0, 0, 0
with open("day13_input.txt", "r") as f:
    for map in f.read().split("\n\n"):
        M.append([ [*mapline] for mapline in map.split() ])

for m in M:
    map = np.array(m)
    for D, axis, factor in [(len(map[0]), X_AXIS, 1), (len(map), Y_AXIS, 100)]:
        for i in range(1, D):
            d = min(i, D-i)
            slice = map[0:, i-d:i+d] if axis==X_AXIS else map[i-d:i+d, 0:]
            p, q = np.split(slice, 2, axis)
            q = np.flip(q, axis)
            match len([ 1 for y in (p == q) for x in y if not x ]):
                case 0: ans1 += factor * i
                case 1: ans2 += factor * i

print(f"ANSWERS -> part1=({ans1}) part2=({ans2}).")