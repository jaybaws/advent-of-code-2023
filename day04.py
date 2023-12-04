with open("day04_input.txt", "r") as f:
    I = f.readlines()

pile_value = 0
copies = [1 for _ in range(len(I))]
scores = [1 for _ in range(len(I))]

for game, card in enumerate(I):
    numbers = card.split(": ")[1].split(" | ")
    winners = [ int(c) for c in numbers[0].split() ]
    stack = [ int(c) for c in numbers[1].split() ]
    matches = len([ c for c in stack if c in winners])
    score = 2 ** (matches - 1) if matches > 1 else matches
    pile_value += score
    scores[game] = score

    for r in range(copies[game]):
        for i in range(matches):
            copies[game + 1 + i] += 1

print(f"""

*** ANSWERS:
      
  Part 1 = '{pile_value}'.
  Part 2 = '{sum(copies)}'.

""")