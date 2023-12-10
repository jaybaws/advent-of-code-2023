with open("day10_input.txt", "r") as f: M = [ [*l] for l in f.read().splitlines() ]

start = None
for r, row in enumerate(M):
    for c, tile in enumerate(row):
        if tile == "S":
            start = (r,c)

r, c = start
loop = [ ]
while True:
    loop.append((r,c))
    match (M[r][c]):
        case "|": 
            if not (r-1,c) in loop:
                r -= 1
            elif not (r+1,c) in loop:
                r += 1
            else:
                break
        case "-":
            if not (r,c-1) in loop:
                c -= 1
            elif not (r,c+1) in loop:
                c += 1
            else:
                break
        case "L":
            if not (r-1,c) in loop:
                r -= 1
            elif not (r,c+1) in loop:
                c += 1
            else:
                break
        case "J":
            if not (r-1,c) in loop:
                r -= 1
            elif not (r,c-1) in loop:
                c -= 1
            else:
                break
        case "7":
            if not (r+1,c) in loop:
                r += 1
            elif not (r,c-1) in loop:
                c -= 1
            else:
                break
        case "F" | "S":
            if not (r,c+1) in loop:
                c += 1
            elif not (r+1,c) in loop:
                r += 1
            else:
                break

ans1 = len(loop) // 2 

ans2 = 0
for r in range(len(M)):
    for c in range(len(M[r])):
        if not (r,c) in loop:
            num_intersects = len([ (y,x) for (y,x) in loop if y == r and x >= c and M[y][x] in ["|", "L", "J"] ])
            if num_intersects % 2 != 0:
                ans2 += 1

print(f"""
*** ANSWERS:
    - Part 1 = '{ans1}'.
    - Part 2 = '{ans2}'.
""")