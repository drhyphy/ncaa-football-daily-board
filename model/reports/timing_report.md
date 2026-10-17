# NCAA football moneyline timing report

Generated: 2026-10-17T10:41:13Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 1 | 0.1874 | -100.0% | 0.0% | 0.0% |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1340 | — | — | — |
| D6 | 144–168 hours | 272 | 7 | 3 | 0.1411 | -100.0% | 8.9% | 0.3% |
| D5 | 120–144 hours | 383 | 40 | 33 | 0.1434 | -26.2% | 3.0% | 0.9% |
| D4 | 96–120 hours | 404 | 46 | 36 | 0.1439 | -17.2% | 1.0% | 0.5% |
| D3 | 72–96 hours | 376 | 40 | 31 | 0.1463 | -14.9% | 0.0% | 0.2% |
| D2 | 48–72 hours | 385 | 41 | 31 | 0.1434 | -30.1% | 0.8% | 0.3% |
| D1 | 24–48 hours | 383 | 48 | 37 | 0.1418 | -25.4% | 1.0% | 0.4% |
| D0 | 0–24 hours | 394 | 42 | 32 | 0.1411 | -16.6% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 3 | 3.2% | 66.7% | -6.2% |
| D5 | D4 | 35 | 0.0% | 37.1% | 0.0% |
| D4 | D3 | 36 | 0.9% | 50.0% | -0.6% |
| D3 | D2 | 35 | -0.4% | 37.1% | 0.5% |
| D2 | D1 | 38 | -0.4% | 31.6% | 0.1% |
| D1 | D0 | 40 | -0.0% | 47.5% | 0.5% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

