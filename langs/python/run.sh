#!/usr/bin/env bash

function show_usage {
    cat <<EOF
usage: ${0##*/} <problem> <input_type> <data_dir> [--part-1] [--part-2]

arguments:
    problem     the day of the problem
    input_type  the type of input file
    data_dir    the root directory containing the problem's data

optional arguments:
    --part-1    only run part 1 solution
    --part-2    only run part 2 solution
EOF
}

set -e

if [[ "$#" < 3 ]]; then
    show_usage >&2
    exit 1
fi

PROBLEM=$1
INPUT_TYPE=$2
DATA_DIR=$3

shift 3

python3 -m aoc.$PROBLEM $INPUT_TYPE $DATA_DIR "$@"