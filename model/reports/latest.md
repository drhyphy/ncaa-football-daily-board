# NCAA football moneyline research card

Snapshot: 2026-09-03T14:40:05Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 3

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Toledo Rockets at Michigan State Spartans | Toledo Rockets | +340 (betrivers) | 25.0% | 22.8% | 10.0% | 0.29% |
| Tulane Green Wave at Duke Blue Devils | Tulane Green Wave | +260 (draftkings) | 29.6% | 27.6% | 6.6% | 0.25% |
| Colorado Buffaloes at Georgia Tech Yellow Jackets | Colorado Buffaloes | +210 (bovada) | 34.1% | 32.2% | 5.6% | 0.27% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| BYU Cougars at Utah Utes | BYU Cougars | 48.1% | 43.7% | 4.4% | 5.7% | no | too_few_books |
| Ole Miss Rebels at Texas Longhorns | Texas Longhorns | 76.3% | 72.6% | 3.7% | 0.9% | no | too_few_books|ev_below_threshold |
| Alcorn State Braves at Southern Mississippi Golden Eagles | Southern Mississippi Golden Eagles | 92.2% | 89.4% | 2.8% | -0.1% | no | ev_below_threshold |
| Ohio State Buckeyes at Indiana Hoosiers | Ohio State Buckeyes | 54.4% | 51.7% | 2.7% | 3.9% | no | ev_below_threshold |
| Texas Longhorns at Texas A&M Aggies | Texas Longhorns | 59.0% | 56.3% | 2.6% | 0.5% | no | too_few_books|ev_below_threshold |
| UNLV Rebels at Hawaii Rainbow Warriors | Hawaii Rainbow Warriors | 44.5% | 42.0% | 2.4% | 2.3% | no | ev_below_threshold |
| UCLA Bruins at California Golden Bears | California Golden Bears | 48.7% | 46.3% | 2.4% | 2.4% | no | ev_below_threshold |
| Kansas Jayhawks at Kansas State Wildcats | Kansas Jayhawks | 31.1% | 28.6% | 2.4% | 4.1% | no | too_few_books |
| Texas Longhorns at LSU Tigers | Texas Longhorns | 58.6% | 56.3% | 2.3% | -0.1% | no | too_few_books|ev_below_threshold |
| Toledo Rockets at Michigan State Spartans | Toledo Rockets | 25.0% | 22.8% | 2.2% | 10.0% | yes | — |
| Arizona State Sun Devils at Texas A&M Aggies | Texas A&M Aggies | 83.9% | 81.7% | 2.2% | -1.5% | no | too_few_books|ev_below_threshold |
| Washington Huskies at Oregon Ducks | Oregon Ducks | 85.3% | 83.2% | 2.2% | -1.5% | no | too_few_books|ev_below_threshold |
| LSU Tigers at Ole Miss Rebels | LSU Tigers | 47.9% | 45.8% | 2.1% | 0.7% | no | too_few_books|ev_below_threshold |
| Tulane Green Wave at Duke Blue Devils | Tulane Green Wave | 29.6% | 27.6% | 2.1% | 6.6% | yes | — |
| Alabama Crimson Tide at Tennessee Volunteers | Alabama Crimson Tide | 54.2% | 52.2% | 2.0% | -0.6% | no | too_few_books|ev_below_threshold |
| Western Kentucky Hilltoppers at Nevada Wolf Pack | Western Kentucky Hilltoppers | 53.0% | 51.1% | 1.9% | -0.5% | no | ev_below_threshold |
| Alabama Crimson Tide at LSU Tigers | Alabama Crimson Tide | 39.6% | 37.8% | 1.9% | 0.7% | no | too_few_books|ev_below_threshold |
| Texas A&M Aggies at Oklahoma Sooners | Texas A&M Aggies | 45.5% | 43.7% | 1.9% | 0.2% | no | too_few_books|ev_below_threshold |
| Colorado Buffaloes at Georgia Tech Yellow Jackets | Colorado Buffaloes | 34.1% | 32.2% | 1.9% | 5.6% | yes | — |
| Idaho State Bengals at Utah State Aggies | Utah State Aggies | 82.8% | 81.0% | 1.8% | -1.7% | no | ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

