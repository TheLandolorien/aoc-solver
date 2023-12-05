import sys
import typing

from collections import namedtuple

from aoc_solver.object_types import Solution

MapRange = namedtuple("MapRange", ["dest_start", "src_start", "range"])

# --- Day 5: If You Give A Seed A Fertilizer ---
# Source: https://adventofcode.com/2023/day/5


def find_closest_location(almanac: typing.List[str]) -> int:
    to_soil_start = almanac.index("seed-to-soil map:") + 1
    to_fertilizer_start = almanac.index("soil-to-fertilizer map:") + 1
    to_water_start = almanac.index("fertilizer-to-water map:") + 1
    to_light_start = almanac.index("water-to-light map:") + 1
    to_temperature_start = almanac.index("light-to-temperature map:") + 1
    to_humidity_start = almanac.index("temperature-to-humidity map:") + 1
    to_location_start = almanac.index("humidity-to-location map:") + 1

    seeds = almanac[0].split(": ")[1].split(" ")
    closest_location = sys.maxsize
    for seed in seeds:
        seed = int(seed)

        soil = get_mapped_value(maps=almanac[to_soil_start : to_fertilizer_start - 2], src=seed)
        fertilizer = get_mapped_value(
            maps=almanac[to_fertilizer_start : to_water_start - 2], src=soil
        )
        water = get_mapped_value(maps=almanac[to_water_start : to_light_start - 2], src=fertilizer)
        light = get_mapped_value(maps=almanac[to_light_start : to_temperature_start - 2], src=water)
        temperature = get_mapped_value(
            maps=almanac[to_temperature_start : to_humidity_start - 2], src=light
        )
        humidity = get_mapped_value(
            maps=almanac[to_humidity_start : to_location_start - 2], src=temperature
        )
        location = get_mapped_value(maps=almanac[to_location_start : len(almanac)], src=humidity)

        if location < closest_location:
            closest_location = location

    return closest_location


def get_mapped_value(maps: typing.List[str], src: int) -> int:
    dest = src
    for raw_map in maps:
        parsed_map = MapRange(*map(int, raw_map.split()))
        if src >= parsed_map.src_start and src < parsed_map.src_start + parsed_map.range:
            dest = src + (parsed_map.dest_start - parsed_map.src_start)
    return dest


def solve(puzzle_input: typing.List[str]) -> Solution:
    return Solution(
        first=find_closest_location(almanac=puzzle_input),
        second=None,
    )
