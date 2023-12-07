from typing import List


def card_value(card: str, v: str) -> int:
   return v.find(card) + 1


class Hand:
    def __init__(self, line: str):
        self.cards_str, self.bid_str = line.strip().split(" ")
        self.bid = int(self.bid_str)
        self.cards = [*self.cards_str]

    def score_p1(self):
        V = "_23456789TJQKA"
        hand_score = 0
        counts = []
        card_score_str = ""

        for c in set(self.cards):
           counts.append(self.cards_str.count(c))

        match sorted(counts, reverse=True):
          case [5]: hand_score = 7  # Five-of-a-kind
          case [4, 1]: hand_score = 6  # Four-of-a-kind
          case [3, 2]: hand_score = 5  # Full-house
          case [3, 1, 1]: hand_score = 4  # Three-of-a-kind
          case [2, 2, 1]: hand_score = 3  # Two-pair
          case [2, 1, 1, 1]: hand_score = 2  # One-pair
          case [1, 1, 1, 1, 1]: hand_score = 1  # High-card

        for c in self.cards:
           card_score_str += str(card_value(c, V)).zfill(2)

        return (hand_score, int(card_score_str), self.bid)

    def score_p2(self):
        V = "J23456789T_QKA"
        hand_score = 0
        counts = []
        card_score_str = ""

        for c in set(self.cards):
           counts.append(self.cards_str.count(c))

        joker_count = self.cards_str.count("J")
        match sorted(counts, reverse=True):
          case [5]:  # Five-of-a-kind
              hand_score = 7

          case [4, 1]:  # Four-of-a-kind
              hand_score = 6
              match joker_count:
                 case 1: hand_score = 7
                 case 4: hand_score = 7

          case [3, 2]:  # Full-house
              hand_score = 5
              match joker_count:
                case 2: hand_score = 7
                case 3: hand_score = 7

          case [3, 1, 1]:  # Three-of-a-kind
              hand_score = 4
              match joker_count:
                case 1: hand_score = 6
                case 3: hand_score = 6

          case [2, 2, 1]:  # Two-pair
              hand_score = 3
              match joker_count:
                case 1: hand_score = 5
                case 2: hand_score = 6

          case [2, 1, 1, 1]:  # One-pair
              hand_score = 2
              match joker_count:
                case 1: hand_score = 4
                case 2: hand_score = 4

          case [1, 1, 1, 1, 1]:  # High-card
              hand_score = 1
              match joker_count:
                case 1: hand_score = 2

        for c in self.cards:
           card_score_str += str(card_value(c, V)).zfill(2)

        return (hand_score, int(card_score_str), self.bid)


F = "day07_input.txt"
hands: List[Hand] = []
with open(F, "r") as f:
  for line in f.readlines():
    hands.append(Hand(line))

ans1 = sum([ h.bid * (i + 1) for i, h in enumerate(sorted(hands, key=lambda h: h.score_p1())) ])
ans2 = sum([ h.bid * (i + 1) for i, h in enumerate(sorted(hands, key=lambda h: h.score_p2())) ])

print(f"""

*** ANSWERS:
      
  Part 1 = '{ans1}'.
  Part 2 = '{ans2}'.

""")