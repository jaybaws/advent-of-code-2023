from perf import clock
from timeit import timeit

# Part ONE
def get_input(file : str):
    with open(file, "r") as f:    
        return [ line for line in f.readlines() ]

def only_digits(s: str) -> str:
    number = "".join([e for e in s if e.isdigit()])
    return number

def value(s: str) -> int:
    return int(s[0])*10 + int(s[-1])

#@clock
def part1() -> int:
    digits = [only_digits(line) for line in get_input("day01_input.txt") ]
    numbers = [ value(d) for d in digits ]
    return sum(numbers)

# Part TWO
def first_digit(s: str) -> int:
    if s[0].isdigit():
        return int(s[0])
    elif s.startswith("one"):
        return "1"
    elif s.startswith("two"):
        return "2"
    elif s.startswith("three"):
        return "3"
    elif s.startswith("four"):
        return "4"
    elif s.startswith("five"):
        return "5"
    elif s.startswith("six"):
        return "6"
    elif s.startswith("seven"):
        return "7"
    elif s.startswith("eight"):
        return "8"
    elif s.startswith("nine"):
        return "9"
    else:
        return first_digit(s[1:])

def last_digit(s: str) -> int:
    if s[-1].isdigit():
        return int(s[-1])
    elif s.endswith("one"):
        return "1"
    elif s.endswith("two"):
        return "2"
    elif s.endswith("three"):
        return "3"
    elif s.endswith("four"):
        return "4"
    elif s.endswith("five"):
        return "5"
    elif s.endswith("six"):
        return "6"
    elif s.endswith("seven"):
        return "7"
    elif s.endswith("eight"):
        return "8"
    elif s.endswith("nine"):
        return "9"
    else:
        return last_digit(s[:-1])

def fix(s: str) -> str:
    first, last = first_digit(s), last_digit(s)
    return f"{first}{last}"

#@clock
def part2() -> None:
    digits = [fix(line.strip()) for line in get_input("day01_input.txt") ]
    numbers = [ value(d) for d in digits ]
    return sum(numbers)

# RESULTS
a1 = part1()
a2 = part2()

print("\n\n")
print(f"Ansers 1 = '{a1}', and answer 2 = '{a2}'.")
print("\n\n")

# PERF crap
a1_speed = timeit(stmt=part1, number=100)
print(f"part 1 took {a1_speed/100} sec.")

a2_speed = timeit(stmt=part2, number=100)
print(f"part 2 took {a2_speed/100} sec.")