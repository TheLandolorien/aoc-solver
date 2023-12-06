import sys
import typing

from collections import namedtuple
from itertools import zip_longest

from aoc_solver.object_types import Solution

MapRange = namedtuple("MapRange", ["dest_start", "src_start", "range"])
Almanac = namedtuple(
    "Almanac",
    [
        "seed_maps",
        "soil_maps",
        "fertilizer_maps",
        "water_maps",
        "light_maps",
        "temperature_maps",
        "humidity_maps",
        "location_maps",
    ],
)

# --- Day 5: If You Give A Seed A Fertilizer ---
# Source: https://adventofcode.com/2023/day/5


def find_closest_location(puzzle_input: typing.List[str], ranged_seeds: bool = False) -> int:
    almanac = build_almanac(raw_almanac=puzzle_input, ranged_seeds=ranged_seeds)

    closest_location = sys.maxsize
    for seed_map in almanac.seed_maps:
        for seed in range(seed_map.src_start, seed_map.src_start + seed_map.range):
            soil = get_mapped_value(map_ranges=almanac.soil_maps, src=seed)
            fertilizer = get_mapped_value(map_ranges=almanac.fertilizer_maps, src=soil)
            water = get_mapped_value(map_ranges=almanac.water_maps, src=fertilizer)
            light = get_mapped_value(map_ranges=almanac.light_maps, src=water)
            temperature = get_mapped_value(map_ranges=almanac.temperature_maps, src=light)
            humidity = get_mapped_value(map_ranges=almanac.humidity_maps, src=temperature)
            location = get_mapped_value(map_ranges=almanac.location_maps, src=humidity)

            if location < closest_location:
                closest_location = location

    return closest_location


def build_almanac(raw_almanac: typing.List[str], ranged_seeds: bool = False) -> Almanac:
    to_soil_start = raw_almanac.index("seed-to-soil map:") + 1
    to_fertilizer_start = raw_almanac.index("soil-to-fertilizer map:") + 1
    to_water_start = raw_almanac.index("fertilizer-to-water map:") + 1
    to_light_start = raw_almanac.index("water-to-light map:") + 1
    to_temperature_start = raw_almanac.index("light-to-temperature map:") + 1
    to_humidity_start = raw_almanac.index("temperature-to-humidity map:") + 1
    to_location_start = raw_almanac.index("humidity-to-location map:") + 1

    return Almanac(
        seed_maps=parse_seed_maps(maps=raw_almanac[0].split(": ")[1], ranged_seeds=ranged_seeds),
        soil_maps=parse_maps(maps=raw_almanac[to_soil_start : to_fertilizer_start - 2]),
        fertilizer_maps=parse_maps(maps=raw_almanac[to_fertilizer_start : to_water_start - 2]),
        water_maps=parse_maps(maps=raw_almanac[to_water_start : to_light_start - 2]),
        light_maps=parse_maps(maps=raw_almanac[to_light_start : to_temperature_start - 2]),
        temperature_maps=parse_maps(maps=raw_almanac[to_temperature_start : to_humidity_start - 2]),
        humidity_maps=parse_maps(maps=raw_almanac[to_humidity_start : to_location_start - 2]),
        location_maps=parse_maps(maps=raw_almanac[to_location_start : len(raw_almanac)]),
    )


def parse_seed_maps(maps: typing.List[str], ranged_seeds: bool) -> typing.List[MapRange]:
    seeds = maps.split(" ")
    if ranged_seeds:
        seed_maps = [f"{start} {length}" for start, length in zip_longest(*(iter(seeds),) * 2)]
    else:
        seed_maps = [f"{seed} 1" for seed in seeds]

    return [build_map_range(raw_map=m) for m in seed_maps]


def parse_maps(maps: typing.List[str]) -> typing.List[MapRange]:
    return [build_map_range(raw_map=m) for m in maps]


def build_map_range(raw_map: str) -> MapRange:
    map_range = [int(n) for n in raw_map.split()]

    if len(map_range) % 2 == 0:
        map_range.insert(0, None)

    return MapRange(*map_range)


def get_mapped_value(map_ranges: typing.List[MapRange], src: int) -> int:
    dest = src
    for map_range in map_ranges:
        if src >= map_range.src_start and src < map_range.src_start + map_range.range:
            dest = src + (map_range.dest_start - map_range.src_start)
    return dest


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=find_closest_location(puzzle_input=puzzle_input),
        second=find_closest_location(puzzle_input=puzzle_input, ranged_seeds=True),
    )
