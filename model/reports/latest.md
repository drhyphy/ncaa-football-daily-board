# NCAA football moneyline research card

Snapshot: 2026-11-04T18:45:06Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 4

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Texas A&M Aggies at South Carolina Gamecocks | Texas A&M Aggies | +230 (caesars) | 34.0% | 29.5% | 12.1% | 0.50% |
| Vanderbilt Commodores at Mississippi State Bulldogs | Mississippi State Bulldogs | -145 (betmgm) | 62.6% | 57.4% | 5.7% | 0.50% |
| Ball State Cardinals at UMass Minutemen | UMass Minutemen | -140 (fanduel) | 61.6% | 56.5% | 5.6% | 0.50% |
| Alabama Crimson Tide at LSU Tigers | Alabama Crimson Tide | +188 (betrivers) | 36.3% | 33.6% | 4.5% | 0.24% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| Vanderbilt Commodores at Mississippi State Bulldogs | Mississippi State Bulldogs | 62.6% | 57.4% | 5.1% | 5.7% | yes | — |
| Ball State Cardinals at UMass Minutemen | UMass Minutemen | 61.6% | 56.5% | 5.1% | 5.6% | yes | — |
| Texas Longhorns at Missouri Tigers | Texas Longhorns | 61.0% | 56.3% | 4.6% | 3.9% | no | ev_below_threshold |
| Texas A&M Aggies at South Carolina Gamecocks | Texas A&M Aggies | 34.0% | 29.5% | 4.5% | 12.1% | yes | — |
| Wyoming Cowboys at UNLV Rebels | UNLV Rebels | 70.9% | 66.9% | 4.0% | 1.7% | no | ev_below_threshold |
| Oregon Ducks at Ohio State Buckeyes | Ohio State Buckeyes | 75.5% | 71.7% | 3.8% | 2.0% | no | ev_below_threshold |
| North Carolina Tar Heels at UConn Huskies | North Carolina Tar Heels | 73.4% | 69.8% | 3.6% | 2.8% | no | ev_below_threshold |
| UL-Monroe Warhawks at Arkansas State Red Wolves | Arkansas State Red Wolves | 87.1% | 84.0% | 3.1% | 0.4% | no | ev_below_threshold |
| Alabama Crimson Tide at LSU Tigers | Alabama Crimson Tide | 36.3% | 33.6% | 2.7% | 4.5% | yes | — |
| Duke Blue Devils at North Carolina State Wolfpack | Duke Blue Devils | 65.6% | 63.0% | 2.6% | 0.5% | no | ev_below_threshold |
| Fresno State Bulldogs at Utah State Aggies | Fresno State Bulldogs | 57.0% | 54.4% | 2.6% | 1.5% | no | ev_below_threshold |
| Maryland Terrapins at Purdue Boilermakers | Purdue Boilermakers | 69.2% | 66.6% | 2.6% | -0.1% | no | ev_below_threshold |
| Northern Illinois Huskies at San Jose State Spartans | San Jose State Spartans | 78.9% | 76.6% | 2.3% | -0.6% | no | ev_below_threshold |
| Boise State Broncos at Colorado State Rams | Boise State Broncos | 89.2% | 87.0% | 2.1% | -0.9% | no | ev_below_threshold |
| Penn State Nittany Lions at Washington Huskies | Penn State Nittany Lions | 47.4% | 45.3% | 2.1% | 1.5% | no | ev_below_threshold |
| Florida State Seminoles at Boston College Eagles | Florida State Seminoles | 70.9% | 69.1% | 1.9% | 1.8% | no | ev_below_threshold |
| UCF Knights at Kansas Jayhawks | Kansas Jayhawks | 59.1% | 57.2% | 1.8% | -0.5% | no | ev_below_threshold |
| UTSA Roadrunners at Florida Atlantic Owls | UTSA Roadrunners | 70.7% | 68.9% | 1.8% | -1.0% | no | ev_below_threshold |
| Cincinnati Bearcats at Houston Cougars | Houston Cougars | 80.0% | 78.2% | 1.8% | -0.9% | no | ev_below_threshold |
| Georgia State Panthers at Appalachian State Mountaineers | Georgia State Panthers | 36.7% | 34.9% | 1.8% | 2.9% | no | ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

