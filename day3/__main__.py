from dataclasses import dataclass
from utils import load_data


@dataclass
class Rucksack:
    compartment_one: str
    compartment_two: str

    @property
    def all_contents(self) -> str:
        return self.compartment_one + self.compartment_two


def get_compartments(rucksack_encoded: str) -> Rucksack:
    assert len(rucksack_encoded) % 2 == 0, f"Not even?? {len(rucksack_encoded)}"
    compartment_size = int(len(rucksack_encoded)/2)
    compartment_one = rucksack_encoded[0:compartment_size]
    compartment_two = rucksack_encoded[compartment_size:]
    assert len(compartment_one) == len(compartment_two)

    return Rucksack(compartment_one, compartment_two)


def find_value(r: Rucksack):
    common_item = next(x for x in r.compartment_one if x in r.compartment_two)
    return get_item_value(common_item)


def get_item_value(item: str):
    if item.lower() == item:
        value = ord(item) - ord('a') + 1
    else:
        value = ord(item) - ord('A') + 27
    return value


def find_rucksack_value(rucksack_encoded):
    rucksack = get_compartments(rucksack_encoded)

    return find_value(rucksack)


def get_groups(rucksacks: list[Rucksack], group_size: int = 3):
    assert len(rucksacks) % group_size == 0
    number_of_groups = int(len(rucksacks) / 3)
    return [rucksacks[i*3:(i+1)*3] for i in range(number_of_groups)]

def get_group_badge(group: list[Rucksack]):
    badge = next(i for i in group[0].all_contents if all(i in x.all_contents for x in group[1:]))
    return badge


if __name__ == "__main__":
    data = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

    data = load_data("./day3/data")

    rucksack_values = [find_rucksack_value(x) for x in data]

    print(f"Part One, total priorities: {sum(rucksack_values)}")

    rucksacks = [get_compartments(x) for x in data]
    groups = get_groups(rucksacks)

    group_badges = [get_group_badge(group) for group in groups]
    badge_priority_sum = sum(get_item_value(x) for x in group_badges)
    print(f"Part Two, badge priorities: {badge_priority_sum}")

