#!/usr/bin/env bash
# Build the screenshot image and run it; the PNGs land in docs/screenshots.
set -euo pipefail

IMAGE="coffee-and-wifi-screenshots"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && { pwd -W 2>/dev/null || pwd; })"
OUT="${ROOT}/docs/screenshots"

mkdir -p "${OUT}"
export MSYS_NO_PATHCONV=1
docker build -f "${ROOT}/tools/screenshots/Dockerfile" -t "${IMAGE}" "${ROOT}"
docker run --rm -v "${OUT}:/out" "${IMAGE}"
