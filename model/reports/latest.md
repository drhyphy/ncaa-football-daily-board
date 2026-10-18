# NCAA football moneyline research card

Snapshot: 2026-10-18T10:32:34Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 2

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| UMass Minutemen at UConn Huskies | UMass Minutemen | +550 (draftkings) | 16.4% | 14.8% | 6.4% | 0.12% |
| James Madison Dukes at Appalachian State Mountaineers | James Madison Dukes | -330 (fanduel) | 79.9% | 77.7% | 4.1% | 0.50% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| North Dakota State Bison at New Mexico Lobos | New Mexico Lobos | 67.3% | 61.4% | 5.9% | 7.9% | no | too_few_books |
| Iowa Hawkeyes at Minnesota Golden Gophers | Iowa Hawkeyes | 69.8% | 64.5% | 5.3% | 7.5% | no | too_few_books|market_dispersion_high |
| South Alabama Jaguars at Marshall Thundering Herd | South Alabama Jaguars | 62.3% | 58.0% | 4.2% | 2.7% | no | ev_below_threshold |
| Ole Miss Rebels at Texas Longhorns | Texas Longhorns | 61.8% | 57.6% | 4.2% | 4.1% | no | too_few_books |
| Kansas State Wildcats at Arizona State Sun Devils | Kansas State Wildcats | 58.6% | 54.4% | 4.1% | 2.9% | no | too_few_books|ev_below_threshold |
| West Virginia Mountaineers at TCU Horned Frogs | TCU Horned Frogs | 71.9% | 68.0% | 3.9% | 0.7% | no | too_few_books|ev_below_threshold |
| Indiana Hoosiers at Michigan Wolverines | Indiana Hoosiers | 76.7% | 74.0% | 2.6% | 0.6% | no | too_few_books|ev_below_threshold |
| Air Force Falcons at Wyoming Cowboys | Air Force Falcons | 74.6% | 72.0% | 2.6% | -0.5% | no | too_few_books|ev_below_threshold |
| James Madison Dukes at Appalachian State Mountaineers | James Madison Dukes | 79.9% | 77.7% | 2.2% | 4.1% | yes | — |
| Vanderbilt Commodores at Kentucky Wildcats | Kentucky Wildcats | 80.9% | 78.7% | 2.2% | -1.2% | no | too_few_books|ev_below_threshold |
| Baylor Bears at Kansas Jayhawks | Baylor Bears | 56.9% | 54.8% | 2.1% | -0.7% | no | too_few_books|ev_below_threshold |
| LSU Tigers at Auburn Tigers | LSU Tigers | 67.1% | 65.3% | 1.8% | -1.0% | no | too_few_books|ev_below_threshold |
| Virginia Tech Hokies at Clemson Tigers | Clemson Tigers | 51.7% | 49.9% | 1.7% | -0.5% | no | too_few_books|ev_below_threshold |
| Texas Tech Red Raiders at Cincinnati Bearcats | Texas Tech Red Raiders | 79.4% | 77.7% | 1.7% | -1.9% | no | too_few_books|ev_below_threshold |
| USC Trojans at Wisconsin Badgers | USC Trojans | 56.5% | 54.8% | 1.7% | -0.1% | no | too_few_books|ev_below_threshold |
| UMass Minutemen at UConn Huskies | UMass Minutemen | 16.4% | 14.8% | 1.6% | 6.4% | yes | — |
| Rutgers Scarlet Knights at Northwestern Wildcats | Northwestern Wildcats | 87.8% | 86.2% | 1.6% | -1.5% | no | too_few_books|ev_below_threshold |
| North Carolina State Wolfpack at Stanford Cardinal | North Carolina State Wolfpack | 72.4% | 71.0% | 1.5% | -1.5% | no | edge_below_threshold|ev_below_threshold |
| Duke Blue Devils at Virginia Cavaliers | Duke Blue Devils | 47.1% | 45.7% | 1.4% | -1.0% | no | edge_below_threshold|ev_below_threshold |
| Oregon Ducks at Illinois Fighting Illini | Illinois Fighting Illini | 19.7% | 18.4% | 1.3% | 2.3% | no | too_few_books|edge_below_threshold|ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

