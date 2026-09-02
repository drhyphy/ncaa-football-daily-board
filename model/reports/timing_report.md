# NCAA football moneyline timing report

Generated: 2026-09-02T10:45:17Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 56 | 0 | 0 | — | — | — | — |
| D7 | 168–192 hours | 1 | 0 | 0 | — | — | — | — |
| D6 | 144–168 hours | 51 | 1 | 0 | — | — | — | — |
| D5 | 120–144 hours | 56 | 3 | 0 | — | — | — | — |
| D4 | 96–120 hours | 63 | 3 | 0 | — | — | — | — |
| D3 | 72–96 hours | 62 | 3 | 0 | — | — | — | — |
| D2 | 48–72 hours | 13 | 1 | 0 | — | — | — | — |
| D1 | 24–48 hours | 7 | 1 | 0 | — | — | — | — |
| D0 | 0–24 hours | 0 | 0 | 0 | — | — | — | — |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 1 | 0.0% | 0.0% | 0.0% |
| D5 | D4 | 2 | 4.1% | 50.0% | -1.0% |
| D4 | D3 | 3 | 0.5% | 66.7% | 0.8% |
| D3 | D2 | 1 | 0.0% | 0.0% | -0.5% |
| D2 | D1 | 0 | — | — | — |
| D1 | D0 | 0 | — | — | — |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

