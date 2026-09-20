# NCAA football moneyline timing report

Generated: 2026-09-20T11:08:22Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 83 | 0 | 0 | 0.1516 | — | — | — |
| D7 | 168–192 hours | 41 | 0 | 0 | 0.1348 | — | — | — |
| D6 | 144–168 hours | 178 | 2 | 1 | 0.1069 | -100.0% | 6.7% | 1.1% |
| D5 | 120–144 hours | 179 | 13 | 13 | 0.1072 | -71.9% | 1.4% | 0.2% |
| D4 | 96–120 hours | 183 | 13 | 13 | 0.1119 | -49.2% | 2.2% | 0.7% |
| D3 | 72–96 hours | 149 | 10 | 10 | 0.1048 | -68.0% | 0.8% | 0.5% |
| D2 | 48–72 hours | 153 | 10 | 10 | 0.1022 | -100.0% | 1.6% | 0.2% |
| D1 | 24–48 hours | 151 | 11 | 11 | 0.0974 | -71.4% | 0.4% | 0.0% |
| D0 | 0–24 hours | 162 | 9 | 9 | 0.1001 | -65.6% | 0.0% | 0.0% |

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
| D1 | D0 | 9 | -0.1% | 44.4% | 0.3% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

