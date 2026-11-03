# NCAA football moneyline research card

Snapshot: 2026-11-03T12:03:05Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 4

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Texas A&M Aggies at South Carolina Gamecocks | Texas A&M Aggies | +237 (betonlineag) | 33.4% | 28.7% | 12.5% | 0.50% |
| Vanderbilt Commodores at Mississippi State Bulldogs | Mississippi State Bulldogs | -145 (bovada) | 62.6% | 57.4% | 5.7% | 0.50% |
| Alabama Crimson Tide at LSU Tigers | Alabama Crimson Tide | +192 (betonlineag) | 35.9% | 33.1% | 4.8% | 0.25% |
| Texas Longhorns at Missouri Tigers | Texas Longhorns | -142 (fanduel) | 61.1% | 56.6% | 4.2% | 0.50% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| Vanderbilt Commodores at Mississippi State Bulldogs | Mississippi State Bulldogs | 62.6% | 57.4% | 5.1% | 5.7% | yes | — |
| Texas A&M Aggies at South Carolina Gamecocks | Texas A&M Aggies | 33.4% | 28.7% | 4.7% | 12.5% | yes | — |
| Texas Longhorns at Missouri Tigers | Texas Longhorns | 61.1% | 56.6% | 4.6% | 4.2% | yes | — |
| Ball State Cardinals at UMass Minutemen | UMass Minutemen | 63.2% | 58.8% | 4.4% | 3.9% | no | ev_below_threshold |
| Oregon Ducks at Ohio State Buckeyes | Ohio State Buckeyes | 74.5% | 70.1% | 4.3% | 2.6% | no | ev_below_threshold |
| Wyoming Cowboys at UNLV Rebels | UNLV Rebels | 70.9% | 66.9% | 4.0% | 2.3% | no | ev_below_threshold |
| North Carolina Tar Heels at UConn Huskies | North Carolina Tar Heels | 73.5% | 70.0% | 3.5% | 1.2% | no | ev_below_threshold |
| UL Monroe Warhawks at Arkansas State Red Wolves | Arkansas State Red Wolves | 87.0% | 83.9% | 3.1% | 0.4% | no | ev_below_threshold |
| Alabama Crimson Tide at LSU Tigers | Alabama Crimson Tide | 35.9% | 33.1% | 2.8% | 4.8% | yes | — |
| Fresno State Bulldogs at Utah State Aggies | Fresno State Bulldogs | 56.9% | 54.3% | 2.6% | 1.3% | no | ev_below_threshold |
| Duke Blue Devils at NC State Wolfpack | Duke Blue Devils | 65.9% | 63.5% | 2.5% | 1.0% | no | ev_below_threshold |
| Northern Illinois Huskies at San Jose State Spartans | San Jose State Spartans | 78.9% | 76.5% | 2.4% | -0.6% | no | ev_below_threshold |
| Maryland Terrapins at Purdue Boilermakers | Purdue Boilermakers | 69.7% | 67.4% | 2.3% | 2.1% | no | ev_below_threshold |
| Boise State Broncos at Colorado State Rams | Boise State Broncos | 89.1% | 86.9% | 2.2% | -1.0% | no | ev_below_threshold |
| UCF Knights at Kansas Jayhawks | Kansas Jayhawks | 58.5% | 56.3% | 2.1% | 0.8% | no | ev_below_threshold |
| Iowa State Cyclones at Baylor Bears | Baylor Bears | 77.3% | 75.5% | 1.8% | -1.6% | no | ev_below_threshold |
| Marshall Thundering Herd at Georgia Southern Eagles | Georgia Southern Eagles | 78.3% | 76.5% | 1.8% | -1.3% | no | ev_below_threshold |
| Cincinnati Bearcats at Houston Cougars | Houston Cougars | 80.1% | 78.3% | 1.7% | -0.4% | no | ev_below_threshold |
| Georgia State Panthers at Appalachian State Mountaineers | Georgia State Panthers | 37.0% | 35.3% | 1.7% | 2.6% | no | ev_below_threshold |
| Nebraska Cornhuskers at Illinois Fighting Illini | Nebraska Cornhuskers | 65.1% | 63.4% | 1.7% | 0.3% | no | ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

