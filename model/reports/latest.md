# NCAA football moneyline research card

Snapshot: 2026-10-11T10:38:22Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 4

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Penn State Nittany Lions at Michigan Wolverines | Penn State Nittany Lions | +205 (fanduel) | 37.7% | 33.3% | 15.1% | 0.50% |
| Notre Dame Fighting Irish at BYU Cougars | BYU Cougars | +410 (betrivers) | 21.1% | 19.6% | 7.5% | 0.18% |
| Missouri Tigers at Ole Miss Rebels | Missouri Tigers | +188 (fanduel) | 36.9% | 33.3% | 6.2% | 0.33% |
| Kansas Jayhawks at Kansas State Wildcats | Kansas Jayhawks | +260 (draftkings) | 28.9% | 27.1% | 4.0% | 0.16% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| Pittsburgh Panthers at Boston College Eagles | Pittsburgh Panthers | 75.4% | 69.7% | 5.7% | 3.9% | no | too_few_books|ev_below_threshold |
| Arizona State Sun Devils at Texas Tech Red Raiders | Texas Tech Red Raiders | 85.6% | 80.3% | 5.3% | 2.0% | no | too_few_books|ev_below_threshold |
| Penn State Nittany Lions at Michigan Wolverines | Penn State Nittany Lions | 37.7% | 33.3% | 4.4% | 15.1% | yes | — |
| Florida Gators at Texas Longhorns | Texas Longhorns | 78.8% | 74.8% | 4.0% | 1.6% | no | ev_below_threshold |
| Oklahoma State Cowboys at Houston Cougars | Houston Cougars | 64.0% | 60.4% | 3.7% | 3.1% | no | ev_below_threshold |
| Missouri Tigers at Ole Miss Rebels | Missouri Tigers | 36.9% | 33.3% | 3.6% | 6.2% | yes | — |
| Appalachian State Mountaineers at Coastal Carolina Chanticleers | Appalachian State Mountaineers | 56.4% | 53.1% | 3.3% | 1.6% | no | too_few_books|ev_below_threshold |
| Fresno State Bulldogs at San Diego State Aztecs | San Diego State Aztecs | 29.3% | 26.6% | 2.7% | 5.4% | no | too_few_books |
| Ohio State Buckeyes at Indiana Hoosiers | Indiana Hoosiers | 39.6% | 36.9% | 2.7% | 3.0% | no | ev_below_threshold |
| Washington Huskies at Purdue Boilermakers | Washington Huskies | 45.1% | 42.6% | 2.6% | 1.5% | no | too_few_books|ev_below_threshold |
| Cincinnati Bearcats at West Virginia Mountaineers | Cincinnati Bearcats | 48.1% | 45.6% | 2.5% | 1.0% | no | too_few_books|ev_below_threshold |
| Western Kentucky Hilltoppers at Sam Houston State Bearkats | Sam Houston State Bearkats | 48.9% | 46.4% | 2.4% | 3.6% | no | ev_below_threshold |
| Georgia Southern Eagles at Old Dominion Monarchs | Georgia Southern Eagles | 58.5% | 56.1% | 2.4% | -0.2% | no | too_few_books|ev_below_threshold |
| Northwestern Wildcats at Michigan State Spartans | Northwestern Wildcats | 75.7% | 73.4% | 2.3% | -1.4% | no | too_few_books|ev_below_threshold |
| Nebraska Cornhuskers at Oregon Ducks | Nebraska Cornhuskers | 21.5% | 19.6% | 1.9% | 7.3% | no | market_dispersion_high |
| Kansas Jayhawks at Kansas State Wildcats | Kansas Jayhawks | 28.9% | 27.1% | 1.8% | 4.0% | yes | — |
| North Carolina Tar Heels at Duke Blue Devils | Duke Blue Devils | 60.0% | 58.3% | 1.7% | -1.2% | no | ev_below_threshold |
| Virginia Cavaliers at SMU Mustangs | Virginia Cavaliers | 28.9% | 27.3% | 1.6% | 1.2% | no | too_few_books|ev_below_threshold |
| Notre Dame Fighting Irish at BYU Cougars | BYU Cougars | 21.1% | 19.6% | 1.5% | 7.5% | yes | — |
| Memphis Tigers at Tulane Green Wave | Tulane Green Wave | 34.4% | 33.0% | 1.4% | -0.2% | no | too_few_books|edge_below_threshold|ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

