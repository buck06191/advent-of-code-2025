from pathlib import Path
from aoc.shared.parse_file import load_file
import itertools


class Part1:
    @staticmethod
    def split_string(string: str, idx: int) -> tuple[str, str]:
        return string[:idx], string[idx:]

    @classmethod
    def validate_range(cls, min: str, max: str) -> list[int]:
        # If length of min AND max are odd AND equal we can skip running
        if len(min) == len(max) and (len(min) % 2) != 0 and (len(max) % 2) != 0:
            return []

        invalid_ids = []
        for id in range(int(min), int(max) + 1):
            id_str = str(id)
            if len(id_str) % 2 != 0:
                continue

            first, second = cls.split_string(id_str, len(id_str) // 2)
            if first == second:
                invalid_ids.append(id)
        return invalid_ids

    @classmethod
    def sum_invalid_ids(cls, input: str):
        invalid_ids = []
        for r in input.split(","):
            try:
                min, max = r.split("-")
                invalid_ids.extend(cls.validate_range(min, max))
            except Exception as err:
                print(f"Failed on {r}")
                raise err

        return sum(invalid_ids)


class Part2:
    @staticmethod
    def compare_string_length(string: str, length: int) -> bool:
        try:
            return len(set(itertools.batched(string, length, strict=True))) == 1
        except ValueError:
            return False

    @classmethod
    def validate_range(cls, min: str, max: str) -> list[int]:
        invalid_ids = []
        for id in range(int(min), int(max) + 1):
            id_str = str(id)
            for i in range(len(id_str) // 2, 0, -1):
                if cls.compare_string_length(id_str, i):
                    invalid_ids.append(id)
                    break

        return invalid_ids

    @classmethod
    def sum_invalid_ids(cls, input: str):
        invalid_ids = []
        for r in input.split(","):
            try:
                min, max = r.split("-")
                invalid_ids.extend(cls.validate_range(min, max))
            except Exception as err:
                print(f"Failed on {r}")
                raise err

        return sum(invalid_ids)


def run_day2():
    print("🎄 Running Day 2\n")
    input_file = Path(__file__).parent.parent.parent / "data" / "day2.txt"
    input = load_file(input_file)
    print("1️⃣ Running Part 1")
    print(Part1.sum_invalid_ids(input))
    print("2️⃣ Running Part 2")
    print(Part2.sum_invalid_ids(input))
