# AGENTS.md

Guidance for agentic coding agents working in this repository.

## Project Snapshot

- This repo is a XeLaTeX-based chemistry lab report workspace for Xiamen University's Central Science Experiment IV course.
- The main editable sources are `template/report.tex` and `src/预习.tex`.
- Most other files under `src/` are experimental data, reference docs, or generated PDFs.
- There is no package manager, CI pipeline, or conventional software test suite in the repo root.

## Repository Layout

```text
/
├── AGENTS.md
├── src/
│   ├── 预习.tex
│   ├── 预习.pdf
│   ├── 催化剂性能评价_data/
│   └── 第6组TPR（程序升温还原）_data/
└── template/
    ├── report.tex
    ├── report.pdf
    └── images/
```

## Rule Files

- Checked `.cursor/rules/`: none found.
- Checked `.cursorrules`: none found.
- Checked `.github/copilot-instructions.md`: none found.
- This `AGENTS.md` is therefore the primary repo-level instruction source.

## Tooling Summary

- Required engine: `xelatex`.
- Recommended automated flags: `-interaction=nonstopmode -halt-on-error`.
- Build each `.tex` file from its own directory when it uses relative assets.
- `template/report.tex` depends on `template/images/...` paths.
- `src/预习.tex` depends on the local font `Noto Serif CJK SC`.

## Build Commands

### Main build targets

Build the template once from `template/`:

```bash
xelatex -interaction=nonstopmode -halt-on-error "report.tex"
```

Build the preview document once from `src/`:

```bash
xelatex -interaction=nonstopmode -halt-on-error "预习.tex"
```

### Stable two-pass builds

Run twice after changing references, captions, bibliography text, TOC-like content, or hyperlinks.

From `template/`:

```bash
xelatex -interaction=nonstopmode -halt-on-error "report.tex" && xelatex -interaction=nonstopmode -halt-on-error "report.tex"
```

From `src/`:

```bash
xelatex -interaction=nonstopmode -halt-on-error "预习.tex" && xelatex -interaction=nonstopmode -halt-on-error "预习.tex"
```

### Single-test equivalent

There is no unit-test runner here. The closest equivalent to a single test is compiling exactly one target `.tex` file.

- Single-target check for report work: build `template/report.tex` from `template/`.
- Single-target check for preview work: build `src/预习.tex` from `src/`.
- If only one document changed, rebuild only that document first.

## Lint And Test Status

- No dedicated lint command was found.
- No automated test framework was found.
- Validation is compile-based rather than test-based.
- Inspect the first real LaTeX error; later messages are often cascades.

## Verified Environment Notes

- `template/report.tex` builds successfully when run from `template/` and usually needs two passes.
- Running `template/report.tex` from the repo root can fail because image paths resolve incorrectly.
- `src/预习.tex` currently fails in this environment because `Noto Serif CJK SC` is not installed.
- Text extracted from generated PDFs may look garbled in CLI tools even when the rendered PDF pages display correctly; use rendered page images to judge final output quality.
- Do not change fonts for portability unless the user explicitly asks.

## Editing Priorities

- Preserve the established university report layout and academic tone.
- Prefer minimal, local edits over large preamble rewrites.
- Keep Chinese content in UTF-8.
- Avoid editing `src/*_data/` unless the task is explicitly about raw experimental data.
- Treat PDFs as generated outputs or references, not primary sources.

## LaTeX Style Guidelines

### Engine and document setup

- Use `xelatex`; do not switch to `pdflatex` or another engine.
- Keep `article` unless a strong repo-specific reason requires change.
- Use `fontspec` and `xeCJK` for CJK-aware documents.

### Package and import conventions

- Keep `\usepackage` lines grouped by purpose: fonts, layout, headers, structure, tables/figures, citations, utilities.
- Avoid duplicate imports and redundant settings.
- Add packages only for an actual document need.
- Check global-layout packages carefully before introducing them.

### Formatting conventions

- Preserve the existing indentation and whitespace style of the file you edit.
- Keep long option lists vertically aligned when already formatted that way.
- Keep sectioning commands compact and consistent.
- Prefer explicit dimensions and font sizes when matching the template.
- Reuse existing macros such as `\zihaoSan`, `\zihaoSi`, `\zihaoWu`, `\zihaoXiaoWu`, `\zihaoLiu`, `\heiti`, `\kaishu`, and `\fangsong`.

### Naming conventions

- TeX filenames may be Chinese when that matches document purpose.
- Macro names should be descriptive and stable.
- New command names should avoid collisions with standard LaTeX commands.
- Labels should use prefixes such as `fig:`, `tab:`, `sec:`, and `eq:`.
- Preserve existing data filenames and lab naming conventions.

### Structure and types

- There are no programming-language types here; treat structural consistency as the equivalent concern.
- Keep macros single-purpose.
- Prefer explicit layout control over implicit magic values.
- Keep preamble changes narrow and justified.

### Tables and figures

- Prefer `booktabs` for formal tables in the report template.
- Use `longtable` only when content truly spans pages.
- Keep figure paths relative to the owning `.tex` file.
- Verify every `\includegraphics` path against a real file.
- Keep scientific figures publication-quality; the template expects about 600 dpi or better.
- Ensure all tables and figures are referenced in surrounding text.
- Keep figures immediately below the paragraph that first discusses them whenever the layout allows; avoid leaving figures on unrelated pages or as isolated float-only pages.
- If a figure drifts too far from its discussion, adjust figure size, placement specifier, or nearby paragraph breaks instead of accepting the default float result.
- For Python-generated plots in this repo, use Matplotlib `bmh` style unless the user explicitly requests a different style.
- No need to delete raw python files after plotting.
- Keep plotting style consistent across related figures in the same report.
- When plotting processed instrumental data, prefer publication/report-ready labels and captions rather than raw export filenames.
- If a plot uses normalized intensity, state that clearly in the axis label or nearby discussion because normalization can make different samples appear more similar.

### Instrument-data plotting

- For XPS, prefer plotting the intended narrow-scan region directly rather than slicing from a survey scan when both exist in the export.
- For LEIS, determine beam species and particle energy from instrument metadata such as `*.properties.txt`; do not trust filenames alone when they conflict with metadata.
- Before comparing LEIS spectra across samples, verify that species, beam energy, acquisition settings, and energy range are matched closely enough for qualitative comparison.
- If LEIS filenames and metadata disagree, call that out explicitly and treat the metadata as the more reliable source unless the user provides a better provenance record.
- If the available LEIS/XPS data support only qualitative comparison, say so clearly and avoid overclaiming rankings or composition values.

### Citations and references

- The template uses `natbib` with `unsrt` and superscript citation style.
- Preserve the existing bibliography approach unless the user requests a workflow change.
- Run a second XeLaTeX pass after citation or cross-reference edits.

## Content Conventions

- Follow Chinese chemistry-lab writing norms and GB-style units.
- Use `s`, `min`, `h`, `mol/L`, `Pa` or `kPa`, `nm`, and `r/min`.
- Keep chemical formulas properly subscripted.
- Do not silently translate terminology unless consistency requires it.
- Maintain formal academic phrasing.
- In processed tables, charts, and report text, do not expose raw source filenames unless the user explicitly wants traceability metadata.

## Error Handling Expectations

- Use `-halt-on-error` for automated validation.
- Fix the first hard error before chasing warnings.
- Distinguish real failures from rerun notices and overfull-box warnings.
- Call out missing fonts, missing images, and broken relative paths explicitly.
- If the problem is environment-specific, say so clearly.

## PDF Output Review

- After meaningful layout edits, inspect the generated PDF itself, not only the `.tex` source or compile log.
- Prefer checking rendered PDF pages for mojibake, missing glyphs, broken line wraps, clipped tables, floating issues, and abnormal whitespace.
- When reviewing figures, specifically check whether each plot stays with its relevant subsection text and whether any page contains a nearly standalone figure with excessive blank space.
- Treat `pdftotext`-style extraction artifacts cautiously: they can misrepresent Chinese text, ligatures, and symbol encoding.
- When reviewing tables, verify header repetition, column alignment, page breaks, and whether continuation pages remain readable.
- When reviewing figures, verify captions, scaling, resolution, and that labels remain legible in the final PDF.

## Safe Agent Workflow

- Read the target `.tex` file before editing.
- If editing `template/report.tex`, also inspect referenced assets under `template/images/`.
- Rebuild only the affected document first.
- Run a second pass when references or citations changed.
- Report both the document changes and the validation result.

## What Not To Do

- Do not replace XeLaTeX with another engine for convenience.
- Do not reformat the entire file just to make a small edit.
- Do not rename or move experimental data files without explicit instruction.
- Do not delete generated PDFs or logs unless asked.
- Do not assume a missing local font should be changed automatically.

## Bottom Line

- This is a document-centric repo.
- Compilation is the primary validation mechanism.
- Good agent behavior here is conservative editing, strict path awareness, XeLaTeX-only builds, and careful preservation of the established academic format.
