# NCAA football moneyline timing report

Generated: 2026-11-10T12:06:26Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **provisional** — Highest mean price CLV among sufficiently sampled buckets; ROI is a secondary tiebreaker.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 1 | 0.2045 | -100.0% | 0.0% | 0.0% |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1340 | — | — | — |
| D6 | 144–168 hours | 391 | 11 | 11 | 0.1639 | 11.3% | 7.9% | 0.7% |
| D5 | 120–144 hours | 584 | 58 | 52 | 0.1669 | -24.0% | 2.3% | 0.6% |
| D4 | 96–120 hours | 625 | 64 | 60 | 0.1666 | -21.5% | 1.3% | 0.5% |
| D3 | 72–96 hours | 527 | 53 | 53 | 0.1695 | -29.2% | 0.3% | 0.2% |
| D2 | 48–72 hours | 562 | 58 | 58 | 0.1682 | -34.9% | -0.4% | -0.2% |
| D1 | 24–48 hours | 560 | 66 | 66 | 0.1669 | -32.1% | 0.2% | 0.1% |
| D0 | 0–24 hours | 568 | 57 | 57 | 0.1660 | -22.9% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 4 | 1.0% | 50.0% | -4.5% |
| D5 | D4 | 47 | 0.0% | 40.4% | -0.1% |
| D4 | D3 | 45 | 0.8% | 51.1% | -0.6% |
| D3 | D2 | 44 | -0.4% | 36.4% | 0.5% |
| D2 | D1 | 52 | -0.5% | 28.8% | 0.1% |
| D1 | D0 | 54 | -0.5% | 37.0% | 0.6% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

