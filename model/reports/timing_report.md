# NCAA football moneyline timing report

Generated: 2026-11-23T12:25:43Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **provisional** — Highest mean price CLV among sufficiently sampled buckets; ROI is a secondary tiebreaker.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 1 | 0.1971 | -100.0% | 0.0% | 0.0% |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1340 | — | — | — |
| D6 | 144–168 hours | 417 | 11 | 11 | 0.1675 | 11.3% | 7.9% | 0.7% |
| D5 | 120–144 hours | 696 | 66 | 63 | 0.1716 | -26.4% | 2.6% | 0.7% |
| D4 | 96–120 hours | 698 | 69 | 68 | 0.1708 | -23.9% | 0.9% | 0.2% |
| D3 | 72–96 hours | 644 | 62 | 62 | 0.1730 | -31.9% | 0.1% | 0.0% |
| D2 | 48–72 hours | 685 | 68 | 68 | 0.1717 | -41.3% | -0.6% | -0.2% |
| D1 | 24–48 hours | 688 | 75 | 75 | 0.1702 | -35.0% | 0.2% | 0.1% |
| D0 | 0–24 hours | 690 | 70 | 70 | 0.1691 | -27.3% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 4 | 1.0% | 50.0% | -4.5% |
| D5 | D4 | 50 | 0.2% | 44.0% | -0.1% |
| D4 | D3 | 53 | 0.8% | 47.2% | -0.5% |
| D3 | D2 | 51 | -0.7% | 31.4% | 0.6% |
| D2 | D1 | 59 | -0.4% | 28.8% | -0.0% |
| D1 | D0 | 62 | -0.5% | 35.5% | 0.6% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

