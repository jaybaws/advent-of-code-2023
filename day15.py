with open("day15_input.txt", "r") as f: I = f.readline().strip().split(",")

def hash(s: str) -> int:
    current_value = 0
    for c in s:
        current_value = (17 * (current_value + ord(c))) % 256
    return current_value

focusing_power, boxes = 0, [ {} for i in range(256) ]
for operation in I:
    label = "".join([ c for c in operation if c.isalpha() ])
    box_num = hash(label)
    if "=" in operation:  # Add/replace
        boxes[box_num][label] = int(operation[-1])
    elif "-" in operation:  # Remove
        if label in boxes[box_num]:
            del boxes[box_num][label]

for box_number, box in enumerate(boxes):
    for slot_number, label in enumerate(box.keys()):
        focal_length = box[label]
        lens_strength = (box_number + 1) * (slot_number + 1) * focal_length
        focusing_power+= lens_strength

print(f"ANSWERS -> part1=({sum(list(map(hash, I)))}) part2=({focusing_power}).")