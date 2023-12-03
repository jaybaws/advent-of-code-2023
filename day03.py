with open("day03_input.txt", "r") as f:
    I = f.readlines()

# All special characters in the schematic
S = "".join(set("".join(I).replace("\n", "").translate({ord(i): None for i in '0123456789.'})))


def part_at(x, y) -> int:
    middle, left, right = I[y][x], "", ""
    
    x_pos = x - 1  # Search left
    while I[y][x_pos].isdigit():
        left += I[y][x_pos]
        x_pos -= 1

    x_pos = x + 1  # Search right
    while I[y][x_pos].isdigit():
        right += I[y][x_pos]
        x_pos += 1

    return int(f"{left[::-1]}{middle}{right}")  # Reverse the left part, as we searched backwards!


def gear_ratio(x: int, y: int) -> int:
    parts_found = []
    for y_offset in [-1, 0, 1]:
        for x_offset in [-1, 0, 1]:
            # My puzzle input has NO '*' chars at the borders, so omitting the try/except clause
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
    number_str = ""
    
    # The 'use' the line-end as a free '.'.
    # We need a non-digit at the end of the line to stop searching for more digits 
    # and to startg determining if it's a valid part.  Otherwise, a part-number at
    # the end of the line simply gets ignored...
    for x, c in enumerate(line.replace('\n', ".")):
        if c.isdigit():
            number_str += c
        else:
            if number_str != "":
                valid_part_found = False

                for y_offset in [-1, 0, 1]:
                    for x_offset in range(len(number_str) + 2):
                        try:  # Because testing array bounds is for p&ssies
                            s = I[y + y_offset][x - x_offset]
                            if s in S:
                                valid_part_found = True
                        except IndexError as ie:
                            pass

                if valid_part_found:
                    sum_of_valid_parts += int(number_str)

            number_str = ""

        if c == "*": # This is only for part 2
            sum_of_gear_ratios += gear_ratio(x, y)

print(f"""

*** ANSWERS:
      
  Part 1 = '{sum_of_valid_parts}'.
  Part 2 = '{sum_of_gear_ratios}'.

""")