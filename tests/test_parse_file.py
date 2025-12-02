from pathlib import Path
import pytest
from aoc.shared.parse_file import load_file_by_lines


@pytest.fixture
def test_file():
    return Path(__file__).parent / "fixtures" / "test_data.txt"


def test_load_file_by_lines(test_file: Path):
    assert load_file_by_lines(test_file) == ["a", "b", "", "c", "", "d"]
