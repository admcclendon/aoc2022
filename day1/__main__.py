from dataclasses import dataclass
from utils import load_data


@dataclass
class Elf:
    index: int
    calories: int = 0


if __name__ == "__main__":
    # load data.
    data = load_data("./day1/data")
    
    elfindex = 0
    elves: list[Elf] = []
    current_elf = Elf(elfindex)
    for line in data:
        if line.strip() == "":
            elves.append(current_elf)
            elfindex = elfindex + 1
            current_elf = Elf(elfindex)
        else:
            calories = int(line)
            current_elf.calories += calories
    elves.append(current_elf)

    elves.sort(key=lambda e: e.calories, reverse=True)
    
    print(f"Part one, highest total: {elves[0].calories}")
    print(f"Part Two, top three total: {sum(map(lambda e: e.calories, elves[0:3]))}")
