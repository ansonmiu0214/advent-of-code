#!/usr/bin/env bash

function show_usage {
    cat <<EOF
usage: ${0##*/} <language> <problem> <input_type>

arguments:
    language    the programming language
    problem     the day of the problem
    input_type  the type of input file
EOF
}

function error {
    NC='\033[0m'
    RED='\033[0;31m'

    echo -e "${RED}ERROR:${NC} $1" >&2
    exit 1
}

set -e

if [[ "$#" != 3 ]]; then
    show_usage >&2
    exit 1
fi

ROOTDIR=$(realpath $(dirname "$0"))
DATADIR="$ROOTDIR/data"

LANG=$1
LANGDIR="$ROOTDIR/langs/$LANG"
[[ -d "$LANGDIR" ]] || error "Language not found: '$LANG'"
[[ -f "$LANGDIR/Dockerfile" ]] || error "'Dockerfile' not found for language: '$LANG'"
[[ -f "$LANGDIR/run.sh" ]] || error "'run.sh' driver not found for language: '$LANG'"

PROBLEM=$2
[[ -d "$DATA_DIR/$PROBLEM" ]] || error "Problem not found: '$PROBLEM'"

INPUT_TYPE=$3
[[ -f "$DATA_DIR/${PROBLEM}/${INPUT_TYPE}.in" ]] || error "Input data for $PROBLEM not found: '$INPUT_TYPE'"

shift

IMAGE="advent-of-code:$LANG"

docker build -t $IMAGE $LANGDIR
docker run --rm -v $LANGDIR:/workarea -v $DATADIR:/data $IMAGE ./run.sh "$@" /data/$PROBLEM