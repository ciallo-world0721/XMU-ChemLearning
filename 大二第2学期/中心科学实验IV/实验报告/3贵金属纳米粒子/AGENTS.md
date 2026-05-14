# Repository Instructions

This workspace is for preparing a Chinese chemistry lab report, not for building an application. Treat `commands/` as the source of truth for the report workflow.

## Report workflow
- Read `commands/initial.md` and `commands/file_description.md` before drafting or analyzing data.
- Do not edit `template/`; copy `template/report.tex` to the repository root and edit the copy there.
- Keep the blank header identity fields from the template, but do not add personal identity information in the report text.
- Add the `思考题` section as section 4; move the original `结论` section to section 5.
- Keep data-processing and plotting scripts in the repository root after use; do not delete them.

## Data and references
- `src/实验三 无机贵金属纳米粒子的合成及表征讲义.pdf` is the experiment handout and source for the thought-question topics.
- `legacy/实验报告-无机贵金属纳米粒子的合成及表征.pdf` is a reference for the analysis flow, but answers and prose should be rewritten.
- `src/img/20260429-SEM/` contains SEM images; filenames encode sample names.
- `src/Raman_100ms_531.81nm/` and `src/Raman_2026-05-08/` contain Raman/SERS text data; data rows start after the instrument header and are whitespace/tab separated.

## Figures and analysis
- Use Python for data processing and plotting; use `uv` only if the global environment lacks needed packages.
- Use matplotlib style `bmh` for plots unless there is a strong reason not to.
- Save newly generated figures under `src/img/`.
- `template/report.tex` references `images/...` sample assets; if working from a root copy, adjust/copy image paths deliberately rather than modifying `template/`.
- The final report should discuss results, not expose file paths or detailed data-processing steps.

## Build and verification
- Compile the editable root report with `xelatex report.tex`.
- Use the PDF skill or browser/PDF viewer to inspect generated PDFs.
- There are no root build/test/lint scripts or CI configs; verification is mainly successful XeLaTeX compilation plus visual PDF review against `template/report.pdf` and the legacy report.

## Path cautions
- Many filenames contain spaces and Chinese characters; quote paths in shell commands.
- `.opencode/` contains local OpenCode runtime/skills, not project source for the lab report.
