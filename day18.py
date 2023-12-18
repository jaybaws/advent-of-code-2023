D = { "U": (-1, +0), "3": (-1, +0), "D": (+1, +0), "1": (+1, +0), "L": (+0, -1), "2": (+0, -1), "R": (+0, +1), "0": (+0, +1) }

edges1 = []
edges2 = []
pos1 = (0,0)
pos2 = (0, 0)
circumference1 = 0
circumference2 = 0

with open("day18_input.txt", "r") as f:
    for line in f.read().splitlines():
        sr1, sc1 = pos1
        sr2, sc2 = pos2

        dir1, length_str, color = line.split(" ")
        dir2 = color[7:8]

        len1 = int(length_str)
        len2 = int(color[2:7], 16)

        circumference1 += len1
        circumference2 += len2
        
        dr1, dc1 = D[dir1]
        dr2, dc2 = D[dir2]

        pos1 = (sr1+(dr1*len1),sc1+(dc1*len1))
        pos2 = (sr2+(dr2*len2),sc2+(dc2*len2))

        edges1.append(((sr1,sc1), pos1))
        edges2.append(((sr2,sc2), pos2))

shoelace_area1 = abs(sum(edges1[i][0][1] * (edges1[(i+1) % len(edges1)][0][0] - edges1[i-1][0][0]) for i in range(len(edges1)))) / 2
inner_area1 = shoelace_area1 - circumference1 // 2 + 1
total_area1 = circumference1 + inner_area1

shoelace_area2 = abs(sum(edges2[i][0][1] * (edges2[(i+1) % len(edges2)][0][0] - edges2[i-1][0][0]) for i in range(len(edges2)))) / 2
inner_area2 = shoelace_area2 - circumference2 // 2 + 1
total_area2 = circumference2 + inner_area2

print(f"ANSWERS -> part1=({int(total_area1)}) part2=({int(total_area2)}).")