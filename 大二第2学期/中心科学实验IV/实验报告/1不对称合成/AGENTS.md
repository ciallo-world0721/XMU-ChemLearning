# AGENTS.md

## What this repo is
- This is a **chemistry experiment report workspace**, not a normal software package. There is no project-level `package.json`, `pyproject.toml`, CI workflow, task runner, or test suite to drive your work.
- Start from these files, in this order: `commands/initial.md` -> `commands/project.md` -> `template/report.tex` -> representative files under `src/uv/` and `src/cd/`.
- Treat `.opencode/` as tool state, not project source.

## Sources of truth
- `commands/initial.md` is the main operating contract.
- `commands/project.md` adds scope limits and report-structure overrides for this specific experiment.
- If prose conflicts with code/template, trust `template/report.tex` and the actual data files.

## Required workflow
- Follow `template/report.tex` strictly for report structure and formatting.
- Do **not** edit files under `template/`. Copy `template/report.tex` to the repo root as the working report source, then edit the copy there.
- Keep any new analysis/plotting scripts in the repo root.
- Save generated figures under `src/img/`.
- Use `python` for data processing and plotting. Use `uv` only if the global Python environment is missing required packages.
- Compile with `xelatex`, not `pdflatex`. The template uses `fontspec` and `xeCJK` and declares `% !TEX program = xelatex`.
- Review the rendered PDF with the PDF skill or browser tooling before considering the work done.

## Report-specific constraints
- The final report should read like a teacher-facing lab report, not a work log. Do not include student name/ID info, local filenames, or step-by-step data-processing details.
- `commands/project.md` changes the template structure: insert the prelab `思考题` content as **section 4**, and move the original conclusion to **section 5**.
- The template requires figures/tables to be discussed in the text and discourages instrument screenshots; redraw spectra as publication-style figures.

## Data boundaries and formats
- Normally, only inspect these inputs:
  - `src/uv/` for UV-Vis data
  - `src/cd/` for circular dichroism data
  - `legacy/*实验报告*` and `legacy/数据处理/` as optional references
- Do not wander into unrelated files unless the command docs force it.
- `src/uv/*.csv` files are instrument exports with a non-UTF header block; the numeric table starts only after the metadata section, at the row headed `波长(nm),吸光值`.
- `src/cd/1/*.txt` and `src/cd/2/*.txt` are JASCO exports with metadata first and numeric data after the `XYDATA` marker.
- Do not assume the two CD folders are directly comparable without checking units/resolution:
  - `src/cd/1/` uses dense sampling (`DELTAX -0.1`) and `YUNITS CD[mdeg]`
  - `src/cd/2/` uses coarse sampling (`DELTAX -2`) and `YUNITS Mol. CD`
- `.jws` files exist beside the CD `.txt` files, but the `.txt` exports are the easier authoritative inputs for scripted analysis.

## Plotting and LaTeX gotchas
- Use the `bmh` plotting style unless there is a compelling reason not to; this is explicitly required by `commands/initial.md`.
- `template/report.tex` references assets as `images/...` relative to the `.tex` file. If you copy the template to the repo root, account for those image paths in the working copy or preserve a matching `images/` layout beside it.
- The template already includes `natbib` plus a manual `thebibliography` block. Do not switch to `biblatex`/`biber` unless you intentionally refactor the report source.

## Legacy references
- `legacy/数据处理/plot_spectra.py` is a **reference implementation**, not a drop-in script for the current repo.
- It assumes a sibling `input/` directory, writes to `output/`, and looks for folder names like `UV`, `CD`, `第一周`, and `第二周`; the current repo actually stores data under `src/uv/`, `src/cd/1/`, and `src/cd/2/`.
- Reuse its parsing/plotting ideas carefully, but do not run it unchanged and assume the paths match.
- If you adapt logic from it, note that it imports `numpy`, `matplotlib`, and `openpyxl`.
