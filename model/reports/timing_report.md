# NCAA football moneyline timing report

Generated: 2026-10-04T10:37:34Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 0 | 0.1484 | — | — | — |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1348 | — | — | — |
| D6 | 144–168 hours | 242 | 3 | 2 | 0.1265 | -100.0% | 8.0% | 0.3% |
| D5 | 120–144 hours | 288 | 28 | 23 | 0.1264 | -68.8% | 1.8% | 0.5% |
| D4 | 96–120 hours | 302 | 29 | 23 | 0.1262 | -45.0% | 2.2% | 0.7% |
| D3 | 72–96 hours | 266 | 25 | 19 | 0.1243 | -50.9% | 0.7% | 0.4% |
| D2 | 48–72 hours | 272 | 23 | 18 | 0.1208 | -77.6% | 0.8% | 0.2% |
| D1 | 24–48 hours | 268 | 26 | 21 | 0.1188 | -65.8% | 1.2% | 0.3% |
| D0 | 0–24 hours | 279 | 22 | 18 | 0.1192 | -44.5% | 0.0% | 0.0% |

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
| D1 | D0 | 21 | 0.6% | 57.1% | -0.2% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

