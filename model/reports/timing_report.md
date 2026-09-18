# NCAA football moneyline timing report

Generated: 2026-09-18T11:10:51Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 83 | 0 | 0 | 0.1516 | — | — | — |
| D7 | 168–192 hours | 41 | 0 | 0 | 0.1348 | — | — | — |
| D6 | 144–168 hours | 129 | 1 | 1 | 0.1029 | -100.0% | 6.7% | 1.1% |
| D5 | 120–144 hours | 175 | 13 | 8 | 0.0977 | -54.4% | 0.8% | 0.2% |
| D4 | 96–120 hours | 182 | 13 | 8 | 0.1044 | -17.5% | 3.0% | 1.0% |
| D3 | 72–96 hours | 149 | 10 | 8 | 0.1035 | -60.0% | 0.8% | 0.7% |
| D2 | 48–72 hours | 153 | 10 | 8 | 0.1011 | -100.0% | 2.0% | 0.3% |
| D1 | 24–48 hours | 151 | 11 | 9 | 0.0948 | -65.0% | 0.4% | 0.0% |
| D0 | 0–24 hours | 137 | 8 | 8 | 0.1003 | -61.3% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 1 | 0.0% | 0.0% | 0.0% |
| D5 | D4 | 12 | 1.4% | 50.0% | -0.8% |
| D4 | D3 | 9 | 2.1% | 88.9% | -0.6% |
| D3 | D2 | 9 | 1.1% | 33.3% | -0.2% |
| D2 | D1 | 9 | 1.1% | 33.3% | -0.9% |
| D1 | D0 | 8 | 0.2% | 50.0% | 0.3% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

