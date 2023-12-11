with open("day10_input.txt", "r") as f: M = [ [*l] for l in f.read().splitlines() ]
D = {
    "|": ((-1,0),(+1,0)),
    "-": ((0,-1),(0,+1)),
    "L": ((-1,0),(0,+1)),
    "J": ((-1,0),(0,-1)),
    "7": ((+1,0),(0,-1)),
    "F": ((0,+1),(+1,0)),
    "S": ((0,+1),(+1,0))
}

start = None
for r, row in enumerate(M):
    for c, tile in enumerate(row):
        if tile == "S":
            start = (r,c)

r, c = start
loop = [ ]
while True:
    loop.append((r,c))
    ((ro1,co1),(ro2,co2)) = D[M[r][c]]
    if not (r+ro1,c+co1) in loop:
        r += ro1
        c += co1
    elif not (r+ro2,c+co2) in loop:
        r += ro2
        c += co2
    else:
        break

ans1 = len(loop) // 2 

ans2 = 0
for r in range(len(M)):
    for c in range(len(M[r])):
        if not (r,c) in loop:
            num_intersects = len([ (y,x) for (y,x) in loop if y == r and x > c and M[y][x] in ["|", "L", "J"] ])
            if num_intersects % 2 != 0:
                ans2 += 1

print(f"""
*** ANSWERS:
    - Part 1 = '{ans1}'.
    - Part 2 = '{ans2}'.
""")