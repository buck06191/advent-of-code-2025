from pathlib import Path


def load_file(file_path: Path) -> list[str]:
    with open(file_path, "r") as f:
        lines = f.read().splitlines()

    if lines[-1].strip() == "":
        lines.pop()

    return lines
