#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

H2_DB_FILE="redd.h2.mv.db"


function check_command() {
    CMD=$1
    if [[ ! -x "$(command -v "$CMD")" ]]; then
    echo "ERROR: $CMD not available" >&2
    exit 1
    fi
}

REQUIRED_COMMANDS=("git" "sbt" "docker")
for cmd in "${REQUIRED_COMMANDS[@]}"; do
  check_command "$cmd"
done


sbt clean assembly

# Download if not exists
if [[ ! -f $H2_DB_FILE ]]; then
    curl -O https://f001.backblazeb2.com/file/modelardata/"$H2_DB_FILE"
fi

DOCKER_TAG=${1:-latest}
GIT_SHA=$(git rev-parse --short HEAD)
GIT_BRANCH=$(git branch --show-current)
GIT_BRANCH=${GIT_BRANCH//\//-} # replace / with -


docker build \
-t "ghcr.io/modelardata/modelardb:$DOCKER_TAG" \
-t "ghcr.io/modelardata/modelardb:$GIT_SHA" \
-t "ghcr.io/modelardata/modelardb:$GIT_BRANCH" \
-f redd.Dockerfile .

