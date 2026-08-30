#!/usr/bin/env bash
# Build the manuscript. Regenerates figure PDFs from SVG, then compiles with latexmk.
set -e
cd "$(dirname "$0")"
if command -v rsvg-convert >/dev/null; then
  for f in figures/*.svg; do rsvg-convert -f pdf -o "${f%.svg}.pdf" "$f"; done
else
  echo "rsvg-convert not found — figure PDFs not regenerated (using existing)."
fi
latexmk -pdf -interaction=nonstopmode paper.tex
