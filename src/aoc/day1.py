from typing import Callable
from dataclasses import dataclass
import operator

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


def run_instruction(start_position: int, instruction: Instruction) -> int:
    return instruction.operation(start_position, instruction.amount) % DIAL_SIZE


def turn_dial(start_position: int, instructions: list[str], verbose=False) -> int:
    current = start_position
    zero_count = 0
    print(f"Starting at {current}")
    for i in instructions:
        instruction = parse_instruction(i)
        next = run_instruction(current, instruction)
        if verbose:
            print(f"The dial is rotated {instruction.name} to point at {next}")
        if next == 0:
            zero_count += 1
        current = next

    return zero_count


def run_day1():
    print("🎄 Running Day 1")
