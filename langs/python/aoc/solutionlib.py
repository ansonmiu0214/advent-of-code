import argparse
import logging
import sys
from pathlib import Path
from typing import Callable, NoReturn


Solution = Callable[[list[str]], int]


def run_solution(part1: Solution, part2: Solution) -> NoReturn:
    sys.exit(_main(part1, part2))


def _main(part1_fn: Solution, part2_fn: Solution) -> int:
    prog = argparse.ArgumentParser()
    prog.add_argument('input_type')
    prog.add_argument('data_dir', type=Path)
    prog.add_argument('--part-1', action='store_true')
    prog.add_argument('--part-2', action='store_true')

    args = prog.parse_args()
    input_type: str = args.input_type
    data_dir: Path = args.data_dir
    part_1: bool = args.part_1
    part_2: bool = args.part_2

    should_run_part_1 = part_2 is False or part_1 is True
    should_run_part_2 = part_1 is False or part_2 is True

    input_file = (data_dir / input_type).with_suffix('.in')
    if not input_file.is_file():
        logging.error('Input file not found: %s', input_file)
        return 1

    lines = input_file.read_text(encoding='utf-8').splitlines()

    ec = 0
    if should_run_part_1:
        try:
            ans_1 = part1_fn(lines)
            print(f'Part 1: {ans_1}')
        except Exception as exc:
            logging.error('Caught exception when computing solution for part 1', exc_info=exc)
            ec += 1

    if should_run_part_2:
        try:
            ans_2 = part2_fn(lines)
            print(f'Part 2: {ans_2}')
        except Exception as exc:
            logging.error('Caught exception when computing solution for part 2', exc_info=exc)
            ec += 1
    
    return ec