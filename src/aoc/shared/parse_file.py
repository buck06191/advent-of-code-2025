from pathlib import Path


def load_file(file_path: Path) -> str:
    with open(file_path, "r") as f:
        return f.read().strip()


def load_file_by_lines(file_path: Path) -> list[str]:
    lines = load_file(file_path).splitlines()

    if lines[-1].strip() == "":
        lines.pop()

    return lines
