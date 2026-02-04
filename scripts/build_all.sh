#!/bin/bash

set -e  # stop on error

echo "Building all PDFs..."
latexmk -pdf -output-directory=solutions tex/*.tex

echo "Updating index..."
python scripts/build_index.py

echo "Done."
