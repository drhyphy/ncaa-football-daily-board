# NCAA football moneyline research card

Snapshot: 2026-09-02T10:45:15Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 3

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Toledo Rockets at Michigan State Spartans | Toledo Rockets | +320 (betrivers) | 25.8% | 23.7% | 8.2% | 0.26% |
| Tulane Green Wave at Duke Blue Devils | Tulane Green Wave | +265 (bovada) | 29.6% | 27.6% | 8.1% | 0.31% |
| Colorado Buffaloes at Georgia Tech Yellow Jackets | Colorado Buffaloes | +215 (bovada) | 33.5% | 31.5% | 5.4% | 0.25% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| BYU Cougars at Utah Utes | BYU Cougars | 46.7% | 41.7% | 5.0% | 7.3% | no | too_few_books |
| Ole Miss Rebels at Texas Longhorns | Texas Longhorns | 76.8% | 73.4% | 3.4% | 0.4% | no | too_few_books|ev_below_threshold |
| Alcorn State Braves at Southern Mississippi Golden Eagles | Southern Mississippi Golden Eagles | 92.6% | 89.4% | 3.2% | 0.3% | no | ev_below_threshold |
| Kansas Jayhawks at Kansas State Wildcats | Kansas Jayhawks | 30.2% | 27.4% | 2.7% | 5.6% | no | too_few_books |
| Ohio State Buckeyes at Indiana Hoosiers | Ohio State Buckeyes | 54.4% | 51.7% | 2.7% | 3.0% | no | ev_below_threshold |
| UCLA Bruins at California Golden Bears | California Golden Bears | 48.3% | 45.7% | 2.6% | 1.4% | no | ev_below_threshold |
| Arizona State Sun Devils at Texas A&M Aggies | Texas A&M Aggies | 83.5% | 81.2% | 2.4% | -1.3% | no | too_few_books|ev_below_threshold |
| Texas Longhorns at LSU Tigers | Texas Longhorns | 58.6% | 56.3% | 2.3% | -0.1% | no | too_few_books|ev_below_threshold |
| Washington Huskies at Oregon Ducks | Oregon Ducks | 85.3% | 83.2% | 2.2% | -1.5% | no | too_few_books|ev_below_threshold |
| Texas A&M Aggies at Oklahoma Sooners | Texas A&M Aggies | 44.9% | 42.8% | 2.1% | 0.6% | no | too_few_books|ev_below_threshold |
| LSU Tigers at Ole Miss Rebels | LSU Tigers | 47.9% | 45.8% | 2.1% | 0.7% | no | too_few_books|ev_below_threshold |
| Toledo Rockets at Michigan State Spartans | Toledo Rockets | 25.8% | 23.7% | 2.1% | 8.2% | yes | — |
| UNLV Rebels at Hawaii Rainbow Warriors | Hawaii Rainbow Warriors | 45.7% | 43.7% | 2.1% | 2.9% | no | ev_below_threshold |
| Tulane Green Wave at Duke Blue Devils | Tulane Green Wave | 29.6% | 27.6% | 2.1% | 8.1% | yes | — |
| Texas Longhorns at Texas A&M Aggies | Texas Longhorns | 60.3% | 58.3% | 2.0% | -0.8% | no | too_few_books|ev_below_threshold |
| Colorado Buffaloes at Georgia Tech Yellow Jackets | Colorado Buffaloes | 33.5% | 31.5% | 2.0% | 5.4% | yes | — |
| Alabama Crimson Tide at Tennessee Volunteers | Alabama Crimson Tide | 54.5% | 52.6% | 1.9% | -0.8% | no | too_few_books|ev_below_threshold |
| Alabama Crimson Tide at LSU Tigers | Alabama Crimson Tide | 39.6% | 37.8% | 1.9% | 0.7% | no | too_few_books|ev_below_threshold |
| Idaho State Bengals at Utah State Aggies | Utah State Aggies | 82.7% | 80.9% | 1.8% | -2.2% | no | ev_below_threshold |
| Houston Cougars at Utah Utes | Houston Cougars | 32.2% | 30.4% | 1.7% | 1.3% | no | too_few_books|ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

