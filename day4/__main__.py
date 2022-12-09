from typing import Callable
from utils import load_data

def check_total_overlap(one, two):
    return two[0] <= one[0] <= two[1] and two[0] <= one[1] <= two[1]

def check_partial_overlap(one, two):
    return two[0] <= one[0] <= two[1] or two[0] <= one[1] <= two[1]

def check_overlap(pair: str, compare: Callable[[list, list], bool]) -> bool:
    first, _, second = pair.partition(",")
    one = list(map(int, first.split('-')))
    two = list(map(int, second.split('-')))
    return compare(one, two) or compare(two, one)


if __name__ == "__main__":
    data = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"
    ]
    data = load_data("./day4/data")

    is_completely_overlapping = [check_overlap(line, check_total_overlap) for line in data]
    total_overlapping = sum(1 if overlap is True else 0 for overlap in is_completely_overlapping)

    print(f"Part One, total overlaps: {total_overlapping}")

    is_partially_overlapping = [check_overlap(line, check_partial_overlap) for line in data]
    total_partial_overlap = sum(1 if overlap is True else 0 for overlap in is_partially_overlapping)
    
    print(f"Part Two, total partial overlaps: {total_partial_overlap}")
