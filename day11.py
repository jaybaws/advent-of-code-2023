with open("day11_input.txt", "r") as f: IMAGE = [ [*line] for line in f.read().splitlines() ]
galaxies = [ (r, c) for r in range(len(IMAGE)) for c in range(len(IMAGE[0])) if IMAGE[r][c] == "#" ]
empty_rows = [ row_index for row_index, row in enumerate(IMAGE) if "#" not in row ]
empty_cols = [ col_index for col_index in range(len(IMAGE[0])) if "#" not in [ r[col_index] for r in IMAGE ] ]

ans1 = ans2 = 0
for ((ar, ac), (br, bc)) in [ ((a_r, a_c), (b_r, b_c)) for ia, (a_r, a_c) in enumerate(galaxies) for ib, (b_r, b_c) in enumerate(galaxies) if ib > ia]:
    manhattan_distance = abs(br - ar) + abs(bc - ac)
    expanded_space = len([c for c in empty_cols if min(ac, bc) < c < max(ac, bc)]) + len([r for r in empty_rows if min(ar, br) < r < max(ar, br)])
    ans1 += manhattan_distance + ((2-1) * expanded_space)
    ans2 += manhattan_distance + ((1000000-1) * expanded_space)

print(f"""
*** ANSWERS:
    - Part 1 = '{ans1}'.
    - Part 2 = '{ans2}'.
""")