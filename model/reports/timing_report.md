# NCAA football moneyline timing report

Generated: 2026-10-10T10:36:36Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 0 | 0.1458 | — | — | — |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1340 | — | — | — |
| D6 | 144–168 hours | 242 | 3 | 2 | 0.1270 | -100.0% | 8.0% | 0.3% |
| D5 | 120–144 hours | 331 | 33 | 28 | 0.1282 | -42.0% | 2.0% | 0.6% |
| D4 | 96–120 hours | 350 | 36 | 31 | 0.1295 | -28.4% | 0.9% | 0.3% |
| D3 | 72–96 hours | 318 | 31 | 27 | 0.1286 | -29.6% | 0.2% | 0.2% |
| D2 | 48–72 hours | 326 | 30 | 27 | 0.1255 | -46.5% | 0.6% | 0.2% |
| D1 | 24–48 hours | 324 | 36 | 30 | 0.1239 | -40.0% | 1.4% | 0.4% |
| D0 | 0–24 hours | 335 | 31 | 25 | 0.1240 | -32.2% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 2 | 1.2% | 50.0% | -4.2% |
| D5 | D4 | 28 | 0.7% | 42.9% | -0.2% |
| D4 | D3 | 27 | 1.0% | 51.9% | -0.8% |
| D3 | D2 | 26 | -0.4% | 38.5% | 0.6% |
| D2 | D1 | 28 | -0.2% | 39.3% | 0.1% |
| D1 | D0 | 29 | 0.4% | 55.2% | 0.4% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

