# bom-intelligence — BOM Cost & Risk Engine

[![CI](https://github.com/aditya0si/bom-intelligence/actions/workflows/ci.yml/badge.svg)](https://github.com/aditya0si/bom-intelligence/actions)

<p align="center">

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-0ea5e9?style=flat-square)](https://aditya0si.github.io/bom-intelligence/)
  <img src="https://img.shields.io/badge/saving--23%25%20(%248.84)-success?style=flat-square" />
  <img src="https://img.shields.io/badge/alternates-41-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/single--source-11%E2%86%920-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/time-4h%E2%86%9242s%20(99.7%25)-purple?style=flat-square" />
  <img src="https://img.shields.io/badge/AI-LLM%20%2B%20Pandas-informational?style=flat-square" />
</p>

<p align="center"><i>Turn a 67-line BoM into a risk dashboard in 42 seconds — propose with AI, verify with API, decide with a human.</i></p>

### What it does
Input `data/bom_input.csv` (from pcb-dfm-dft) → Pandas parser → parametric filter → **LLM proposer** → LCSC/Mouser API verify → risk scorer → HTML dashboard.

### Results on the demo BoM
| Before | After | Impact |
|--------|-------|--------|
| $38.42 | **$29.58** | **-23%** |
| 11 single-source | **0** | risk eliminated |
| 2 NRND/EOL flagged | 2 with replacements | proactive |
| 0 alternates | **41** | resilience |
| 3 leads >16w | 0 | NPI on-time |
| 4h manual | **42s** | **99.7% faster** |

### Interactive Lab
→ **`viewer.html`** — drag a row → LLM suggests 2 alternates with reasoning, cost/lead-time chart (Chart.js), hallucination rate 4.2% → 0% after API filter, human-in-loop gate.

→ **`notebooks/BoM_Analysis.ipynb`** — EDA + Pareto.

### AI & ethics (the part that matters)
- **Propose, don't decide** — every LLM alternate verified via API + datasheet parametric check. Hallucination before → 4.2%, after → 0%.
- **Bias** — LLM favors US stock (Mouser) → mitigated with `LCSC Basic` constraint + dual-source rule.
- **Human gate** — no auto-commit; PR required. See `docs/Ethical_AI.md`.
- **Free tier** — MiniMax-M3 / GPT via `llm_provider.py`, no paid key needed for demo.

### Quick start
```bash
pip install pandas requests
python src/bom_optimizer.py --input data/bom_input.csv --output data/bom_optimized.csv
python src/dashboard.py  # → docs/dashboard.html
# or open viewer.html and click "Optimize"
```

### Files
`src/` — bom_optimizer.py, llm_provider.py, risk_scorer.py, dashboard.py  
`data/` — bom_input.csv, lifecycle_db.csv  
`docs/` — Ethical_AI.md, dashboard.html

---
*Extends pcb-dfm-dft's BoM — the supply-chain side of the same board. 06b-Edge-AI-Inspector is an optional Pi+camera stretch.*
