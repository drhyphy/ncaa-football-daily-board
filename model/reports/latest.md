# NCAA football moneyline research card

Snapshot: 2026-09-01T11:56:45Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 2

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Toledo Rockets at Michigan State Spartans | Toledo Rockets | +320 (betrivers) | 25.9% | 23.8% | 8.7% | 0.27% |
| Tulane Green Wave at Duke Blue Devils | Tulane Green Wave | +265 (bovada) | 29.5% | 27.4% | 7.7% | 0.29% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| Alcorn State Braves at Southern Mississippi Golden Eagles | Southern Mississippi Golden Eagles | 93.1% | 90.3% | 2.8% | 0.0% | no | ev_below_threshold |
| Ohio State Buckeyes at Indiana Hoosiers | Ohio State Buckeyes | 54.6% | 52.0% | 2.6% | 0.8% | no | too_few_books|ev_below_threshold |
| UCLA Bruins at California Golden Bears | California Golden Bears | 49.2% | 46.8% | 2.3% | 3.2% | no | ev_below_threshold |
| Tulane Green Wave at Duke Blue Devils | Tulane Green Wave | 29.5% | 27.4% | 2.1% | 7.7% | yes | — |
| LSU Tigers at Ole Miss Rebels | LSU Tigers | 48.0% | 46.0% | 2.1% | -0.1% | no | too_few_books|ev_below_threshold |
| Toledo Rockets at Michigan State Spartans | Toledo Rockets | 25.9% | 23.8% | 2.1% | 8.7% | yes | — |
| Colorado Buffaloes at Georgia Tech Yellow Jackets | Colorado Buffaloes | 33.2% | 31.1% | 2.1% | 2.8% | no | ev_below_threshold |
| UNLV Rebels at Hawaii Rainbow Warriors | Hawaii Rainbow Warriors | 45.9% | 43.8% | 2.1% | 3.2% | no | ev_below_threshold |
| Idaho State Bengals at Utah State Aggies | Utah State Aggies | 83.2% | 81.6% | 1.6% | -1.9% | no | ev_below_threshold |
| Michigan Wolverines at Ohio State Buckeyes | Ohio State Buckeyes | 83.0% | 81.6% | 1.4% | -1.3% | no | too_few_books|edge_below_threshold|ev_below_threshold |
| Maine Black Bears at Appalachian State Mountaineers | Appalachian State Mountaineers | 89.1% | 87.7% | 1.4% | -2.4% | no | edge_below_threshold|ev_below_threshold |
| Texas Longhorns at Oklahoma Sooners | Texas Longhorns | 67.8% | 66.4% | 1.4% | -1.4% | no | too_few_books|edge_below_threshold|ev_below_threshold |
| Rhode Island Rams at Temple Owls | Temple Owls | 79.5% | 78.3% | 1.3% | -2.8% | no | edge_below_threshold|ev_below_threshold |
| San Jose State Spartans at Eastern Michigan Eagles | San Jose State Spartans | 42.7% | 41.4% | 1.3% | 0.2% | no | edge_below_threshold|ev_below_threshold |
| Central Michigan Chippewas at New Mexico Lobos | New Mexico Lobos | 78.2% | 77.0% | 1.2% | -2.2% | no | edge_below_threshold|ev_below_threshold |
| UT Rio Grande Valley Vaqueros at UTSA Roadrunners | UT Rio Grande Valley Vaqueros | 5.3% | 4.2% | 1.2% | 38.8% | no | too_few_books|edge_below_threshold |
| South Dakota State Jackrabbits at Northwestern Wildcats | South Dakota State Jackrabbits | 19.1% | 18.0% | 1.1% | 7.0% | no | too_few_books|edge_below_threshold |
| Boston College Eagles at Cincinnati Bearcats | Cincinnati Bearcats | 73.1% | 72.1% | 1.0% | -0.8% | no | edge_below_threshold|ev_below_threshold |
| Georgia Bulldogs at Arkansas Razorbacks | Georgia Bulldogs | 86.9% | 85.9% | 1.0% | -3.2% | no | too_few_books|edge_below_threshold|ev_below_threshold |
| Western Kentucky Hilltoppers at Nevada Wolf Pack | Western Kentucky Hilltoppers | 56.3% | 55.3% | 1.0% | -2.1% | no | edge_below_threshold|ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

