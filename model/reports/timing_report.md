# NCAA football moneyline timing report

Generated: 2026-10-02T10:38:02Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 0 | 0.1484 | — | — | — |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1348 | — | — | — |
| D6 | 144–168 hours | 217 | 2 | 2 | 0.1200 | -100.0% | 8.0% | 0.3% |
| D5 | 120–144 hours | 284 | 27 | 18 | 0.1185 | -79.7% | 0.9% | 0.2% |
| D4 | 96–120 hours | 298 | 29 | 17 | 0.1194 | -61.2% | 1.4% | 0.4% |
| D3 | 72–96 hours | 264 | 24 | 14 | 0.1169 | -62.1% | 0.5% | 0.5% |
| D2 | 48–72 hours | 271 | 22 | 14 | 0.1131 | -100.0% | 0.3% | 0.1% |
| D1 | 24–48 hours | 268 | 26 | 15 | 0.1108 | -79.0% | 0.3% | 0.0% |
| D0 | 0–24 hours | 227 | 15 | 14 | 0.1119 | -55.7% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 2 | 1.2% | 50.0% | -4.2% |
| D5 | D4 | 24 | 0.6% | 41.7% | -0.2% |
| D4 | D3 | 22 | 1.4% | 59.1% | -0.9% |
| D3 | D2 | 20 | -0.6% | 35.0% | 0.8% |
| D2 | D1 | 21 | -0.1% | 33.3% | 0.2% |
| D1 | D0 | 14 | 0.7% | 57.1% | -0.2% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

