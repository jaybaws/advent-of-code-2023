from typing import List, Tuple
from math import sqrt, ceil, floor

I1_sample, I1, I2_sample, I2 = [ (7, 9), (15, 40), (30, 200) ], [ (47,400), (98,1213), (66, 1011), (98,1540) ], [ (71530, 940200) ], [ (47986698, 400121310111540) ]

def ways_by_math(races: List[Tuple[int, int]]) -> int:
    result = 1
    
    for total_time, record in races:
        determinant = (total_time ** 2) - (4 * (record + 1))  # Aim for *improvement* of the record!
        charging_time_min = ceil( ((-1 * total_time) + sqrt(determinant)) / -2 )
        charging_time_max = floor( ((-1 * total_time) - sqrt(determinant)) / -2 )
        ways_to_win = charging_time_max - charging_time_min + 1

        result *= ways_to_win

    return result

print(f"""

*** ANSWERS:
      
  Part 1 = '{ways_by_math(I1)}'.
  Part 2 = '{ways_by_math(I2)}'.

""")