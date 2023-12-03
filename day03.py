import re

with open("day03_input.txt", "r") as f:
    I = f.readlines()

# All special characters in the schematic
S = "".join(set("".join(I).replace("\n", "").translate({ord(i): None for i in '0123456789.'})))

def part_at(x: int, y: int) -> int:  # I did learn how to use `re.finditer`` after all!
    return int([match.group() for match in re.finditer(r'\d+', I[y]) if match.start() <= x <= match.end() ][0])

def gear_ratio(x: int, y: int) -> int:
    parts_found = []
    for y_offset, x_offset in [(-1, -1), (-1, 0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        # My puzzle input has NO '*' directly at any edges of the schematic, so omitting the try/except clause
        s = I[y + y_offset][x + x_offset]
        if s.isdigit():
            part = part_at(x=x + x_offset, y=y + y_offset)
            if part not in parts_found:
                parts_found.append(part)

    if len(parts_found) == 2:
        return parts_found[0] * parts_found[1]
    else:
        return 0  # Since we're summing ratio's, this is 'safe' to return 

sum_of_valid_parts, sum_of_gear_ratios = 0, 0
for y, line in enumerate(I):
    current_number = ""

    for x, c in enumerate(line.replace('\n', ".")):  # Add a '.' at the end, so we always hit our stop condition!
        if c.isdigit():
            current_number += c
        else:  # "stop condition" means, not finding more digits to add...
            if current_number != "":
                valid_part_found = False

                for y_offset in [-1, 0, 1]:  # Look around the entire part number
                    for x_offset in range(len(current_number) + 2):
                        try:  # (because testing array boundaries is for p&ssies...)
                            s = I[y + y_offset][x - x_offset]
                            if s in S:  # For special characters
                                valid_part_found = True
                        except IndexError as ie:
                            pass  # (because fsck 'em!)

                if valid_part_found:
                    sum_of_valid_parts += int(current_number)

            current_number = ""  # Reset and proceed looking for more part numbers

        if c == "*":
            sum_of_gear_ratios += gear_ratio(x, y)

print(f"""

*** ANSWERS:
      
  Part 1 = '{sum_of_valid_parts}'.
  Part 2 = '{sum_of_gear_ratios}'.

""")