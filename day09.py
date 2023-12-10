with open("day09_input.txt", "r") as f: S = [ list(map(int, l.split())) for l in f.read().splitlines() ]
total_p1 = total_p2 = 0

def determine_deltas(r):
    result = []
    for i in range(len(r) - 1):
        result.append(r[i + 1] - r[i])
    return result

for s in S:
    deltas, top_left = [], s[0]
    while not all([ v == 0 for v in s ]):
        total_p1 += s[-1]
        s = determine_deltas(s)
        deltas.append((s[0], s[-1]))

    lefty, _ = deltas.pop()
    while len(deltas) > 0:
        l, _ = deltas.pop()
        lefty = l - lefty
    total_p2 += top_left - lefty
    
print(f"""
*** ANSWERS:
    - Part 1 = '{total_p1}'.
    - Part 2 = '{total_p2}'.
""")