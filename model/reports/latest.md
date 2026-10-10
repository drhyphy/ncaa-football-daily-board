# NCAA football moneyline research card

Snapshot: 2026-10-10T10:36:32Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 6

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| UCF Knights at Oklahoma State Cowboys | UCF Knights | +350 (draftkings) | 26.2% | 22.2% | 17.9% | 0.50% |
| San Diego State Aztecs at Oregon State Beavers | San Diego State Aztecs | +580 (fanduel) | 16.6% | 14.8% | 12.6% | 0.22% |
| Coastal Carolina Chanticleers at Marshall Thundering Herd | Coastal Carolina Chanticleers | +170 (betrivers) | 41.4% | 37.8% | 11.8% | 0.50% |
| North Dakota State Bison at UNLV Rebels | UNLV Rebels | +135 (betmgm) | 46.8% | 44.4% | 9.9% | 0.50% |
| South Carolina Gamecocks at Florida Gators | South Carolina Gamecocks | +370 (caesars) | 22.5% | 20.8% | 5.8% | 0.16% |
| Texas A&M Aggies at Missouri Tigers | Texas A&M Aggies | +150 (draftkings) | 41.7% | 39.4% | 4.2% | 0.28% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| Texas Longhorns at Oklahoma Sooners | Texas Longhorns | 76.8% | 72.6% | 4.2% | 2.3% | no | ev_below_threshold |
| North Carolina Tar Heels at Pittsburgh Panthers | Pittsburgh Panthers | 65.7% | 61.7% | 4.0% | 3.3% | no | ev_below_threshold |
| UCF Knights at Oklahoma State Cowboys | UCF Knights | 26.2% | 22.2% | 4.0% | 17.9% | yes | — |
| Coastal Carolina Chanticleers at Marshall Thundering Herd | Coastal Carolina Chanticleers | 41.4% | 37.8% | 3.7% | 11.8% | yes | — |
| Miami (OH) RedHawks at UMass Minutemen | UMass Minutemen | 39.9% | 36.3% | 3.6% | 9.6% | no | market_dispersion_high |
| UAB Blazers at Memphis Tigers | Memphis Tigers | 85.9% | 82.7% | 3.2% | 0.3% | no | ev_below_threshold |
| Kent State Golden Flashes at Western Michigan Broncos | Western Michigan Broncos | 85.4% | 82.6% | 2.8% | -0.4% | no | ev_below_threshold |
| Central Michigan Chippewas at Ohio Bobcats | Ohio Bobcats | 56.8% | 54.2% | 2.6% | 0.5% | no | ev_below_threshold |
| USC Trojans at Penn State Nittany Lions | Penn State Nittany Lions | 55.8% | 53.1% | 2.6% | 2.2% | no | ev_below_threshold |
| UCLA Bruins at Oregon Ducks | Oregon Ducks | 79.8% | 77.3% | 2.4% | -0.8% | no | ev_below_threshold |
| North Dakota State Bison at UNLV Rebels | UNLV Rebels | 46.8% | 44.4% | 2.4% | 9.9% | yes | — |
| Texas A&M Aggies at Missouri Tigers | Texas A&M Aggies | 41.7% | 39.4% | 2.3% | 4.2% | yes | — |
| Nevada Wolf Pack at UTEP Miners | Nevada Wolf Pack | 78.0% | 75.7% | 2.2% | 0.2% | no | ev_below_threshold |
| James Madison Dukes at Georgia Southern Eagles | James Madison Dukes | 74.6% | 72.4% | 2.2% | 0.8% | no | ev_below_threshold |
| Rice Owls at East Carolina Pirates | East Carolina Pirates | 78.1% | 75.9% | 2.1% | -1.1% | no | ev_below_threshold |
| Wake Forest Demon Deacons at North Carolina State Wolfpack | Wake Forest Demon Deacons | 62.4% | 60.4% | 2.1% | 1.0% | no | ev_below_threshold |
| Tennessee Volunteers at Arkansas Razorbacks | Tennessee Volunteers | 82.9% | 80.9% | 1.9% | -1.4% | no | ev_below_threshold |
| Sacramento State Hornets at Bowling Green Falcons | Bowling Green Falcons | 75.1% | 73.2% | 1.9% | 0.1% | no | ev_below_threshold |
| San Diego State Aztecs at Oregon State Beavers | San Diego State Aztecs | 16.6% | 14.8% | 1.7% | 12.6% | yes | — |
| South Carolina Gamecocks at Florida Gators | South Carolina Gamecocks | 22.5% | 20.8% | 1.7% | 5.8% | yes | — |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

