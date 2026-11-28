# NCAA football moneyline research card

Snapshot: 2026-11-28T19:09:22Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 4

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| UAB Blazers at North Texas Mean Green | North Texas Mean Green | -130 (betmgm) | 66.1% | 54.4% | 17.0% | 0.50% |
| South Carolina Gamecocks at Clemson Tigers | Clemson Tigers | +220 (draftkings) | 34.2% | 30.4% | 9.5% | 0.43% |
| Duke Blue Devils at Wake Forest Demon Deacons | Duke Blue Devils | +500 (betmgm) | 17.9% | 16.3% | 7.6% | 0.15% |
| USC Trojans at UCLA Bruins | UCLA Bruins | +166 (caesars) | 40.4% | 36.3% | 7.4% | 0.45% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| UAB Blazers at North Texas Mean Green | North Texas Mean Green | 66.1% | 54.4% | 11.7% | 17.0% | yes | — |
| Sacramento State Hornets at Hawai'i Warriors | Hawai'i Warriors | 86.6% | 81.8% | 4.8% | 2.3% | no | ev_below_threshold |
| USC Trojans at UCLA Bruins | UCLA Bruins | 40.4% | 36.3% | 4.1% | 7.4% | yes | — |
| South Carolina Gamecocks at Clemson Tigers | Clemson Tigers | 34.2% | 30.4% | 3.8% | 9.5% | yes | — |
| UTEP Miners at Northern Illinois Huskies | Northern Illinois Huskies | 68.0% | 65.3% | 2.7% | 0.4% | no | ev_below_threshold |
| SMU Mustangs at Stanford Cardinal | SMU Mustangs | 73.5% | 71.0% | 2.5% | 1.2% | no | ev_below_threshold |
| Penn State Nittany Lions at Maryland Terrapins | Penn State Nittany Lions | 76.5% | 74.1% | 2.5% | 1.6% | no | ev_below_threshold |
| UMass Minutemen at Bowling Green Falcons | UMass Minutemen | 41.9% | 39.6% | 2.3% | 1.5% | no | ev_below_threshold |
| Tennessee Volunteers at Vanderbilt Commodores | Tennessee Volunteers | 83.2% | 81.2% | 2.0% | -1.7% | no | ev_below_threshold |
| Virginia Cavaliers at Virginia Tech Hokies | Virginia Cavaliers | 47.5% | 45.7% | 1.8% | 0.7% | no | ev_below_threshold |
| Washington Huskies at Oregon Ducks | Oregon Ducks | 83.7% | 81.9% | 1.8% | -1.9% | no | ev_below_threshold |
| Michigan State Spartans at Rutgers Scarlet Knights | Michigan State Spartans | 56.3% | 54.5% | 1.7% | -0.5% | no | ev_below_threshold |
| Duke Blue Devils at Wake Forest Demon Deacons | Duke Blue Devils | 17.9% | 16.3% | 1.6% | 7.6% | yes | — |
| Auburn Tigers at Alabama Crimson Tide | Alabama Crimson Tide | 84.8% | 83.3% | 1.5% | -1.6% | no | ev_below_threshold |
| Arizona State Sun Devils at Arizona Wildcats | Arizona Wildcats | 74.5% | 73.0% | 1.5% | -0.7% | no | ev_below_threshold |
| Kansas Jayhawks at Oklahoma State Cowboys | Oklahoma State Cowboys | 67.6% | 66.4% | 1.3% | -1.6% | no | edge_below_threshold|ev_below_threshold |
| Nevada Wolf Pack at UNLV Rebels | UNLV Rebels | 65.0% | 63.9% | 1.2% | -1.4% | no | edge_below_threshold|ev_below_threshold |
| Boise State Broncos at Colorado State Rams | Boise State Broncos | 92.3% | 91.3% | 1.0% | -1.9% | no | edge_below_threshold|ev_below_threshold |
| Georgia Tech Yellow Jackets at Georgia Bulldogs | Georgia Bulldogs | 96.8% | 95.8% | 1.0% | -2.2% | no | too_few_books|edge_below_threshold|ev_below_threshold |
| Oregon State Beavers at Fresno State Bulldogs | Oregon State Beavers | 46.8% | 45.9% | 0.8% | -1.8% | no | edge_below_threshold|ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

