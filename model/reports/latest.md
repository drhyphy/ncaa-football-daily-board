# NCAA football moneyline research card

Snapshot: 2026-08-31T14:42:41Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 4

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Tulane Green Wave at Duke Blue Devils | Tulane Green Wave | +300 (draftkings) | 27.5% | 25.0% | 9.9% | 0.33% |
| Toledo Rockets at Michigan State Spartans | Toledo Rockets | +340 (betrivers) | 24.5% | 22.2% | 7.9% | 0.23% |
| Colorado Buffaloes at Georgia Tech Yellow Jackets | Colorado Buffaloes | +220 (draftkings) | 33.6% | 31.6% | 7.4% | 0.34% |
| UNLV Rebels at Hawaii Rainbow Warriors | Hawaii Rainbow Warriors | +135 (lowvig) | 44.3% | 42.3% | 4.2% | 0.31% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| Ohio State Buckeyes at Indiana Hoosiers | Ohio State Buckeyes | 54.6% | 52.0% | 2.6% | 0.8% | no | too_few_books|ev_below_threshold |
| Tulane Green Wave at Duke Blue Devils | Tulane Green Wave | 27.5% | 25.0% | 2.5% | 9.9% | yes | — |
| Toledo Rockets at Michigan State Spartans | Toledo Rockets | 24.5% | 22.2% | 2.3% | 7.9% | yes | — |
| UCLA Bruins at California Golden Bears | California Golden Bears | 49.2% | 46.9% | 2.3% | 0.9% | no | ev_below_threshold |
| LSU Tigers at Ole Miss Rebels | LSU Tigers | 48.0% | 46.0% | 2.1% | -0.1% | no | too_few_books|ev_below_threshold |
| UNLV Rebels at Hawaii Rainbow Warriors | Hawaii Rainbow Warriors | 44.3% | 42.3% | 2.0% | 4.2% | yes | — |
| Colorado Buffaloes at Georgia Tech Yellow Jackets | Colorado Buffaloes | 33.6% | 31.6% | 2.0% | 7.4% | yes | — |
| Idaho State Bengals at Utah State Aggies | Utah State Aggies | 82.9% | 81.2% | 1.8% | -2.0% | no | ev_below_threshold |
| Rhode Island Rams at Temple Owls | Temple Owls | 80.5% | 78.8% | 1.7% | -2.1% | no | ev_below_threshold |
| SMU Mustangs at Florida State Seminoles | Florida State Seminoles | 42.4% | 40.8% | 1.6% | 3.8% | no | ev_below_threshold |
| Maine Black Bears at Appalachian State Mountaineers | Appalachian State Mountaineers | 90.1% | 88.6% | 1.5% | 1.4% | no | ev_below_threshold |
| Alcorn State Braves at Southern Mississippi Golden Eagles | Southern Mississippi Golden Eagles | 95.1% | 93.6% | 1.5% | -1.5% | no | edge_below_threshold|ev_below_threshold |
| Michigan Wolverines at Ohio State Buckeyes | Ohio State Buckeyes | 83.0% | 81.6% | 1.4% | -1.3% | no | too_few_books|edge_below_threshold|ev_below_threshold |
| Texas Longhorns at Oklahoma Sooners | Texas Longhorns | 67.8% | 66.4% | 1.4% | -1.4% | no | too_few_books|edge_below_threshold|ev_below_threshold |
| UT Rio Grande Valley Vaqueros at UTSA Roadrunners | UT Rio Grande Valley Vaqueros | 5.1% | 4.0% | 1.2% | 33.7% | no | too_few_books|edge_below_threshold |
| Central Michigan Chippewas at New Mexico Lobos | New Mexico Lobos | 78.6% | 77.5% | 1.1% | -2.4% | no | edge_below_threshold|ev_below_threshold |
| West Georgia Wolves at Kennesaw State Owls | West Georgia Wolves | 6.8% | 5.8% | 1.0% | 43.1% | no | too_few_books|edge_below_threshold |
| Boston College Eagles at Cincinnati Bearcats | Cincinnati Bearcats | 73.1% | 72.1% | 1.0% | -1.6% | no | edge_below_threshold|ev_below_threshold |
| Georgia Bulldogs at Arkansas Razorbacks | Georgia Bulldogs | 86.9% | 85.9% | 1.0% | -3.2% | no | too_few_books|edge_below_threshold|ev_below_threshold |
| Arkansas State Red Wolves at Memphis Tigers | Arkansas State Red Wolves | 24.4% | 23.4% | 1.0% | 1.4% | no | edge_below_threshold|ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

