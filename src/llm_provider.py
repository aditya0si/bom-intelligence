# src/llm_provider.py — Free tier LLM adapter (GMI Cloud pattern)
# Uses MiniMax-M3 free (1M ctx) via api.gmi-serving.com/v1 — same as arch.bitnet
import os, requests
GMI_BASE = "https://api.gmi-serving.com/v1"
MODEL = "MiniMaxAI/MiniMax-M3"  # free

PROMPT = """You are a supply chain engineer. Given BoM line: {line}
Propose 2 alternates with same value/footprint/tolerance, lower cost, LCSC Basic preferred.
Return JSON: [{"part": "...", "reason": "...", "risk": "low"}]
Verify parametric match, flag if tolerance differs.
"""

def propose(line: str, api_key=None):
    # In demo, mock; in real, call GMI with browser UA to avoid CF 403
    # headers = {"Authorization": f"Bearer {api_key}", "User-Agent": "Mozilla/5.0"}
    # r = requests.post(f"{GMI_BASE}/chat/completions", json={"model": MODEL, "messages": [{"role":"user","content": PROMPT.format(line=line)}]}, headers=headers)
    return [{"part": "CL10B104KB8NNNC", "reason": "100nF 0603 X7R 16V same, 30% cheaper, 45k stock", "risk": "low"}]

if __name__=="__main__":
    print(propose("C14663 100nF 0603 16V X7R"))
