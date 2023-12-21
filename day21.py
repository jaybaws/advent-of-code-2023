from collections import deque
from typing import List, Tuple
from tqdm import tqdm

reachable_coords = set([])
M: List[List[str]] = []

with open("day21_input.txt", "r") as f:
    M = [ [ *line ] for line in f.read().splitlines() ]
    H = len(M)
    W = len(M[0])
    
    for r in range(H):
        for c in range(W):
            if M[r][c] == "S":
                reachable_coords.add((r, c))


def adj(r: int, c: int) -> List[Tuple[int, int]]:
    return [ (r+dr, c+dc) for dr,dc in [(+1,0),(-1,0),(0,+1),(0,-1)] if 0<=r+dr<H and 0<=c+dc<W and M[r+dr][c+dc] in ".S" ]

def display(rc):
    print("\n\n")
    for y in range(H):
        print("")
        for x in range(W):
            s = "O" if (y,x) in rc else M[y][x]
            print(s, end="")


seen = []
for step in range(26501365):
    new_reachable_coords = []
    while reachable_coords:
        (r, c) = reachable_coords.pop()
        new_reachable_coords += adj(r, c)
   
    reachable_coords.update(set(new_reachable_coords))

    if reachable_coords in seen:
        print(f"W00000T! at {step}.")
    else:
        seen.append(reachable_coords)

ans1 = len(reachable_coords)

print(f"ANSWERS -> part1=({ans1}) part2=({None}).")