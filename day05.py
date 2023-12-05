with open("day05_input.txt", "r") as f: I = f.read()

def substring_between(test_str: str, sub1: str, sub2: str) -> str:
    return test_str[test_str.find(sub1) + len(sub1): test_str.find(sub2)]

def substring_after(test_str: str, sub1: str) -> str:
    return test_str[test_str.find(sub1) + len(sub1):]

def parse(input: str) -> (int, int, int):
    items = input.split()
    return (int(items[0]), int(items[1]), int(items[2]))

seeds = list(map(int, substring_between(I, "seeds: ", "\n").split()))
seed_to_soil_map_map = list(map(parse, substring_between(I, "seed-to-soil map:\n", "\n\nsoil-to-fertilizer map:").split("\n")))
soil_to_fertilizer_map = list(map(parse, substring_between(I, "soil-to-fertilizer map:\n", "\n\nfertilizer-to-water map:").split("\n")))
fertilizer_to_water_map = list(map(parse, substring_between(I, "fertilizer-to-water map:\n", "\n\nwater-to-light map:").split("\n")))
water_to_light_map = list(map(parse, substring_between(I, "water-to-light map:\n", "\n\nlight-to-temperature map:").split("\n")))
light_to_temperature_map = list(map(parse, substring_between(I, "light-to-temperature map:\n", "\n\ntemperature-to-humidity map:").split("\n")))
temperature_to_humidity_map = list(map(parse, substring_between(I, "temperature-to-humidity map:\n", "\n\nhumidity-to-location map:").split("\n")))
humidity_to_location_map = list(map(parse, substring_after(I, "humidity-to-location map:\n").split("\n")))

# Part 1
def do_map(val: int, mapping: list[(int,int,int)]) -> int:
    for (dest_range_start, source_range_start, range_length) in mapping:
        if source_range_start <= val <= source_range_start + range_length:
            return dest_range_start + (val-source_range_start)

    return val

def seed_to_location(seed: int) -> int:
    return do_map(do_map(do_map(do_map(do_map(do_map(do_map(seed, seed_to_soil_map_map), soil_to_fertilizer_map), fertilizer_to_water_map), water_to_light_map), light_to_temperature_map), temperature_to_humidity_map), humidity_to_location_map)

print(f"Answer to part one: {min([ seed_to_location(seed) for seed in seeds ])}.")

# Part 2...
seed_ranges = [ range(v, v+seeds[i+1]) for i, v in enumerate(seeds) if i % 2 == 0 ]
...