with open("day02_input.txt", "r") as f:
    I = f.readlines()

sum_of_valid_games, sum_of_powers = 0, 0

for i, l in enumerate(I):
    game_number, game_line = i + 1, l.strip().split(": ")[1]
    part1_satisfied, min_red, min_green, min_blue = True, 0, 0, 0

    for reveal in game_line.split("; "):
        for cubes in reveal.split(", "):
            amount_str, color = cubes.split(" ")
            amount = int(amount_str)

            if (color == "red" and amount > 12) or (color == "green" and amount > 13) or (color == "blue" and amount > 14):
                part1_satisfied = False

            if (color == "red" and amount > min_red):
                min_red = amount
            if (color == "blue" and amount > min_blue):
                min_blue = amount
            if (color == "green" and amount > min_green):
                min_green = amount

    if part1_satisfied:
        sum_of_valid_games += game_number

    sum_of_powers += min_red*min_blue*min_green

print(f"""

*** ANSWERS:
      
  Part 1 = '{sum_of_valid_games}'.
  Part 2 = '{sum_of_powers}'.

""")