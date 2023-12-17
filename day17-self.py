from math import inf as infinity
from collections import defaultdict
from typing import Dict, Tuple, Set

UP, DOWN, LEFT, RIGHT = (-1,0), (1,0), (0, -1), (0, 1)
all_directions = [ UP, DOWN, LEFT, RIGHT ]

with open("day17a_input_sample.txt", "r") as f:
    D = [ [int(c) for c in line.strip() ] for line in f.read().splitlines() ]
    H = len(D)
    W = len(D[0])
    graph = defaultdict(lambda : infinity)
    graph[(0,0)] = 0
    processed = set([])

def key_of_smallest(d: Dict[Tuple[int, int], int]) -> Tuple[int, int]:
    key = None
    min_val = infinity
    
    for k, d in d.items():
        if d < min_val:
            key = k
            min_val = d
            
    return key

def neighbour_coords(r, c):
    return [ (r+dr, c+dc) for (dr, dc) in all_directions if 0<=r+dr<H and 0<=c+dc<W ]

def unprocessed(g: Dict, s: Set):
    return { key:value for (key,value) in g.items() if key not in s }

while (H-1, W-1) not in processed:
    (r, c) = key_of_smallest(unprocessed(graph, processed))

    for (nr, nc) in neighbour_coords(r, c):
        graph[(nr, nc)] = min([ graph[ (nr, nc) ] ] + [ graph[(nnr, nnc)]+D[nnr][nnc] for nnr, nnc in neighbour_coords(nr, nc) ])

    processed.add((r, c))

print(f"Dijkstra done --> {graph[(H-1, W-1)]}")