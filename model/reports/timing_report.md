# NCAA football moneyline timing report

Generated: 2026-09-10T11:07:34Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 83 | 0 | 0 | 0.1913 | — | — | — |
| D7 | 168–192 hours | 41 | 0 | 0 | 0.1795 | — | — | — |
| D6 | 144–168 hours | 91 | 1 | 1 | 0.0853 | -100.0% | 6.7% | 1.1% |
| D5 | 120–144 hours | 121 | 8 | 3 | 0.0856 | -100.0% | 2.2% | 0.5% |
| D4 | 96–120 hours | 128 | 8 | 3 | 0.0964 | 1.7% | -1.7% | -0.3% |
| D3 | 72–96 hours | 129 | 8 | 3 | 0.0971 | 6.7% | -2.0% | -0.6% |
| D2 | 48–72 hours | 132 | 8 | 2 | 0.0949 | -100.0% | -5.3% | -1.1% |
| D1 | 24–48 hours | 66 | 4 | 4 | 0.0835 | -21.3% | 0.1% | -0.3% |
| D0 | 0–24 hours | 66 | 3 | 3 | 0.0936 | 3.3% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 1 | 0.0% | 0.0% | 0.0% |
| D5 | D4 | 7 | 1.5% | 42.9% | -0.1% |
| D4 | D3 | 7 | 2.1% | 85.7% | -0.7% |
| D3 | D2 | 7 | 1.3% | 28.6% | -0.3% |
| D2 | D1 | 2 | -3.6% | 0.0% | 2.4% |
| D1 | D0 | 3 | -0.6% | 33.3% | 0.0% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

