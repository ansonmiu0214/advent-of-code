# project
from .solutionlib import run_solution


NUMBER_WORDS = 'one two three four five six seven eight nine'.split(' ')


def part1(lines: list[str]) -> int:
    return sum(
        parse_calibration_value_from_line(line, word_aware=False)
        for line in lines
    )


def part2(lines: list[str]) -> int:
    return sum(
        parse_calibration_value_from_line(line, word_aware=True)
        for line in lines
    )


def parse_calibration_value_from_line(
    line: str,
    *,
    word_aware: bool
) -> list[str]:
    digits: list[int] = []

    for idx, char in enumerate(line):
        if word_aware:
            for num, word in enumerate(NUMBER_WORDS, start=1):
                if line[idx:idx + len(word)] == word:
                    digits.append(num)
                    break

        if char.isdigit():
            digits.append(int(char))

    return digits[0] * 10 + digits[-1]


if __name__ == '__main__':
    run_solution(part1, part2)