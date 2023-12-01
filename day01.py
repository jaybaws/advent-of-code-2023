from timeit import timeit

# COMMON
def get_input(file : str):
    with open(file, "r") as f:    
        return [ line for line in f.readlines() ]

# HELPERS
def first_digit(s: str, part_2: bool = False) -> int:
    if s[0].isdigit():
        return int(s[0])
    
    if part_2:
        if s.startswith("one"):
            return 1
        elif s.startswith("two"):
            return 2
        elif s.startswith("three"):
            return 3
        elif s.startswith("four"):
            return 4
        elif s.startswith("five"):
            return 5
        elif s.startswith("six"):
            return 6
        elif s.startswith("seven"):
            return 7
        elif s.startswith("eight"):
            return 8
        elif s.startswith("nine"):
            return 9

    return first_digit(s[1:], part_2)

def last_digit(s: str, part_2: bool = False) -> int:
    if s[-1].isdigit():
        return int(s[-1])
    
    if part_2:
        if s.endswith("one"):
            return 1
        elif s.endswith("two"):
            return 2
        elif s.endswith("three"):
            return 3
        elif s.endswith("four"):
            return 4
        elif s.endswith("five"):
            return 5
        elif s.endswith("six"):
            return 6
        elif s.endswith("seven"):
            return 7
        elif s.endswith("eight"):
            return 8
        elif s.endswith("nine"):
            return 9

    return last_digit(s[:-1], part_2)

# PART ONE
def part1() -> int:
    return sum([ (10 * first_digit(line, False)) + last_digit(line, False) for line in get_input("day01_input.txt") ])

# PART TWO
def part2() -> None:
    return sum([ (10 * first_digit(line, True)) + last_digit(line, True) for line in get_input("day01_input.txt") ])

# RESULTS
part1_result = part1()
part2_result = part2()
part1_avg_duration = timeit(stmt=part1, number=100) / 100
part2_avg_duration = timeit(stmt=part2, number=100) / 100

print(f"""

*** ANSWERS:
      
  Part 1 = '{part1()}' (and took on average {part1_avg_duration} sec).
  Part 2 = '{part2()}' (and took on average {part2_avg_duration} sec).

""")