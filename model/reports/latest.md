# NCAA football moneyline research card

Snapshot: 2026-10-25T14:28:00Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 5

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Auburn Tigers at Ole Miss Rebels | Auburn Tigers | +390 (fanduel) | 23.6% | 21.9% | 15.7% | 0.40% |
| Kent State Golden Flashes at Sacramento State Hornets | Sacramento State Hornets | +350 (betrivers) | 25.0% | 22.3% | 12.4% | 0.35% |
| Kennesaw State Owls at Middle Tennessee Blue Raiders | Kennesaw State Owls | +116 (betrivers) | 50.3% | 44.5% | 8.5% | 0.50% |
| SMU Mustangs at Syracuse Orange | Syracuse Orange | +295 (betrivers) | 27.4% | 25.5% | 8.1% | 0.28% |
| Arizona Wildcats at Texas Tech Red Raiders | Texas Tech Red Raiders | -175 (draftkings) | 68.6% | 63.0% | 7.8% | 0.50% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| Kennesaw State Owls at Middle Tennessee Blue Raiders | Kennesaw State Owls | 50.3% | 44.5% | 5.7% | 8.5% | yes | — |
| Arizona Wildcats at Texas Tech Red Raiders | Texas Tech Red Raiders | 68.6% | 63.0% | 5.7% | 7.8% | yes | — |
| Northwestern Wildcats at Oregon Ducks | Oregon Ducks | 66.5% | 61.6% | 4.9% | 3.9% | no | ev_below_threshold |
| Oklahoma State Cowboys at Iowa State Cyclones | Iowa State Cyclones | 29.8% | 25.2% | 4.6% | 13.2% | no | too_few_books |
| Washington Huskies at Nebraska Cornhuskers | Nebraska Cornhuskers | 79.1% | 74.8% | 4.3% | 3.5% | no | ev_below_threshold |
| Boston College Eagles at Duke Blue Devils | Duke Blue Devils | 75.2% | 71.4% | 3.8% | 2.6% | no | too_few_books|ev_below_threshold |
| Ohio State Buckeyes at USC Trojans | Ohio State Buckeyes | 70.8% | 67.3% | 3.4% | 2.2% | no | ev_below_threshold |
| Baylor Bears at UCF Knights | Baylor Bears | 47.8% | 44.4% | 3.3% | 3.1% | no | ev_below_threshold |
| Utah Utes at Cincinnati Bearcats | Utah Utes | 71.6% | 68.3% | 3.3% | 1.7% | no | too_few_books|ev_below_threshold |
| Arizona State Sun Devils at BYU Cougars | BYU Cougars | 87.5% | 84.3% | 3.2% | 2.1% | no | ev_below_threshold |
| Georgia Tech Yellow Jackets at Pittsburgh Panthers | Pittsburgh Panthers | 73.3% | 70.1% | 3.2% | -0.0% | no | too_few_books|ev_below_threshold |
| Purdue Boilermakers at Penn State Nittany Lions | Penn State Nittany Lions | 75.5% | 72.6% | 2.9% | -0.2% | no | too_few_books|ev_below_threshold |
| Tulane Green Wave at Charlotte 49ers | Tulane Green Wave | 84.1% | 81.4% | 2.8% | -0.2% | no | too_few_books|ev_below_threshold |
| Stanford Cardinal at Louisville Cardinals | Louisville Cardinals | 93.8% | 91.1% | 2.7% | -1.5% | no | too_few_books|ev_below_threshold |
| Kent State Golden Flashes at Sacramento State Hornets | Sacramento State Hornets | 25.0% | 22.3% | 2.7% | 12.4% | yes | — |
| Florida Atlantic Owls at North Texas Mean Green | North Texas Mean Green | 81.6% | 79.1% | 2.5% | -0.3% | no | ev_below_threshold |
| Kansas Jayhawks at TCU Horned Frogs | TCU Horned Frogs | 65.5% | 63.2% | 2.3% | -0.8% | no | too_few_books|ev_below_threshold |
| Wisconsin Badgers at Iowa Hawkeyes | Iowa Hawkeyes | 62.6% | 60.3% | 2.2% | 0.3% | no | too_few_books|ev_below_threshold |
| Minnesota Golden Gophers at Indiana Hoosiers | Indiana Hoosiers | 93.7% | 91.6% | 2.1% | -1.1% | no | too_few_books|ev_below_threshold |
| Oregon State Beavers at Fresno State Bulldogs | Fresno State Bulldogs | 32.3% | 30.4% | 1.9% | 3.4% | no | too_few_books|ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

