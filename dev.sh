#!/usr/bin/env bash

function show_usage {
    cat <<EOF
usage: ${0##*/} <language>

arguments:
    language    the programming language
EOF
}

function error {
    NC='\033[0m'
    RED='\033[0;31m'

    echo -e "${RED}ERROR:${NC} $1" >&2
    exit 1
}

set -e

if [[ "$#" != 1 ]]; then
    show_usage >&2
    exit 1
fi

ROOTDIR=$(realpath $(dirname "$0"))
DATADIR="$ROOTDIR/data"

LANG=$1
LANGDIR="$ROOTDIR/langs/$LANG"
[[ -d "$LANGDIR" ]] || error "Language not found: '$LANG'"
[[ -f "$LANGDIR/Dockerfile" ]] || error "'Dockerfile' not found for language: '$LANG'"


IMAGE="advent-of-code:$LANG"

docker build --build-arg MODE=dev -t $IMAGE $LANGDIR
docker run --rm -it -v $LANGDIR:/workarea -v $DATADIR:/data $IMAGE /usr/bin/env bash