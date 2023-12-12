from typing import Tuple
from tqdm import tqdm

with open("day12_input.txt", "r") as f:
    I = [ (line.split()[0], tuple(map(int, line.split()[1].split(",")))) for line in f.read().splitlines() ]

DP_cache = {}

def possibilities(condition_mask:str, damaged:Tuple):
    DP_cache_key = (condition_mask, damaged)

    if condition_mask == "":
        return 1 if damaged == () else 0
    elif damaged == ():
        return 0 if "#" in condition_mask else 1
    elif DP_cache_key in DP_cache:
        return DP_cache[DP_cache_key]
    else:
        result = 0
        
        if condition_mask[0] in ".?":
            result += possibilities(condition_mask[1:], damaged)
            
        cur_dmg = damaged[0]
        if condition_mask[0] in "#?":
            if cur_dmg <= len(condition_mask) and "." not in condition_mask[:cur_dmg] and (cur_dmg == len(condition_mask) or condition_mask[cur_dmg] != "#"):
                result += possibilities(condition_mask[cur_dmg + 1:], damaged[1:])

        DP_cache[DP_cache_key] = result    

        return result

ans1 = ans2 = 0
for record1, check1 in tqdm(I):
    record2, check2 = "?".join([record1] * 5), check1 * 5
    ans1 += possibilities(record1, check1)
    ans2 += possibilities(record2, check2)

print(f"""
*** ANSWERS:
    - Part 1 = '{ans1}'.
    - Part 2 = '{ans2}'.
""")