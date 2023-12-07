from typing import List

def card_value(card: str, v: str) -> int: return v.find(card) + 1

class Hand:
    def __init__(self, line: str):
        self.cards_str, self.bid_str = line.strip().split(" ")

    def score(self, jokers: bool = False):
        V = "J23456789T_QKA" if jokers else "_23456789TJQKA"
        joker_count = self.cards_str.count("J") if jokers else 0
        hand_score, counts, card_score_str = 0, [], ""

        for c in set([*self.cards_str]):
            counts.append(self.cards_str.count(c))
        
        match sorted(counts, reverse=True):
            case [5]:  # Five-of-a-kind
                hand_score = 7
            case [4, 1]:  # Four-of-a-kind
                hand_score = 6
                match joker_count:
                    case 1 | 4: hand_score = 7
            case [3, 2]:  # Full-house
                hand_score = 5
                match joker_count:
                    case 2 | 3: hand_score = 7
            case [3, 1, 1]:  # Three-of-a-kind
                hand_score = 4
                match joker_count:
                    case 1 | 3: hand_score = 6
            case [2, 2, 1]:  # Two-pair
                hand_score = 3
                match joker_count:
                    case 1: hand_score = 5
                    case 2: hand_score = 6
            case [2, 1, 1, 1]:  # One-pair
                hand_score = 2
                match joker_count:
                    case 1 | 2: hand_score = 4
            case [1, 1, 1, 1, 1]:  # High-card
                hand_score = 1
                match joker_count:
                    case 1: hand_score = 2

        for c in [*self.cards_str]:
            card_score_str += str(card_value(c, V)).zfill(2)

        return (hand_score, int(card_score_str), int(self.bid_str))

hands: List[Hand] = []
with open("day07_input.txt", "r") as f:
    for line in f.readlines():
        hands.append(Hand(line))

print(f"""
*** ANSWERS:
    - Part 1 = '{sum([ int(h.bid_str) * (i + 1) for i, h in enumerate(sorted(hands, key=lambda h: h.score())) ])}'.
    - Part 2 = '{sum([ int(h.bid_str) * (i + 1) for i, h in enumerate(sorted(hands, key=lambda h: h.score(jokers=True))) ])}'.
""")