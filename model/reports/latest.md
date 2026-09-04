# NCAA football moneyline research card

Snapshot: 2026-09-04T11:08:48Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 3

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Toledo Rockets at Michigan State Spartans | Toledo Rockets | +350 (betrivers) | 25.1% | 22.8% | 12.8% | 0.37% |
| Tulane Green Wave at Duke Blue Devils | Tulane Green Wave | +270 (bovada) | 29.6% | 27.6% | 9.6% | 0.35% |
| UCLA Bruins at California Golden Bears | California Golden Bears | +120 (bovada) | 48.3% | 45.7% | 6.2% | 0.50% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| Jacksonville State Gamecocks at Ohio Bobcats | Ohio Bobcats | 56.4% | 51.2% | 5.2% | 5.4% | no | too_few_books |
| San Diego State Aztecs at UCLA Bruins | San Diego State Aztecs | 27.1% | 22.8% | 4.3% | 13.8% | no | too_few_books |
| Ole Miss Rebels at Texas Longhorns | Texas Longhorns | 76.3% | 72.6% | 3.7% | 0.9% | no | too_few_books|ev_below_threshold |
| Buffalo Bulls at Florida International Panthers | Buffalo Bulls | 31.2% | 27.7% | 3.5% | 7.7% | no | too_few_books |
| Alcorn State Braves at Southern Mississippi Golden Eagles | Southern Mississippi Golden Eagles | 92.2% | 89.4% | 2.9% | -0.1% | no | ev_below_threshold |
| Ohio State Buckeyes at Indiana Hoosiers | Ohio State Buckeyes | 54.4% | 51.7% | 2.7% | 3.9% | no | ev_below_threshold |
| Texas Longhorns at Texas A&M Aggies | Texas Longhorns | 59.0% | 56.3% | 2.6% | 0.5% | no | too_few_books|ev_below_threshold |
| UCLA Bruins at California Golden Bears | California Golden Bears | 48.3% | 45.7% | 2.6% | 6.2% | yes | — |
| California Golden Bears at Syracuse Orange | Syracuse Orange | 49.2% | 46.7% | 2.5% | 0.8% | no | too_few_books|ev_below_threshold |
| UNLV Rebels at Hawaii Rainbow Warriors | Hawaii Rainbow Warriors | 44.5% | 42.0% | 2.5% | 2.3% | no | ev_below_threshold |
| Kansas Jayhawks at Kansas State Wildcats | Kansas Jayhawks | 31.1% | 28.6% | 2.4% | 4.1% | no | too_few_books |
| UTSA Roadrunners at Texas State Bobcats | Texas State Bobcats | 50.6% | 48.3% | 2.3% | 0.2% | no | too_few_books|ev_below_threshold |
| Texas Longhorns at LSU Tigers | Texas Longhorns | 58.6% | 56.3% | 2.3% | -0.1% | no | too_few_books|ev_below_threshold |
| Toledo Rockets at Michigan State Spartans | Toledo Rockets | 25.1% | 22.8% | 2.2% | 12.8% | yes | — |
| UCF Knights at Pittsburgh Panthers | UCF Knights | 28.7% | 26.6% | 2.1% | 3.2% | no | too_few_books|ev_below_threshold |
| LSU Tigers at Ole Miss Rebels | LSU Tigers | 47.9% | 45.8% | 2.1% | 0.7% | no | too_few_books|ev_below_threshold |
| Tulane Green Wave at Duke Blue Devils | Tulane Green Wave | 29.6% | 27.6% | 2.1% | 9.6% | yes | — |
| Alabama Crimson Tide at Tennessee Volunteers | Alabama Crimson Tide | 54.2% | 52.2% | 2.0% | -0.6% | no | too_few_books|ev_below_threshold |
| Western Kentucky Hilltoppers at Nevada Wolf Pack | Western Kentucky Hilltoppers | 53.0% | 51.1% | 1.9% | -0.9% | no | ev_below_threshold |
| Alabama Crimson Tide at LSU Tigers | Alabama Crimson Tide | 39.6% | 37.8% | 1.9% | 0.7% | no | too_few_books|ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

