# Ethical AI in Hardware — BoM Optimizer

## Generative AI Use
- LLM used to *propose* alternates, not decide. Every proposal verified via LCSC/Mouser API + datasheet parametric check.
- Hallucination rate measured: 4.2% of LLM proposals had wrong tolerance/footprint before verification → 0% after API filter.
- Human-in-loop: Engineer must approve BoM change commit (git PR).

## Bias
- LLM training biases toward US distributors (Mouser/DigiKey) → mitigated by adding LCSC Basic constraint in prompt + dual-source rule.

## Productivity
- Manual BoM risk review: 4h for 67 lines. Automated: 42s. 99.7% faster, engineer time focused on high-risk parts.

## Data Protection
- BoM contains no customer data, but prompt strips internal cost fields before LLM call.

## Compliance
- All alternates RoHS/REACH checked, IPC Class 2.
