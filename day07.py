from typing import List

class Hand:
    def __init__(self, line: str):
        self.cards_str, self.bid_str = line.strip().split(" ")

    def score(self, jokers: bool = False):
        V = "J23456789T_QKA" if jokers else "_23456789TJQKA"
        joker_count = self.cards_str.count("J") if jokers else 0
        counts, score = [], ""

        for c in set([*self.cards_str]):
            counts.append(self.cards_str.count(c))
        
        match sorted(counts, reverse=True):
            case [5]:  # Five-of-a-kind
                score = "7"
            case [4, 1]:  # Four-of-a-kind
                score = "6"
                match joker_count:
                    case 1 | 4: score = "7"
            case [3, 2]:  # Full-house
                score = "5"
                match joker_count:
                    case 2 | 3: score = "7"
            case [3, 1, 1]:  # Three-of-a-kind
                score = "4"
                match joker_count:
                    case 1 | 3: score = "6"
            case [2, 2, 1]:  # Two-pair
                score = "3"
                match joker_count:
                    case 1: score = "5"
                    case 2: score = "6"
            case [2, 1, 1, 1]:  # One-pair
                score = "2"
                match joker_count:
                    case 1 | 2: score = "4"
            case [1, 1, 1, 1, 1]:  # High-card
                score = "1"
                match joker_count:
                    case 1: score = "2"

        for c in [*self.cards_str]:
            score += str(V.find(c) + 1).zfill(2)

        return (int(score), int(self.bid_str))

hands: List[Hand] = []
with open("day07_input.txt", "r") as f:
    for line in f.readlines():
        hands.append(Hand(line))

for part, with_jokers in [ (1, False), (2, True) ]:
    print(f"Answer {part}: '{sum([ int(h.bid_str) * (i + 1) for i, h in enumerate(sorted(hands, key=lambda h: h.score(jokers=with_jokers))) ])}'. ")