import numpy as np

ans1 = ans2 = 0
M = []

with open("day13_input.txt", "r") as f:
    for map in f.read().split("\n\n"):
        M.append([ [*mapline] for mapline in map.split() ])

for m in M:
    map = np.array(m)
    H, W = len(map), len(map[0])

    for col in range(1, W):
        b = min(col, W-col)
        slice = map[0:, col-b:col+b]
        left, right = np.hsplit(slice, 2)
        right = np.fliplr(right)
        comparison = left == right
        num_diff = len([ 1 for y in comparison for x in y if not x ])
        if num_diff == 0:
            ans1 += col
        elif num_diff == 1:
            ans2 += col

    for row in range(1, H):
        d = min(row, H-row)
        slice = map[row-d:row+d, 0:]
        up, down = np.vsplit(slice, 2)
        down = np.flipud(down)
        comparison = up == down
        num_diff = len([ 1 for y in comparison for x in y if not x ])
        if num_diff == 0:
            ans1 += 100 * row
        elif num_diff == 1:
            ans2 += 100 * row

print(f"""
*** ANSWERS:
    - Part 1 = '{ans1}'.
    - Part 2 = '{ans2}'.
""")