# NCAA football moneyline timing report

Generated: 2026-10-05T10:37:41Z

Each bucket represents a separate hypothetical entry strategy. Duplicate same-game snapshots inside a bucket are reduced to the latest snapshot. Price CLV is the primary timing metric; ROI and hit rate are secondary.

Status: **collecting** — No timing bucket has 50 graded signals yet.

| Horizon | Window | Games captured | Signals | Graded signals | Brier | ROI | Price CLV | Prob. CLV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| D8+ | 192+ hours | 91 | 1 | 0 | 0.1468 | — | — | — |
| D7 | 168–192 hours | 43 | 0 | 0 | 0.1348 | — | — | — |
| D6 | 144–168 hours | 242 | 3 | 2 | 0.1268 | -100.0% | 8.0% | 0.3% |
| D5 | 120–144 hours | 331 | 33 | 27 | 0.1280 | -47.4% | 2.5% | 0.8% |
| D4 | 96–120 hours | 307 | 31 | 28 | 0.1277 | -28.8% | 0.7% | 0.3% |
| D3 | 72–96 hours | 270 | 26 | 24 | 0.1261 | -30.8% | -0.7% | -0.0% |
| D2 | 48–72 hours | 274 | 24 | 22 | 0.1231 | -45.3% | 0.2% | 0.0% |
| D1 | 24–48 hours | 269 | 27 | 26 | 0.1214 | -40.0% | 0.9% | 0.2% |
| D0 | 0–24 hours | 279 | 22 | 22 | 0.1217 | -33.6% | 0.0% | 0.0% |

## Persistent-signal price drift

This matched comparison uses only games where the same side remained qualified in both adjacent horizons.

| Earlier | Later | Persistent signals | Earlier price advantage | Earlier price better | Later EV change |
|---|---:|---:|---:|---:|---:|
| D8+ | D7 | 0 | — | — | — |
| D7 | D6 | 0 | — | — | — |
| D6 | D5 | 2 | 1.2% | 50.0% | -4.2% |
| D5 | D4 | 25 | 0.3% | 40.0% | -0.1% |
| D4 | D3 | 22 | 1.4% | 59.1% | -0.9% |
| D3 | D2 | 21 | -0.2% | 38.1% | 0.7% |
| D2 | D1 | 22 | -0.7% | 31.8% | 0.4% |
| D1 | D0 | 21 | 0.6% | 57.1% | -0.2% |

Interpretation rules:

- Do not declare an optimal window until a bucket reaches the configured minimum graded-signal count.
- Prefer positive price CLV that persists across conferences, favorite/underdog bands, and weeks.
- Compare timing buckets on the same model version and deduplicate to one hypothetical bet per game per bucket.
- A later recommendation is not automatically better: it may have more accurate information but a worse price.

