# NCAA football moneyline timing report

Generated: 2026-11-28T19:09:33Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **provisional** — Highest mean price CLV among sufficiently sampled buckets; ROI is a secondary tiebreaker.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 1 | 0.1948 | -100.0% | 0.0% | 0.0% |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1340 | — | — | — |
| D6 | 144–168 hours | 417 | 11 | 11 | 0.1675 | 11.3% | 7.9% | 0.7% |
| D5 | 120–144 hours | 696 | 66 | 64 | 0.1704 | -27.6% | 2.8% | 0.8% |
| D4 | 96–120 hours | 750 | 73 | 69 | 0.1701 | -25.0% | 0.9% | 0.2% |
| D3 | 72–96 hours | 709 | 67 | 63 | 0.1723 | -33.0% | 0.1% | 0.0% |
| D2 | 48–72 hours | 751 | 72 | 68 | 0.1715 | -41.3% | -0.6% | -0.2% |
| D1 | 24–48 hours | 731 | 79 | 75 | 0.1700 | -35.0% | 0.2% | 0.1% |
| D0 | 0–24 hours | 753 | 75 | 70 | 0.1691 | -27.3% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 4 | 1.0% | 50.0% | -4.5% |
| D5 | D4 | 52 | 0.2% | 44.2% | -0.1% |
| D4 | D3 | 56 | 0.7% | 44.6% | -0.5% |
| D3 | D2 | 55 | -0.7% | 32.7% | 0.6% |
| D2 | D1 | 63 | -0.4% | 28.6% | 0.0% |
| D1 | D0 | 66 | -0.5% | 34.8% | 0.5% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

