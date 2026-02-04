# AI-Assisted Mathematics Archive

This repository is a curated collection of mathematical problems and
their solutions, written as self-contained PDF documents.

Some solutions were developed with the assistance of AI tools.
All final results are reviewed, edited, and verified by a human.

The goal of this repository is long-term reference and pedagogy:
solutions are written to be readable, stable, and inheritable.

---

## Structure

- `tex/`  
  LaTeX source files for each problem.  
  Each file contains the full problem statement, solution, and remarks.

- `solutions/`  
  Compiled PDF files, one per problem.  
  These PDFs are the canonical artifacts meant for reading and sharing.

- `index.md`  
  An auto-generated index listing all problems and linking to their PDFs.

- `scripts/`  
  Utility scripts for building PDFs and generating the index.

---

## Workflow

For each problem:

1. Write a LaTeX file `PXXX.tex` in `tex/`
2. Compile all PDFs and update the index using:
   ```bash
   ./scripts/build_all.sh
