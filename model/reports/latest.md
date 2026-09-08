# NCAA football moneyline research card

Snapshot: 2026-09-08T14:17:45Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 5

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Buffalo Bulls at Florida International Panthers | Buffalo Bulls | +360 (betrivers) | 25.8% | 21.8% | 18.7% | 0.50% |
| Middle Tennessee Blue Raiders at Marshall Thundering Herd | Middle Tennessee Blue Raiders | +475 (caesars) | 20.5% | 17.0% | 17.8% | 0.37% |
| San Diego State Aztecs at UCLA Bruins | San Diego State Aztecs | +390 (fanduel) | 22.5% | 20.2% | 10.4% | 0.27% |
| California Golden Bears at Syracuse Orange | Syracuse Orange | -156 (fanduel) | 64.3% | 59.5% | 5.5% | 0.50% |
| Appalachian State Mountaineers at East Carolina Pirates | Appalachian State Mountaineers | +255 (betrivers) | 29.7% | 27.8% | 5.3% | 0.21% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| California Golden Bears at Syracuse Orange | Syracuse Orange | 64.3% | 59.5% | 4.8% | 5.5% | yes | — |
| Montana State Bobcats at Nevada Wolf Pack | Nevada Wolf Pack | 40.9% | 36.4% | 4.5% | 8.4% | no | too_few_books |
| Navy Midshipmen at Florida Atlantic Owls | Navy Midshipmen | 68.1% | 63.8% | 4.3% | 3.5% | no | ev_below_threshold |
| Buffalo Bulls at Florida International Panthers | Buffalo Bulls | 25.8% | 21.8% | 4.0% | 18.7% | yes | — |
| Middle Tennessee Blue Raiders at Marshall Thundering Herd | Middle Tennessee Blue Raiders | 20.5% | 17.0% | 3.5% | 17.8% | yes | — |
| Wofford Terriers at Kent State Golden Flashes | Wofford Terriers | 19.8% | 17.0% | 2.8% | 10.8% | no | too_few_books |
| San Diego State Aztecs at UCLA Bruins | San Diego State Aztecs | 22.5% | 20.2% | 2.3% | 10.4% | yes | — |
| Appalachian State Mountaineers at East Carolina Pirates | Appalachian State Mountaineers | 29.7% | 27.8% | 1.9% | 5.3% | yes | — |
| UTSA Roadrunners at Texas State Bobcats | UTSA Roadrunners | 49.9% | 48.1% | 1.8% | 0.3% | no | ev_below_threshold |
| Alabama Crimson Tide at Kentucky Wildcats | Alabama Crimson Tide | 78.7% | 76.9% | 1.8% | -1.1% | no | ev_below_threshold |
| Ohio State Buckeyes at Texas Longhorns | Texas Longhorns | 53.5% | 51.7% | 1.7% | -0.8% | no | ev_below_threshold |
| Mississippi State Bulldogs at Minnesota Golden Gophers | Mississippi State Bulldogs | 53.6% | 51.9% | 1.7% | 0.2% | no | ev_below_threshold |
| Colgate Raiders at Central Michigan Chippewas | Colgate Raiders | 8.3% | 6.9% | 1.5% | 16.8% | no | too_few_books|edge_below_threshold |
| Southern Utah Thunderbirds at Colorado State Rams | Southern Utah Thunderbirds | 10.8% | 9.4% | 1.4% | 9.8% | no | too_few_books|edge_below_threshold |
| New Mexico State Aggies at Hawai'i Warriors | Hawai'i Warriors | 76.0% | 74.7% | 1.3% | -1.7% | no | edge_below_threshold|ev_below_threshold |
| Arizona Wildcats at BYU Cougars | BYU Cougars | 72.2% | 71.0% | 1.3% | -1.5% | no | edge_below_threshold|ev_below_threshold |
| UNLV Rebels at North Texas Mean Green | UNLV Rebels | 63.3% | 62.1% | 1.3% | -1.8% | no | edge_below_threshold|ev_below_threshold |
| Maryland Terrapins at UConn Huskies | UConn Huskies | 21.2% | 20.0% | 1.2% | 3.0% | no | edge_below_threshold|ev_below_threshold |
| Arizona State Sun Devils at Texas A&M Aggies | Texas A&M Aggies | 84.6% | 83.4% | 1.2% | -1.8% | no | edge_below_threshold|ev_below_threshold |
| UCF Knights at Pittsburgh Panthers | Pittsburgh Panthers | 71.4% | 70.3% | 1.1% | -2.1% | no | edge_below_threshold|ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

