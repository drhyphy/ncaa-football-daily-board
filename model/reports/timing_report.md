# NCAA football moneyline timing report

Generated: 2026-09-06T11:46:27Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 83 | 0 | 0 | — | — | — | — |
| D7 | 168–192 hours | 41 | 0 | 0 | — | — | — | — |
| D6 | 144–168 hours | 91 | 1 | 1 | 0.0835 | -100.0% | 6.7% | 1.1% |
| D5 | 120–144 hours | 60 | 3 | 3 | 0.0840 | -100.0% | 2.2% | 0.5% |
| D4 | 96–120 hours | 64 | 3 | 3 | 0.0952 | 1.7% | -1.7% | -0.3% |
| D3 | 72–96 hours | 63 | 3 | 3 | 0.0957 | 6.7% | -2.0% | -0.6% |
| D2 | 48–72 hours | 64 | 2 | 2 | 0.0936 | -100.0% | -5.3% | -1.1% |
| D1 | 24–48 hours | 62 | 4 | 4 | 0.0818 | -21.3% | 0.1% | -0.3% |
| D0 | 0–24 hours | 65 | 3 | 3 | 0.0951 | 3.3% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 1 | 0.0% | 0.0% | 0.0% |
| D5 | D4 | 2 | 4.1% | 50.0% | -1.0% |
| D4 | D3 | 3 | 0.5% | 66.7% | 0.8% |
| D3 | D2 | 2 | 0.7% | 50.0% | -1.0% |
| D2 | D1 | 2 | -3.6% | 0.0% | 2.4% |
| D1 | D0 | 3 | -0.6% | 33.3% | 0.0% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

