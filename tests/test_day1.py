import operator
import pytest
from aoc.day1 import turn_dial, run_instruction_part_2, Instruction


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


def test_turn_dial__part_1(mock_instructions):
    assert turn_dial(50, mock_instructions, verbose=True) == 3


def test_turn_dial__part_2(mock_instructions):
    assert turn_dial(50, mock_instructions, verbose=True, part=2) == 6


@pytest.mark.parametrize(
    argnames=["start", "instruction", "expected"],
    argvalues=[
        (50, Instruction(name="L68", amount=68, operation=operator.sub), (82, 1)),
        (82, Instruction(name="L30", amount=30, operation=operator.sub), (52, 0)),
        (52, Instruction(name="R48", amount=48, operation=operator.add), (0, 1)),
        (0, Instruction(name="L5", amount=5, operation=operator.sub), (95, 0)),
        (95, Instruction(name="R60", amount=60, operation=operator.add), (55, 1)),
        (55, Instruction(name="L55", amount=55, operation=operator.sub), (0, 1)),
        (0, Instruction(name="L1", amount=1, operation=operator.sub), (99, 0)),
        (99, Instruction(name="L99", amount=99, operation=operator.sub), (0, 1)),
        (0, Instruction(name="R14", amount=14, operation=operator.add), (14, 0)),
        (14, Instruction(name="L82", amount=82, operation=operator.sub), (32, 1)),
        (50, Instruction(name="R1000", amount=1000, operation=operator.add), (50, 10)),
        (50, Instruction(name="L1000", amount=1000, operation=operator.sub), (50, 10)),
        (0, Instruction(name="L300", amount=300, operation=operator.sub), (0, 3)),
        (0, Instruction(name="R300", amount=300, operation=operator.add), (0, 3)),
        (10, Instruction(name="L110", amount=110, operation=operator.sub), (0, 2)),
        (10, Instruction(name="L111", amount=111, operation=operator.sub), (99, 2)),
    ],
    ids=[
        "50-L68",
        "82-L30",
        "52-R48",
        "0-L5",
        "95-R60",
        "55-L55",
        "0-L1",
        "99-L99",
        "0-R14",
        "14-L82",
        "50-R1000",
        "50-L1000",
        "0-L300",
        "0-R300",
        "10-L110",
        "10-L111",
    ],
)
def test_run_instruction_part_2(start, instruction, expected):
    assert run_instruction_part_2(start, instruction) == expected
