# NCAA football moneyline timing report

Generated: 2026-09-26T11:07:28Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 83 | 0 | 0 | 0.1516 | — | — | — |
| D7 | 168–192 hours | 41 | 0 | 0 | 0.1348 | — | — | — |
| D6 | 144–168 hours | 178 | 2 | 1 | 0.1069 | -100.0% | 6.7% | 1.1% |
| D5 | 120–144 hours | 229 | 18 | 13 | 0.1104 | -71.9% | 1.4% | 0.2% |
| D4 | 96–120 hours | 243 | 17 | 13 | 0.1153 | -49.2% | 2.2% | 0.7% |
| D3 | 72–96 hours | 208 | 13 | 10 | 0.1087 | -68.0% | 0.8% | 0.5% |
| D2 | 48–72 hours | 215 | 14 | 10 | 0.1054 | -100.0% | 1.6% | 0.2% |
| D1 | 24–48 hours | 211 | 15 | 11 | 0.1014 | -71.4% | 0.4% | 0.0% |
| D0 | 0–24 hours | 222 | 14 | 9 | 0.1037 | -65.6% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 2 | 1.2% | 50.0% | -4.2% |
| D5 | D4 | 16 | 1.0% | 50.0% | -0.3% |
| D4 | D3 | 12 | 1.2% | 75.0% | -0.7% |
| D3 | D2 | 12 | 0.7% | 25.0% | -0.1% |
| D2 | D1 | 13 | -0.1% | 23.1% | 0.1% |
| D1 | D0 | 13 | -0.1% | 53.8% | 0.2% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

