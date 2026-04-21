# AGENTS.md

## Purpose
- This repository is primarily a document-production project for a chemistry lab report, not a conventional application codebase.
- The main deliverable is a polished XeLaTeX report built from data and reference materials in `src/`.
- Agents should optimize for accurate scientific writing, reproducible data processing, and minimal disruption to the provided template.

## Repository Layout
- `commands/initial.md`: baseline project instructions.
- `commands/project.md`: extra project-specific constraints.
- `template/report.tex`: the authoritative LaTeX template; preserve its structure and style.
- `template/images/`: template assets used by the report header and examples.
- `src/`: raw experimental inputs, references, and supporting materials.
- `.vscode/settings.json`: Python environment preference is the system interpreter.
- `.opencode/`: local tool metadata; not part of the report deliverable.

## External Instruction Files
- Read `commands/initial.md` before making substantial changes.
- Read `commands/project.md` before analyzing source data or drafting the report.
- No `.cursorrules` file is present.
- No `.cursor/rules/` directory is present.
- No `.github/copilot-instructions.md` file is present.

## High-Level Working Rules
- Do not modify files under `template/` unless the user explicitly asks for template changes.
- Keep report source files and any helper scripts at the repository root.
- Put generated figures in `src/img/`.
- Keep raw data in `src/` unchanged.
- Focus analysis on the files explicitly called out in `commands/project.md`.
- Use the reference `.docx` and PDFs for understanding content and structure, not for blind copying.

## Expected Deliverables
- A root-level `report.tex` derived from `template/report.tex` when authoring the final report.
- Optional root-level Python scripts for data cleaning, fitting, and plotting.
- Generated plot files under `src/img/`.
- Optionally, a built PDF such as `report.pdf` in the repository root if the user asks for compiled output.

## Build Commands
- Primary build command for the final report:
  - `xelatex -interaction=nonstopmode -halt-on-error report.tex`
- Run XeLaTeX twice if cross-references, figure numbering, or table numbering need to settle:
  - `xelatex -interaction=nonstopmode -halt-on-error report.tex`
  - `xelatex -interaction=nonstopmode -halt-on-error report.tex`
- If you need isolated Python dependencies, create an environment with `uv` first, per `commands/initial.md`.
- There is no Makefile, task runner, or package manager script defined at the repository root.

## Lint / Format Commands
- No dedicated linter or formatter configuration is present in the repository root.
- For LaTeX validation, use the build command above and treat warnings/errors as the main quality gate.
- For Python syntax validation of a single helper script:
  - `python -m py_compile path/to/script.py`
- For all helper scripts at once, if such scripts exist:
  - `python -m compileall .`
- If you introduce a formatter or linter, do so only when requested or when clearly justified by the scope of work.

## Test Commands
- There is no existing automated test suite in this repository.
- There is no `pytest.ini`, `tox.ini`, `pyproject.toml`, `package.json`, or root test harness.
- Validation is primarily done by:
  - running data-processing scripts successfully,
  - checking generated figures manually,
  - compiling `report.tex` with XeLaTeX,
  - verifying that referenced assets exist.

## Single-Test Guidance
- No single-test command exists yet because there is no test framework configured.
- If you add `pytest` tests for helper scripts, prefer this single-test pattern:
  - `pytest tests/test_name.py::test_case_name`
- If you add `unittest` tests, prefer this single-test pattern:
  - `python -m unittest tests.test_module.TestClass.test_method`
- If the repo remains testless, treat “single test” as running one script or one compile target only.

## Common Validation Workflow
- Confirm that raw input files in `src/` are present before writing analysis code.
- Run the relevant Python script directly with `python script_name.py`.
- Verify output figures land in `src/img/` with stable filenames.
- Compile the report with XeLaTeX.
- Re-run the build after edits that affect references, tables, or figure numbering.

## Observed Style Baseline
- The strongest existing style signal is the LaTeX template in `template/report.tex`.
- The project favors formal academic Chinese prose with English technical terms where appropriate.
- The template uses explicit formatting rather than terse macros; preserve that clarity.
- The project instructions prefer reproducible scripts over manual spreadsheet-only processing.

## LaTeX Style Guidelines
- Preserve the section structure and typography conventions from `template/report.tex`.
- Keep the report professional, formal, and readable for an instructor audience.
- Do not include student identity details unless the user explicitly requests them.
- Follow the instruction from `commands/project.md` to insert the prelab “思考题” as Section 4.
- Shift the original conclusion to Section 5 when building the final report.
- Mention every figure and table in the body text before or where it appears.
- Use consistent units, symbols, and significant figures.
- Keep captions specific and self-explanatory.
- Prefer concise paragraphs that interpret data rather than restating raw values.
- Do not dump raw spreadsheet output into the report.

## Figure and Table Conventions
- Use the `bmh` plotting style for generated charts, per `commands/initial.md`.
- Re-plot instrument output rather than embedding raw instrument screenshots.
- Keep chart styling consistent across all generated figures.
- Label axes with quantity names and units.
- Use stable filenames for generated figures so LaTeX references do not churn.
- Prefer vector or high-resolution outputs when practical.
- Match the report narrative to the actual plotted data.

## Python Code Style Guidelines
- There is no repository-wide formatter config, so keep Python simple and conventional.
- Target readable scripts over framework-heavy abstractions.
- Prefer small, composable functions over long notebook-style scripts.
- Keep one clear responsibility per script: loading, cleaning, plotting, or tabulating.
- Add type hints for public functions and non-trivial helpers.
- Use docstrings sparingly; add them when function behavior is not obvious.
- Avoid clever one-liners when straightforward code is clearer.

## Imports
- Group imports in this order: standard library, third-party packages, local modules.
- Separate import groups with a single blank line.
- Prefer explicit imports over wildcard imports.
- Use conventional aliases such as `import pandas as pd`, `import numpy as np`, and `import matplotlib.pyplot as plt`.
- Remove unused imports before finishing.

## Formatting
- Use 4-space indentation in Python.
- Keep lines reasonably short; aim for roughly 88-100 characters when possible.
- Use trailing commas in multi-line literals where they improve diffs.
- Prefer f-strings over `%` formatting or `str.format()` for new code.
- Keep whitespace consistent and avoid alignment-by-spacing.

## Naming
- Use `snake_case` for Python functions, variables, and filenames.
- Use `PascalCase` for classes.
- Use `UPPER_SNAKE_CASE` for module-level constants.
- Name plotting outputs descriptively, for example `uv_vis_absorbance.png` or `temperature_response_curve.png`.
- Prefer names tied to the experiment domain over vague names like `data2` or `result_final`.

## Types and Data Handling
- Use `pathlib.Path` for filesystem paths in new Python code.
- Validate assumptions about spreadsheet columns before processing.
- Convert units explicitly and in one place.
- Keep floating-point rounding for presentation separate from analysis calculations.
- Store intermediate data in tidy tabular form when possible.

## Error Handling
- Fail early on missing files, missing columns, or malformed inputs.
- Raise clear exceptions with actionable messages.
- Do not silently swallow parsing or plotting errors.
- When a recoverable issue occurs, log or print a concise explanation.
- Guard entry points with `if __name__ == "__main__":` in standalone scripts.

## Scientific Writing Guidelines
- Explain what each analysis result means physically or chemically.
- Compare trends, not just absolute values.
- Use literature or provided references to support interpretation where relevant.
- Distinguish observation, inference, and speculation.
- Keep claims proportional to the evidence in the data.

## Files to Avoid Touching Casually
- `template/report.tex`
- files under `template/images/`
- raw spreadsheets under `src/`
- reference documents in `src/` unless the task is explicitly about extracting from them

## Practical Agent Defaults
- If a root `report.tex` does not exist, create it by copying and adapting the template rather than editing `template/report.tex`.
- If `src/img/` does not exist, create it before writing figures there.
- Prefer Python scripts over manual spreadsheet edits for reproducibility.
- Keep generated artifacts named deterministically.
- Summarize any assumptions you make about data interpretation.

## Completion Checklist
- Commands from `commands/initial.md` and `commands/project.md` are respected.
- New scripts live at the repository root.
- New figures live in `src/img/`.
- Raw data remains unchanged.
- The report compiles with `xelatex`.
- The report structure reflects the required Section 4 / Section 5 adjustment.
