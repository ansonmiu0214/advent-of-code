# project
from .solutionlib import run_solution


Report = list[int]


def part1(lines: list[str]) -> int:
    return sum(map(report_is_safe, map(parse_report, lines)))


def part2(lines: list[str]) -> int:
    return NotImplemented


def parse_report(line: str) -> Report:
    return list(map(int, line.split(' ')))


def report_is_safe(report: Report) -> bool:
    lvl_diffs = [
        curr_lvl - next_lvl
        for curr_lvl, next_lvl in zip(report, report[1:])
    ]
    if any(diff == 0 for diff in lvl_diffs):
        return False
    
    if not all(1 <= abs(diff) <= 3 for diff in lvl_diffs):
        return False
    
    if all(diff < 0 for diff in lvl_diffs):
        return True
    
    if all(diff > 0 for diff in lvl_diffs):
        return True
    
    return False


if __name__ == '__main__':
    run_solution(part1, part2)