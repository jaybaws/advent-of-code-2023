from collections import deque
from typing import Tuple

with open("day16_input.txt", "r") as f:
    M = [ [*line.strip()] for line in f.read().splitlines() ]
    H = len(M)
    W = len(M[0])

def energy(start: Tuple[int, int], heading: Tuple[int, int]) -> int:
    tiles_to_consider = deque([ (start, heading) ])
    tiles_seen = set()

    while tiles_to_consider:
        (x, y), (dx, dy) = tiles_to_consider.popleft()
        x, y = x+dx, y+dy

        if 0 <= x < W and 0 <= y < H:
            s = M[y][x]
            
            if s == "/":
                dy, dx = -dx, -dy
            elif s == "\\":
                dy, dx = dx, dy

            if ((x, y), (dx, dy)) not in tiles_seen:
                tiles_seen.add(((x, y), (dx, dy)))
                match s:
                    case "-":
                        tiles_to_consider.append(((x, y), (-1, 0)))
                        tiles_to_consider.append(((x, y), (+1, 0)))
                    case "|":
                        tiles_to_consider.append(((x, y), (0, -1)))
                        tiles_to_consider.append(((x, y), (0, +1)))
                    case _:
                        tiles_to_consider.append(((x, y), (dx, dy)))

    return len(set([ (x, y) for ((x, y), _) in tiles_seen ]))

ans1 = energy((-1, 0), (+1, 0))

ans2 = 0
for x in range(W):
    ans2 = max(ans2, energy((x, -1), (0, +1)), energy((x, H), (0, -1)))
for y in range(H):
    ans2 = max(ans2, energy((-1, y), (+1, 0)), energy((W, y), (-1, 0)))

print(f"ANSWERS -> part1=({ans1}) part2=({ans2}).")