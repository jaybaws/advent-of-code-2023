from math import gcd
from itertools import cycle

with open("day08_input.txt", "r") as f: I = f.readlines()

directions = [ 0 if d == "L" else 1 for d in [ *I[0].strip() ] ]
nodes = { n[0:3]:(n[7:10], n[12:15]) for n in I[2:] }

# Part one
at_node = 'AAA'
for i, direction in enumerate(cycle(directions)):
    at_node = nodes[at_node][direction]
    if at_node == "ZZZ":
        print(f"Answer 1: {i + 1}")
        break

# Part two
trips = []
for at_node in [ n for n in nodes.keys() if n.endswith('A') ]:
    for i, direction in enumerate(cycle(directions)):
        at_node = nodes[at_node][direction]
        if at_node.endswith("Z"):
            trips.append(i + 1)
            break

lcm = trips[0]
for trip in trips[1:]:
    lcm = lcm * trip // gcd(lcm, trip)

print(f"Answer 2: {lcm}")