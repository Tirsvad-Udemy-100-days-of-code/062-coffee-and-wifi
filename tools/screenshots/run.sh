#!/usr/bin/env bash
# Build the screenshot image, run it, and copy the PNGs to docs/screenshots.
# The container runs as an unprivileged user, so the files are copied out with
# `docker cp` instead of a bind mount (a mount is not writable for that user).
set -euo pipefail

IMAGE="coffee-and-wifi-screenshots"
CONTAINER="coffee-and-wifi-screenshots-run"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && { pwd -W 2>/dev/null || pwd; })"
OUT="${ROOT}/docs/screenshots"

mkdir -p "${OUT}"
export MSYS_NO_PATHCONV=1
docker build -f "${ROOT}/tools/screenshots/Dockerfile" -t "${IMAGE}" "${ROOT}"
docker rm -f "${CONTAINER}" >/dev/null 2>&1 || true
trap 'docker rm -f "${CONTAINER}" >/dev/null 2>&1 || true' EXIT
docker run --name "${CONTAINER}" "${IMAGE}"
docker cp "${CONTAINER}:/home/pwuser/out/." "${OUT}"
