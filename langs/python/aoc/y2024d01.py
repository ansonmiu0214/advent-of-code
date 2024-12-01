# built-ins
import re
from collections import Counter

# project
from .solutionlib import run_solution


def part1(lines: list[str]) -> int:
    left, right = parse_location_id_lists(lines)

    left = sorted(left)
    right = sorted(right)

    return sum(
        abs(left_id - right_id)
        for left_id, right_id in zip(left, right)
    )


def part2(lines: list[str]) -> int:
    left, right = parse_location_id_lists(lines)

    left_freq_table = Counter(left)
    right_freq_table = Counter(right)

    return sum(
        num * num_left_freq * right_freq_table[num]
        for num, num_left_freq in left_freq_table.items()
    )


def parse_location_id_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []

    tokenizer = re.compile(r'\s+')
    for line in lines:
        left_id, right_id = tokenizer.split(line)
        left.append(int(left_id))
        right.append(int(right_id))
    
    return left, right


if __name__ == '__main__':
    run_solution(part1, part2)