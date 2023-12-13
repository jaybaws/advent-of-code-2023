import numpy as np

Y_AXIS, X_AXIS, M = 0, 1, []

with open("day13_input.txt", "r") as f:
    for map in f.read().split("\n\n"):
        M.append([ [*mapline] for mapline in map.split() ])

ans1 = ans2 = 0
for m in M:
    map = np.array(m)
    for D, axis, factor in [(len(map[0]), X_AXIS, 1), (len(map), Y_AXIS, 100)]:
        for i in range(1, D):
            d = min(i, D-i)
            slice = map[0:, i-d:i+d] if axis==X_AXIS else map[i-d:i+d, 0:]
            p, q = np.split(slice, 2, axis)
            q = np.flip(q, axis)
            comp = p == q
            num_diff = len([ 1 for y in comp for x in y if not x ])
            if num_diff == 0:
                ans1 += factor * i
            elif num_diff == 1:
                ans2 += factor * i

print(f"""
*** ANSWERS:
    - Part 1 = '{ans1}'.
    - Part 2 = '{ans2}'.
""")