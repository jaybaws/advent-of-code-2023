from heapq import heappush, heappop

with open("day17_input.txt", "r") as f:
    D = [ [int(c) for c in line.strip() ] for line in f.read().splitlines() ]
    H = len(D)
    W = len(D[0])

def total_heat_loss(min_steps: int, max_steps: int, neighbouring_directions=[ (0, 1), (1, 0), (0, -1), (-1, 0) ]) -> int:
    priority_queue, seen = [ (0, 0, 0, 0, 0, 0) ], set()

    while priority_queue:
        heat_loss, r, c, dr, dc, n = heappop(priority_queue)
        
        if (r, c) == (H-1, W-1) and n >= min_steps:
            return heat_loss
        
        elif not (r, c, dr, dc, n) in seen:
            seen.add((r, c, dr, dc, n))
            
            if n < max_steps and (dr, dc) != (0, 0):
                nr = r + dr
                nc = c + dc
                if 0<=nr<H and 0<=nc<W:
                    heappush(priority_queue, (heat_loss + D[nr][nc], nr, nc, dr, dc, n + 1))
            
            if n >= min_steps or (dr, dc) == (0, 0):
                for ndr, ndc in neighbouring_directions:
                    if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                        nr, nc = r + ndr, c + ndc
                        if 0<=nr<H and 0<=nc<W:
                            heappush(priority_queue, (heat_loss + D[nr][nc], nr, nc, ndr, ndc, 1))

print(f"ANSWERS -> part1=({total_heat_loss(1, 3)}) part2=({total_heat_loss(4, 10)}).")