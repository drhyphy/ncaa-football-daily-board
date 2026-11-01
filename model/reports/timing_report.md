# NCAA football moneyline timing report

Generated: 2026-11-01T12:08:41Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **provisional** — Highest mean price CLV among sufficiently sampled buckets; ROI is a secondary tiebreaker.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 1 | 0.1920 | -100.0% | 0.0% | 0.0% |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1340 | — | — | — |
| D6 | 144–168 hours | 359 | 11 | 10 | 0.1607 | 6.2% | 9.2% | 1.3% |
| D5 | 120–144 hours | 476 | 48 | 48 | 0.1621 | -27.3% | 2.5% | 0.7% |
| D4 | 96–120 hours | 510 | 56 | 56 | 0.1620 | -24.2% | 1.3% | 0.5% |
| D3 | 72–96 hours | 476 | 50 | 50 | 0.1653 | -30.7% | 0.4% | 0.3% |
| D2 | 48–72 hours | 495 | 51 | 51 | 0.1636 | -38.3% | -0.4% | -0.1% |
| D1 | 24–48 hours | 493 | 59 | 59 | 0.1622 | -36.9% | 0.3% | 0.2% |
| D0 | 0–24 hours | 504 | 49 | 49 | 0.1614 | -29.5% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 3 | 3.2% | 66.7% | -6.2% |
| D5 | D4 | 40 | -0.1% | 35.0% | 0.1% |
| D4 | D3 | 42 | 0.8% | 50.0% | -0.6% |
| D3 | D2 | 41 | -0.4% | 36.6% | 0.5% |
| D2 | D1 | 47 | -0.5% | 27.7% | 0.1% |
| D1 | D0 | 47 | -0.4% | 40.4% | 0.6% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

