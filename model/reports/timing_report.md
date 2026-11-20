# NCAA football moneyline timing report

Generated: 2026-11-20T12:14:10Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **provisional** — Highest mean price CLV among sufficiently sampled buckets; ROI is a secondary tiebreaker.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 1 | 0.2005 | -100.0% | 0.0% | 0.0% |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1340 | — | — | — |
| D6 | 144–168 hours | 391 | 11 | 11 | 0.1675 | 11.3% | 7.9% | 0.7% |
| D5 | 120–144 hours | 637 | 63 | 58 | 0.1710 | -28.0% | 2.6% | 0.8% |
| D4 | 96–120 hours | 684 | 68 | 64 | 0.1703 | -19.1% | 1.1% | 0.4% |
| D3 | 72–96 hours | 643 | 62 | 58 | 0.1730 | -27.2% | 0.3% | 0.2% |
| D2 | 48–72 hours | 683 | 68 | 63 | 0.1717 | -36.6% | -0.7% | -0.2% |
| D1 | 24–48 hours | 686 | 75 | 70 | 0.1701 | -32.9% | 0.0% | 0.1% |
| D0 | 0–24 hours | 636 | 65 | 65 | 0.1687 | -21.7% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 4 | 1.0% | 50.0% | -4.5% |
| D5 | D4 | 49 | 0.1% | 42.9% | -0.1% |
| D4 | D3 | 53 | 0.8% | 47.2% | -0.5% |
| D3 | D2 | 51 | -0.7% | 31.4% | 0.6% |
| D2 | D1 | 59 | -0.4% | 28.8% | -0.0% |
| D1 | D0 | 58 | -0.6% | 34.5% | 0.7% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

