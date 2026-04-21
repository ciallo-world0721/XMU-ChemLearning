# AGENTS.md — Scientific Experiment Report Project

## Project Overview

This is a **scientific experiment report project** for "中心科学实验 IV" (Central Science Experiment IV) at Xiamen University. The experiment focuses on **observing Brownian motion to determine Boltzmann's constant**.

**Primary deliverable**: A LaTeX experiment report (`report.tex`) with data analysis, figures, and conclusions.

**Language**: Chinese (Simplified) for report content, English for code.

---

## Build Commands

### Compile LaTeX Report
```bash
xelatex report.tex
```
XeLaTeX is required for Chinese font support (SimSun, SimHei, KaiTi, FangSong).

### Run Python Data Analysis
```bash
python <script_name>.py
```
Use global Python environment. If dependencies are missing, create virtual environment with `uv`:
```bash
uv venv && uv pip install pandas matplotlib scipy numpy openpyxl
```

### View PDF Files
Use the `pdf` skill or `chrome-devtools` MCP to view generated reports and reference materials.

---

## Project Structure

```
cse4-3/
├── AGENTS.md           # This file
├── report.tex          # Your working report (copy from template/)
├── *.py                # Data analysis scripts (place in root)
├── src/
│   ├── data/           # Experimental data
│   │   ├── 1/, 2/, 3/  # Tracker data per measurement group
│   │   └── *.xlsx      # Particle position data
│   ├── img/            # Generated figures (save here)
│   └── *.pdf           # Reference reports and lecture notes
├── template/
│   ├── report.tex      # Report template (DO NOT MODIFY)
│   └── images/         # Template images (logo, etc.)
├── commands/
│   ├── initial.md      # General project instructions
│   └── project.md      # Experiment-specific requirements
└── .opencode/skills/   # PDF and XLSX processing skills
```

---

## Data Files

| File | Description |
|------|-------------|
| `src/data/{1,2,3}/*.xlsx` | Particle position data from Tracker (t, x, y columns) |
| `src/data/*/real-time_measurement_data.xlsx` | Particle radius measurements (54 nm/px conversion) |
| `src/data/analysis_summary.json` | Pre-computed analysis results (diffusion coefficients, Boltzmann constant estimates) |

**Key conversion**: Image scale is ~54 nm/pixel. Original images are 2560×1920 pixels.

---

## Code Style Guidelines

### Python

**Plotting Style**:
```python
import matplotlib.pyplot as plt
plt.style.use('bmh')  # REQUIRED: Use 'bmh' style for all plots
```

**Data Analysis Libraries**:
- `pandas` — Data manipulation
- `numpy` — Numerical operations
- `scipy.stats` — Statistical tests (normality, etc.)
- `matplotlib` — Plotting
- `openpyxl` — Excel file reading

**Naming Conventions**:
- Variables: `snake_case`
- Functions: `snake_case`
- Constants: `UPPER_CASE`

**File Handling**:
```python
# Reading Excel data
import pandas as pd
df = pd.read_excel('src/data/1/1.xlsx')
```

**Figure Output**:
```python
# Save figures to src/img/
plt.savefig('src/img/figure_name.png', dpi=600, bbox_inches='tight')
```

### LaTeX

**Document Class**: `article` with A4 paper
**Font Setup**: SimSun (main), SimHei (headings), Times New Roman (English)
**Compiler**: XeLaTeX only (not pdflatex)

**Section Formatting**:
- 4号黑体 (16pt SimHei) for `\section`
- 5号黑体 (10.5pt SimHei) for `\subsection`
- 5号宋体 (10.5pt SimSun) for body text

**Figure Requirements**:
- Minimum 600 DPI
- Half-column: 50mm × 80mm
- Full-column: 150mm width
- Labels: 6号 (7.5pt) for axis labels and numbers

**Table Style**: Three-line tables (`\toprule`, `\midrule`, `\bottomrule` from `booktabs`)

---

## Key Requirements from `commands/`

### From `initial.md`:
1. Copy `template/report.tex` to project root before editing
2. DO NOT modify `template/` directory
3. Save generated images to `src/img/`
4. Keep Python scripts in project root
5. Use `bmh` matplotlib style for all plots
6. Final report should read naturally — no file paths or technical details

### From `project.md`:
1. Process all particle tracking data from groups 1, 2, 3
2. Calculate displacement relative to previous second
3. Compute mean and standard deviation per group
4. Plot normal distribution and perform statistical tests
5. Add "思考题" (Questions) section as Section 4
6. Move original "结论" (Conclusion) to Section 5
7. **Ignore**: `*.tif`, `*.mp4` files

---

## Statistical Analysis Required

For each data group:
1. Calculate frame-to-frame displacement (Δx, Δy)
2. Compute mean and standard deviation of displacements
3. Test for normality (e.g., Shapiro-Wilk test)
4. Plot histogram with fitted normal distribution
5. Calculate diffusion coefficient: D = σ²/(2Δt)
6. Estimate Boltzmann constant: k_B = D × 6πηr / T

**Reference values** (from `analysis_summary.json`):
- Groups 1-3 show k_B estimates in range 2.6–4.2 × 10⁻²³ J/K
- Standard Boltzmann constant: 1.38 × 10⁻²³ J/K

---

## Error Handling

**Python**:
- Handle missing data with `pd.notna()` checks
- Validate Excel file structure before processing
- Use try/except for file operations

**LaTeX**:
- Check for missing images before compilation
- Verify figure paths are relative to report.tex location

---

## Important Patterns

### Excel Data Processing
```python
import pandas as pd

# Load Tracker data
df = pd.read_excel('src/data/1/1.xlsx')

# Calculate displacement (assuming 1 second intervals)
df['dx'] = df['x'].diff()
df['dy'] = df['y'].diff()

# Convert pixels to micrometers
nm_per_px = 54
df['dx_um'] = df['dx'] * nm_per_px / 1000
```

### Normal Distribution Plot
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.style.use('bmh')

# Fit normal distribution
mu, std = data.mean(), data.std()
x = np.linspace(mu - 4*std, mu + 4*std, 100)
plt.hist(data, bins=15, density=True, alpha=0.7)
plt.plot(x, stats.norm.pdf(x, mu, std), 'r-', lw=2)
plt.xlabel('Displacement (μm)')
plt.ylabel('Probability Density')
plt.savefig('src/img/normal_dist.png', dpi=600)
```

---

## Skills Available

### `/pdf` Skill
For reading PDF reference materials, extracting text/tables, viewing generated reports.

### `/xlsx` Skill  
For reading and processing Excel data files. Key points:
- Use `pandas.read_excel()` for data analysis
- Use `openpyxl` for formatting-heavy operations
- Formula recalculation requires LibreOffice

---

## Checklist Before Submission

- [ ] Report compiled without errors (`xelatex report.tex`)
- [ ] All figures saved to `src/img/` at 600+ DPI
- [ ] Python scripts retained in project root
- [ ] `bmh` style used for all matplotlib plots
- [ ] Template directory unchanged
- [ ] No personal information in report
- [ ] No file paths mentioned in report text
- [ ] 思考题 section added as Section 4
- [ ] 结论 section moved to Section 5
