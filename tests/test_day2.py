import pytest
from aoc.day2 import Part1, Part2


@pytest.fixture(scope="package")
def test_input() -> str:
    return "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


class TestPartOne:
    @pytest.mark.parametrize(
        "min, max, expected",
        [
            ("11", "22", [11, 22]),
            ("95", "115", [99]),
            ("998", "1012", [1010]),
            ("1188511880", "1188511890", [1188511885]),
            ("222220", "222224", [222222]),
            ("1698522", "1698528", []),
            ("446443", "446449", [446446]),
            ("38593856", "38593862", [38593859]),
        ],
    )
    def test_validate_range(self, min: str, max: str, expected: list[int]):
        assert Part1.validate_range(min, max) == expected

    def test_sum_invalid_ids(self, test_input: str):
        assert Part1.sum_invalid_ids(test_input) == 1227775554


class TestPartTwo:
    @pytest.mark.parametrize(
        "min, max, expected",
        [
            ("11", "22", [11, 22]),
            ("95", "115", [99, 111]),
            ("998", "1012", [999, 1010]),
            ("1188511880", "1188511890", [1188511885]),
            ("222220", "222224", [222222]),
            ("1698522", "1698528", []),
            ("446443", "446449", [446446]),
            ("38593856", "38593862", [38593859]),
            ("565653", "565659", [565656]),
            ("824824821", "824824827", [824824824]),
            ("2121212118", "2121212124", [2121212121]),
        ],
    )
    def test_validate_range(self, min: str, max: str, expected: list[int]):
        assert Part2.validate_range(min, max) == expected

    def test_sum_invalid_ids(self, test_input: str):
        assert Part2.sum_invalid_ids(test_input) == 4174379265
