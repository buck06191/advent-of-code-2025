from pathlib import Path
from typing import Callable
from dataclasses import dataclass
import operator

from aoc.shared.parse_file import load_file

DIAL_SIZE = 100


@dataclass
class Instruction:
    name: str
    operation: Callable[[int, int], int]
    amount: int


def parse_instruction(instruction: str) -> Instruction:
    direction, amount = instruction[0], int(instruction[1:])

    if direction == "L":
        return Instruction(name=instruction, operation=operator.sub, amount=amount)
    elif direction == "R":
        return Instruction(name=instruction, operation=operator.add, amount=amount)
    else:
        raise ValueError()


def run_instruction_part_1(start_position: int, instruction: Instruction) -> int:
    return instruction.operation(start_position, instruction.amount) % DIAL_SIZE


def run_instruction_part_2(
    start_position: int, instruction: Instruction
) -> tuple[int, int]:
    nonmod_int = instruction.operation(start_position, instruction.amount)
    new_start = nonmod_int % DIAL_SIZE

    if start_position == 0:
        return new_start, instruction.amount // DIAL_SIZE
    else:
        return new_start, abs(nonmod_int // DIAL_SIZE) + (
            # Add one if we finish on zero and we were turning left
            # We're being cheeky here and using a boolean as 1
            new_start == 0 and instruction.name.startswith("L")
        )


def turn_dial(
    start_position: int, instructions: list[str], verbose=False, part=1
) -> int:
    current = start_position
    zero_total = 0

    if verbose:
        print(f"Starting at {current}")
    for i in instructions:
        instruction = parse_instruction(i)
        if part == 2:
            next, zero_count = run_instruction_part_2(current, instruction)
            zero_total += zero_count
        else:
            next = run_instruction_part_1(current, instruction)
            if next == 0:
                zero_total += 1
        if verbose:
            print(f"The dial is rotated {instruction.name} to point at {next}")
        current = next

    print(f"🔐 The password is {zero_total}\n")
    return zero_total


def run_day1():
    print("🎄 Running Day 1\n")
    input_file = Path(__file__).parent.parent.parent / "data" / "day1.txt"
    instructions = load_file(input_file)
    print("1️⃣ Running Part 1")
    turn_dial(50, instructions, part=1)
    print("2️⃣ Running Part 2")
    turn_dial(50, instructions, part=2)
