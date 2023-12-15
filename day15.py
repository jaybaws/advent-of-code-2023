with open("day15_input.txt", "r") as f: I = f.readline().strip().split(",")

def hash(s: str) -> int:
    current_value = 0
    for c in s:
        current_value += ord (c)
        current_value *= 17
        current_value = current_value % 256
    return current_value

ans1 = sum(list(map(hash, I)))

ans2 = 0
boxes = [ {} for i in range(256) ]
for op in I:
    label = "".join([ c for c in op if c.isalpha() ])
    box_num = hash(label)

    if "=" in op:
        focal_length = int(op[-1])
        if label not in boxes[box_num]:  # Add
            boxes[box_num][label] = focal_length
        else:  # Replace
            boxes[box_num][label] = focal_length

    elif "-" in op:  # Remove
        if label in boxes[box_num]:
            del boxes[box_num][label]

for box_number, box in enumerate(boxes):
    if box != {}:
        for slot, label in enumerate(box.keys()):
            focal_length = box[label]
            lens_strength = (box_number+1) * (slot+1) * focal_length
            ans2+= lens_strength

print(f"ANSWERS -> part1=({ans1}) part2=({ans2}).")