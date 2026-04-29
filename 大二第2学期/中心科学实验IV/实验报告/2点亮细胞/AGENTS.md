# AGENTS.md

## Repository purpose
- This is a Chinese LaTeX experiment-report project for “绿色荧光蛋白的克隆表达和表征”, not an application/codebase repo.
- Treat `commands/initial.md` and `commands/project.md` as the operative task instructions; they override stale generated notes.

## Source material to read first
- `template/report.tex`: required report template and formatting source of truth; compile engine is XeLaTeX because it uses `fontspec`/`xeCJK`.
- `src/实验二 点亮细胞-绿色荧光蛋白的克隆表达和表征.pdf`: course handout for this experiment.
- `legacy/*实验报告*.pdf`: reference only for analysis approach and 思考题 title/count structure; do not copy answers.
- `src/img/`: experiment photos; `src/img/report/` contains LaTeX-safe ASCII figure copies when present.

## File placement rules
- Do not edit anything under `template/`; copy `template/report.tex` to root `report.tex` and edit the root copy.
- Put new analysis/plotting scripts in the repo root and keep them; do not delete scripts after generating figures.
- Put report-ready images under `src/img/` (prefer `src/img/report/` with ASCII filenames for LaTeX paths).
- The root `images/` directory is for the template header assets referenced by `report.tex`.

## Report content constraints
- Final report prose must not show student identity labels/fields such as `姓名`, `学号`, `专业`, or `实验台号`.
- Do not mention workspace paths, source filenames, extraction artifacts, or “generated from files” provenance in teacher-facing prose.
- `commands/project.md` requires a `思考题` section before conclusion: use the legacy/report structure, write fresh answers, then make the original conclusion the next section.
- Expected 思考题 counts from the existing plan/evidence are 7 + 5 + 8 + 2 questions across: 质粒载体DNA的制备与检测, PCR技术扩增目的基因, 外源基因的转化与表达, 综合思考题.
- Do not invent quantitative results, lane identities, yields, A260/A280 values, fluorescence intensity, or colony counts unless directly supported by source material or visible images.

## Commands and verification
- Compile from repo root with XeLaTeX, usually twice for references: `xelatex -interaction=nonstopmode -halt-on-error report.tex`.
- Use Python for data processing/plotting; if plotting is needed, use matplotlib style `bmh` unless there is a concrete reason not to.
- After compile, check that `report.pdf` exists, `report.log` has no LaTeX errors/missing-file errors, every `\includegraphics` path resolves, and extracted PDF text contains 引言, 实验部分, 结果与讨论, 思考题, 结论.
- Use the `pdf` skill or browser/PDF tooling to inspect PDFs when content or rendering needs verification.

## Current-state gotchas
- There is no root `report.tex`/`report.pdf` in the live filesystem as of this AGENTS update; recreate them from `template/report.tex` if continuing the report.
- `.sisyphus/BUILD_SUMMARY.md` and evidence files claim prior completion, but they are stale unless live root artifacts exist; verify files directly before trusting them.
- `.opencode/` contains tool/skill dependencies and is not this project’s package manifest.
