#!/usr/bin/env python3
"""
Turn vertical label rows into horizontal LaTeX rows (grouped by label).

Paste your raw data into raw_text (tabs or spaces OK). Each line must be:
Label <tab/space> Examples <tab/space> Correct <tab/space> Percent

The script groups occurrences by label in the order they appear,
sorts labels alphabetically, rounds percentages to integers,
formats percent as 'NN\%', and copies the result to the clipboard.
"""
import pyperclip
from collections import defaultdict

raw_text = """
H	4	2	50.00
L	7	7	100.00
V	5	5	100.00
T	5	5	100.00
Q	3	1	33.33
A	6	3	50.00
E	6	3	50.00
Z	4	3	75.00
H	8	1	12.50
A	3	1	33.33
T	9	9	100.00
L	3	3	100.00
E	4	2	50.00
V	4	4	100.00
Z	5	4	80.00
Q	4	0	 0.00
H	7	0	 0.00
Q	4	0	 0.00
V	4	4	100.00
L	8	8	100.00
E	7	2	28.57
A	4	4	100.00
T	3	3	100.00
Z	3	2	66.67
A	7	2	28.57
Z	8	4	50.00
Q	9	4	44.44
T	3	3	100.00
L	2	2	100.00
E	3	1	33.33
V	7	7	100.00
H	1	0	 0.00
"""

# ---- parse ----
lines = [ln.strip() for ln in raw_text.strip().splitlines() if ln.strip() and not ln.strip().startswith("#")]
groups = defaultdict(list)  # label -> list of (ex, cor, pct_int)

for ln in lines:
    parts = ln.split()
    if len(parts) < 4:
        continue
    label, ex, cor, pct_raw = parts[0], parts[1], parts[2], parts[3]
    try:
        pct_int = int(round(float(pct_raw)))
    except Exception:
        # fallback if percent not parseable
        pct_int = pct_raw
    groups[label].append((ex, cor, f"{pct_int}\\%"))

# determine max occurrences (columns per label)
max_cols = max((len(v) for v in groups.values()), default=0)

# build LaTeX rows (labels sorted alphabetically)
rows = []
for label in sorted(groups.keys()):
    parts = [label]
    entries = groups[label]
    # keep entries in the same order they appeared
    for (ex, cor, pct) in entries:
        parts.extend([ex, cor, pct])
    # fill missing entries (if some labels have fewer occurrences than max_cols)
    missing = max_cols - len(entries)
    for _ in range(missing):
        parts.extend(["-", "-", "-"])
    row = "        " + " & ".join(parts) + r" \\"
    rows.append(row)

output = "\n".join(rows) + "\n"

# copy to clipboard and print
pyperclip.copy(output)
print("LaTeX rows copied to clipboard:\n")
print(output)
