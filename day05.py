from typing import List, Tuple

with open("day05_input.txt", "r") as f: I = f.read()

def substring_between(s: str, l: str, r: str) -> str:
    return s[s.find(l) + len(l): s.find(r)]

def substring_after(s: str, l: str) -> str:
    return s[s.find(l) + len(l):]

def parse(s: str) -> (int, int, int):
    return tuple(map(int, s.split()))

seeds = list(map(int, substring_between(I, "seeds: ", "\n").split()))
seed_to_soil_map_map = list(map(parse, substring_between(I, "seed-to-soil map:\n", "\n\nsoil-to-fertilizer map:").split("\n")))
soil_to_fertilizer_map = list(map(parse, substring_between(I, "soil-to-fertilizer map:\n", "\n\nfertilizer-to-water map:").split("\n")))
fertilizer_to_water_map = list(map(parse, substring_between(I, "fertilizer-to-water map:\n", "\n\nwater-to-light map:").split("\n")))
water_to_light_map = list(map(parse, substring_between(I, "water-to-light map:\n", "\n\nlight-to-temperature map:").split("\n")))
light_to_temperature_map = list(map(parse, substring_between(I, "light-to-temperature map:\n", "\n\ntemperature-to-humidity map:").split("\n")))
temperature_to_humidity_map = list(map(parse, substring_between(I, "temperature-to-humidity map:\n", "\n\nhumidity-to-location map:").split("\n")))
humidity_to_location_map = list(map(parse, substring_after(I, "humidity-to-location map:\n").split("\n")))

# Part 1
def map_value(v: int, m: List[Tuple[int, int, int]]) -> int:
    for (dest_range_start, source_range_start, range_length) in m:
        if source_range_start <= v <= source_range_start + range_length:
            return dest_range_start + (v - source_range_start)

    return v

def seed_to_location(s: int) -> int:
    result = s
    for m in [ seed_to_soil_map_map, soil_to_fertilizer_map,
               fertilizer_to_water_map, water_to_light_map,
               light_to_temperature_map, temperature_to_humidity_map,
               humidity_to_location_map ]:
        result = map_value(result, m)

    return result

print(f"Answer to part one: {min([ seed_to_location(seed) for seed in seeds ])}.")

# Part 2...
seed_ranges = [ (v, v + seeds[i + 1] - 1) for i, v in enumerate(seeds) if i % 2 == 0 ]

for mapping in [ seed_to_soil_map_map, soil_to_fertilizer_map,
            fertilizer_to_water_map, water_to_light_map,
            light_to_temperature_map, temperature_to_humidity_map,
            humidity_to_location_map ]:

    ranges = []
    for m in mapping:
        ranges.append(m)
    new = []
    while len(seed_ranges) > 0:
        seed_range_start, seed_range_end = seed_ranges.pop()
        for dest_range_start, source_range_start, range_size in ranges:
            overlap_start = max(seed_range_start, source_range_start)
            overlap_end = min(seed_range_end, source_range_start + range_size)
            if overlap_start < overlap_end:
                new.append((overlap_start - source_range_start + dest_range_start, overlap_end - source_range_start + dest_range_start))
                if overlap_start > seed_range_start:
                    seed_ranges.append((seed_range_start, overlap_start))
                if seed_range_end > overlap_end:
                    seed_ranges.append((overlap_end, seed_range_end))
                break
        else:
            new.append((seed_range_start, seed_range_end))
    seed_ranges = new

print(f"Answer to part two: {min(seed_ranges)[0]}.")