# NCAA football moneyline timing report

Generated: 2026-10-28T16:44:30Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **provisional** — Highest mean price CLV among sufficiently sampled buckets; ROI is a secondary tiebreaker.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 1 | 0.1944 | -100.0% | 0.0% | 0.0% |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1340 | — | — | — |
| D6 | 144–168 hours | 331 | 10 | 7 | 0.1599 | -27.1% | 12.1% | 2.3% |
| D5 | 120–144 hours | 471 | 48 | 45 | 0.1613 | -36.0% | 2.0% | 0.7% |
| D4 | 96–120 hours | 508 | 56 | 53 | 0.1610 | -26.3% | 1.2% | 0.5% |
| D3 | 72–96 hours | 473 | 50 | 45 | 0.1636 | -31.4% | 0.5% | 0.4% |
| D2 | 48–72 hours | 458 | 47 | 46 | 0.1624 | -43.3% | -0.2% | 0.0% |
| D1 | 24–48 hours | 443 | 55 | 55 | 0.1613 | -38.6% | 0.5% | 0.3% |
| D0 | 0–24 hours | 452 | 46 | 46 | 0.1607 | -28.4% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 3 | 3.2% | 66.7% | -6.2% |
| D5 | D4 | 40 | -0.1% | 35.0% | 0.1% |
| D4 | D3 | 42 | 0.8% | 50.0% | -0.6% |
| D3 | D2 | 38 | -0.3% | 39.5% | 0.4% |
| D2 | D1 | 43 | -0.5% | 27.9% | 0.2% |
| D1 | D0 | 44 | -0.2% | 43.2% | 0.5% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

