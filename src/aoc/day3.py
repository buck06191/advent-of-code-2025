from pathlib import Path

from aoc.shared.parse_file import load_file_by_lines


class Part1:
    @classmethod
    def total_joltage(cls, battery_racks: list[str]) -> int:
        return sum(
            [cls.highest_pairing([int(b) for b in rack]) for rack in battery_racks]
        )

    @staticmethod
    def highest_pairing(batteries: list[int]) -> int:
        highest = 0
        second_highest = 0
        for idx, battery in enumerate(batteries):
            if battery > highest and idx != len(batteries) - 1:
                highest = battery
                second_highest = 0
                continue
            if battery > second_highest:
                second_highest = battery
                continue

        return int(f"{highest}{second_highest}")


class Part2:
    pass


def run_day3():
    print("🎄 Running Day 3\n")
    input_file = Path(__file__).parent.parent.parent / "data" / "day3.txt"
    input = load_file_by_lines(input_file)
    print("1️⃣ Running Part 1")
    print(Part1.total_joltage(battery_racks=input))
    print("2️⃣ Running Part 2")
