rules, parts, q = {}, [], []
with open("day19_input.txt", "r") as f:
    rules_str, parts_str = f.read().split("\n\n")
    for rule_str in rules_str.splitlines():
        name, rule_parts = rule_str[:-1].split("{")
        rules[name] = rule_parts.split(",")

    for part_str in parts_str.splitlines():
        part = {}
        for attr in part_str[1:-1].split(","):
            name, val = attr.split("=")
            part[name] = int(val)
        parts.append(part)
        q.append((part, "in"))

def eval_rule(rules : str, part: {}) -> str:
    for rule in rules:
        if ":" in rule:
            pred, dest = rule.split(":")
            attr_name, operand, value = pred[0:1], pred[1:2], pred[2:]
            value = int(value)

            match operand:
                case ">":
                    if part[attr_name] > value:
                        return dest
                case "<":
                    if part[attr_name] < value:
                        return dest
        else:
            return rule

def count(ranges, name):
    if name == "R":
        return 0
    elif name == "A":
        product = 1
        for r_start, r_end in ranges.values():
            product *= r_end - r_start + 1
        return product
    else:
        total = 0
        for rule in rules[name]:
            if ":" in rule:
                pred, dest = rule.split(":")
                attr_name, operand, value = pred[0:1], pred[1:2], pred[2:]
                value = int(value)
                
                r_start, r_end = ranges[attr_name]
                if operand == "<":
                    success_side = (r_start, value - 1)
                    failure_side = (value, r_end)
                else:
                    success_side = (value + 1, r_end)
                    failure_side = (r_start, value)
                if success_side[0] <= success_side[1]:
                    copy = dict(ranges)
                    copy[attr_name] = success_side
                    total += count(copy, dest)
                if failure_side[0] <= failure_side[1]:
                    ranges = dict(ranges)
                    ranges[attr_name] = failure_side
                else:
                    break
            else:
                total += count(ranges, rule)
            
        return total

ans1 = 0
while q:
    new_q = []
    for part, rule_name in q:
        new_rule_name = eval_rule(rules[rule_name], part)
        if new_rule_name == "A":
            ans1 += part["x"] + part["m"] + part["a"] + part["s"]
        elif new_rule_name == "R":
            pass
        else:
            new_q.append((part, new_rule_name))
    q = new_q

ans2 = count({"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000) }, "in")

print(f"ANSWERS -> part1=({ans1}) part2=({ans2}).")