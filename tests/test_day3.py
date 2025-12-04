import pytest

from aoc.day3 import Part1


@pytest.fixture
def battery_racks() -> list[str]:
    return ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]


@pytest.mark.parametrize(
    ["batteries", "expected"],
    [
        ([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1], 98),
        ([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], 89),
        ([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8], 78),
        ([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1], 92),
    ],
)
def test_highest_pair(batteries, expected):
    assert Part1.highest_pairing(batteries) == expected


def test_total_joltage(battery_racks):
    assert Part1.total_joltage(battery_racks) == 357
