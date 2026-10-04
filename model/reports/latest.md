# NCAA football moneyline research card

Snapshot: 2026-10-04T10:37:26Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 4

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Indiana Hoosiers at Nebraska Cornhuskers | Nebraska Cornhuskers | +310 (betrivers) | 27.9% | 26.2% | 14.3% | 0.46% |
| Iowa Hawkeyes at Washington Huskies | Iowa Hawkeyes | +105 (fanduel) | 52.1% | 46.8% | 6.9% | 0.50% |
| Jacksonville State Gamecocks at Kennesaw State Owls | Kennesaw State Owls | +150 (draftkings) | 42.3% | 40.2% | 5.8% | 0.39% |
| Southern Miss Golden Eagles at Troy Trojans | Southern Miss Golden Eagles | +285 (fanduel) | 27.5% | 24.9% | 5.7% | 0.20% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| North Carolina Tar Heels at Pittsburgh Panthers | Pittsburgh Panthers | 65.3% | 59.1% | 6.2% | 5.7% | no | too_few_books |
| Iowa Hawkeyes at Washington Huskies | Iowa Hawkeyes | 52.1% | 46.8% | 5.4% | 6.9% | yes | — |
| Syracuse Orange at Virginia Cavaliers | Virginia Cavaliers | 74.0% | 69.1% | 4.9% | 2.5% | no | too_few_books|ev_below_threshold |
| Kansas Jayhawks at Utah Utes | Utah Utes | 87.2% | 82.6% | 4.6% | 1.0% | no | too_few_books|ev_below_threshold |
| Texas A&M Aggies at Missouri Tigers | Texas A&M Aggies | 48.2% | 43.7% | 4.6% | 11.8% | no | market_dispersion_high |
| USC Trojans at Penn State Nittany Lions | Penn State Nittany Lions | 50.3% | 46.9% | 3.5% | 3.2% | no | market_dispersion_high|ev_below_threshold |
| Texas Longhorns at Oklahoma Sooners | Texas Longhorns | 76.7% | 73.4% | 3.3% | 1.0% | no | market_dispersion_high|ev_below_threshold |
| Tulsa Golden Hurricane at Navy Midshipmen | Tulsa Golden Hurricane | 42.7% | 39.6% | 3.1% | 5.9% | no | too_few_books |
| Arizona Wildcats at West Virginia Mountaineers | West Virginia Mountaineers | 45.3% | 42.6% | 2.8% | 2.0% | no | too_few_books|ev_below_threshold |
| UCF Knights at Oklahoma State Cowboys | UCF Knights | 28.6% | 25.8% | 2.8% | 5.9% | no | too_few_books |
| San Diego State Aztecs at Oregon State Beavers | San Diego State Aztecs | 18.8% | 16.2% | 2.6% | 11.2% | no | too_few_books |
| Southern Miss Golden Eagles at Troy Trojans | Southern Miss Golden Eagles | 27.5% | 24.9% | 2.6% | 5.7% | yes | — |
| Virginia Tech Hokies at California Golden Bears | California Golden Bears | 22.3% | 19.7% | 2.6% | 8.3% | no | too_few_books |
| South Florida Bulls at UTSA Roadrunners | South Florida Bulls | 31.5% | 29.2% | 2.3% | 3.9% | no | too_few_books|ev_below_threshold |
| Jacksonville State Gamecocks at Kennesaw State Owls | Kennesaw State Owls | 42.3% | 40.2% | 2.1% | 5.8% | yes | — |
| Iowa State Cyclones at BYU Cougars | BYU Cougars | 80.3% | 78.3% | 2.0% | -0.8% | no | market_dispersion_high|ev_below_threshold |
| UCLA Bruins at Oregon Ducks | Oregon Ducks | 81.1% | 79.3% | 1.8% | -0.1% | no | ev_below_threshold |
| Duke Blue Devils at Georgia Tech Yellow Jackets | Duke Blue Devils | 70.4% | 68.7% | 1.8% | -1.9% | no | too_few_books|ev_below_threshold |
| Illinois Fighting Illini at Michigan State Spartans | Michigan State Spartans | 42.5% | 40.9% | 1.6% | -0.5% | no | too_few_books|ev_below_threshold |
| Indiana Hoosiers at Nebraska Cornhuskers | Nebraska Cornhuskers | 27.9% | 26.2% | 1.6% | 14.3% | yes | — |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

