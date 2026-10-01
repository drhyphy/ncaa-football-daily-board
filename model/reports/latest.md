# NCAA football moneyline research card

Snapshot: 2026-10-01T10:36:45Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 9

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Texas State Bobcats at San Diego State Aztecs | San Diego State Aztecs | +235 (betrivers) | 34.6% | 29.7% | 16.1% | 0.50% |
| Cincinnati Bearcats at Arizona Wildcats | Cincinnati Bearcats | +220 (betrivers) | 34.6% | 31.1% | 10.8% | 0.49% |
| UCF Knights at Houston Cougars | UCF Knights | +385 (fanduel) | 22.8% | 21.0% | 10.8% | 0.28% |
| Pittsburgh Panthers at Virginia Tech Hokies | Pittsburgh Panthers | +143 (betonlineag) | 45.6% | 40.6% | 10.7% | 0.50% |
| Michigan State Spartans at Wisconsin Badgers | Michigan State Spartans | +320 (draftkings) | 26.1% | 23.7% | 9.8% | 0.31% |
| Fresno State Bulldogs at Washington State Cougars | Fresno State Bulldogs | +108 (betrivers) | 52.0% | 47.8% | 8.1% | 0.50% |
| Baylor Bears at Arizona State Sun Devils | Baylor Bears | +157 (betonlineag) | 41.9% | 37.8% | 7.7% | 0.49% |
| Ohio Bobcats at Kent State Golden Flashes | Ohio Bobcats | -160 (lowvig) | 65.2% | 59.6% | 5.9% | 0.50% |
| Liberty Flames at Delaware Blue Hens | Delaware Blue Hens | +250 (bovada) | 29.8% | 27.9% | 4.3% | 0.17% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| Ohio Bobcats at Kent State Golden Flashes | Ohio Bobcats | 65.2% | 59.6% | 5.5% | 5.9% | yes | — |
| Eastern Michigan Eagles at UMass Minutemen | UMass Minutemen | 72.6% | 67.4% | 5.2% | 3.5% | no | ev_below_threshold |
| Pittsburgh Panthers at Virginia Tech Hokies | Pittsburgh Panthers | 45.6% | 40.6% | 5.0% | 10.7% | yes | — |
| Texas State Bobcats at San Diego State Aztecs | San Diego State Aztecs | 34.6% | 29.7% | 4.9% | 16.1% | yes | — |
| Iowa Hawkeyes at Washington Huskies | Iowa Hawkeyes | 53.2% | 48.3% | 4.9% | 5.3% | no | too_few_books |
| USC Trojans at Penn State Nittany Lions | Penn State Nittany Lions | 55.4% | 51.1% | 4.3% | 3.5% | no | too_few_books|ev_below_threshold |
| Baylor Bears at Arizona State Sun Devils | Baylor Bears | 41.9% | 37.8% | 4.2% | 7.7% | yes | — |
| Fresno State Bulldogs at Washington State Cougars | Fresno State Bulldogs | 52.0% | 47.8% | 4.1% | 8.1% | yes | — |
| Cincinnati Bearcats at Arizona Wildcats | Cincinnati Bearcats | 34.6% | 31.1% | 3.5% | 10.8% | yes | — |
| Maryland Terrapins at Nebraska Cornhuskers | Nebraska Cornhuskers | 87.0% | 83.7% | 3.3% | 0.4% | no | ev_below_threshold |
| Texas A&M Aggies at Missouri Tigers | Texas A&M Aggies | 51.5% | 48.3% | 3.2% | 2.0% | no | too_few_books|ev_below_threshold |
| Michigan Wolverines at Minnesota Golden Gophers | Michigan Wolverines | 68.7% | 65.6% | 3.1% | 1.2% | no | ev_below_threshold |
| Old Dominion Monarchs at Georgia State Panthers | Georgia State Panthers | 58.1% | 55.1% | 2.9% | 3.4% | no | ev_below_threshold |
| San Jose State Spartans at Hawaii Rainbow Warriors | Hawaii Rainbow Warriors | 59.6% | 56.8% | 2.8% | 1.6% | no | ev_below_threshold |
| Southern Mississippi Golden Eagles at Troy Trojans | Southern Mississippi Golden Eagles | 27.3% | 24.6% | 2.7% | 12.0% | no | too_few_books |
| North Texas Mean Green at Tulsa Golden Hurricane | North Texas Mean Green | 53.0% | 50.4% | 2.6% | 1.6% | no | ev_below_threshold |
| UL Monroe Warhawks at South Alabama Jaguars | South Alabama Jaguars | 85.1% | 82.6% | 2.6% | -0.4% | no | ev_below_threshold |
| Washington Huskies at USC Trojans | USC Trojans | 78.5% | 75.9% | 2.6% | -0.6% | no | ev_below_threshold |
| Texas Tech Red Raiders at Colorado Buffaloes | Texas Tech Red Raiders | 81.9% | 79.4% | 2.5% | -0.9% | no | ev_below_threshold |
| Michigan State Spartans at Wisconsin Badgers | Michigan State Spartans | 26.1% | 23.7% | 2.5% | 9.8% | yes | — |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

