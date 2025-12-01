import pytest
from aoc.day1 import turn_dial


@pytest.fixture
def mock_instructions() -> list[str]:
    return [
        "L68",
        "L30",
        "R48",
        "L5 ",
        "R60",
        "L55",
        "L1 ",
        "L99",
        "R14",
        "L82",
    ]


def test_turn_dial(mock_instructions):
    assert turn_dial(50, mock_instructions, verbose=True) == 3
