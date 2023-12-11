with open("day11_input.txt", "r") as f: C = [ [*l] for l in f.read().splitlines() ]
galaxies = [ (r,c) for r in range(len(C)) for c in range(len(C[0])) if C[r][c] == "#" ]
empty_rows = [ idx for idx, row in enumerate(C) if "#" not in row ]
empty_cols = [ ci for ci in range(len(C[0])) if "#" not in [ r[ci] for r in C ] ]

ans1 = ans2 = 0
for ia, (ga_r, ga_c) in enumerate(galaxies):
    for ib, (gb_r, gb_c) in enumerate(galaxies):
        if ib > ia:
            d = abs(gb_r - ga_r) + abs(gb_c - ga_c)
            e = len([c for c in empty_cols if min(ga_c, gb_c) < c < max(ga_c, gb_c)]) + len([r for r in empty_rows if min(ga_r, gb_r) < r < max(ga_r, gb_r)])
            ans1 += d + e
            ans2 += d + ((1000000-1) * e)

print(f"""
*** ANSWERS:
    - Part 1 = '{ans1}'.
    - Part 2 = '{ans2}'.
""")