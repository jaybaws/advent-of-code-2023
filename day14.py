from copy import deepcopy
from typing import List

with open("day14_input.txt", "r") as f:
    P = [ [*line] for line in f.read().splitlines() ]

def roll(M: List[List[str]]):
    for col in range(len(M[0])):
        did_something = None
        while did_something in [None, True]:
            did_something = False
            bound = -1
            for row in range(len(M)):
                match M[row][col]:
                    case "#":
                        bound = row
                    case "O":
                        if row > bound+1 and M[row-1][col] == ".":
                            M[row][col] = "."
                            M[row-1][col] = "O"
                            did_something = True

def total_load(M: List[List[str]]) -> int:
    total = 0
    for i in range(len(M)):
        weight = len(M) - i
        total += weight * len([ 1 for x in M[i] if x == "O" ])
    return total

def rotate(original):
    return [list(r) for r in zip(*original[::-1])]

def cycle(M: List[List[str]]) -> List[List[str]]:
    roll(M) # North
    M = rotate(M)
    roll(M) # West
    M = rotate(M)
    roll(M)  # South
    M = rotate(M)
    roll(M) # East
    M = rotate(M)
    return M

def part_one(M: List[List[str]]) -> int:
    roll(M)
    return total_load(M)

def part_two(M: List[List[str]]) -> int:
    seen = loads = {}
    seen[str(M)] = 0
    loads[0] = total_load(M)

    for occurrance in range(1, 1_000_000_000+1):
        M = cycle(M)
        key = str(M)
        if key in seen:
            first_occurance = seen[key]
            true_value_at = (1_000_000_000 - first_occurance) % (occurrance - first_occurance) + first_occurance
            return loads[true_value_at]
        else:
            seen[key] = occurrance
            loads[occurrance] = total_load(M)

print(f"""

*** ANSWERS:
      
  Part 1 = '{part_one(deepcopy(P))}'.
  Part 2 = '{part_two(deepcopy(P))}'.

""")