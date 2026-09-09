# NCAA football moneyline research card

Snapshot: 2026-09-09T11:07:59Z

Status: forward paper research only. Historical moneyline ROI has not been validated.

Leading specification: 75% of fitted FPI residual (alpha 21.0% in weeks 0–4; 29.2% in weeks 5+).

Qualified paper bets: 5

| Game | Selection | Best price | Model | Market | EV | Stake |
|---|---:|---:|---:|---:|---:|---:|
| Buffalo Bulls at Florida International Panthers | Buffalo Bulls | +350 (betrivers) | 26.1% | 22.1% | 17.3% | 0.49% |
| Middle Tennessee Blue Raiders at Marshall Thundering Herd | Middle Tennessee Blue Raiders | +425 (caesars) | 21.9% | 18.5% | 14.8% | 0.35% |
| Montana State Bobcats at Nevada Wolf Pack | Nevada Wolf Pack | +164 (draftkings) | 41.1% | 36.6% | 8.4% | 0.50% |
| San Diego State Aztecs at UCLA Bruins | San Diego State Aztecs | +385 (fanduel) | 22.3% | 19.9% | 8.2% | 0.21% |
| California Golden Bears at Syracuse Orange | Syracuse Orange | -159 (betrivers) | 64.4% | 59.5% | 4.9% | 0.50% |

## Highest model-vs-market disagreements

| Game | Side | Model | Market | Edge | EV | Eligible | Flags |
|---|---:|---:|---:|---:|---:|---:|---|
| California Golden Bears at Syracuse Orange | Syracuse Orange | 64.4% | 59.5% | 4.8% | 4.9% | yes | — |
| Montana State Bobcats at Nevada Wolf Pack | Nevada Wolf Pack | 41.1% | 36.6% | 4.5% | 8.4% | yes | — |
| Navy Midshipmen at Florida Atlantic Owls | Navy Midshipmen | 68.1% | 63.8% | 4.3% | 3.2% | no | ev_below_threshold |
| Buffalo Bulls at Florida International Panthers | Buffalo Bulls | 26.1% | 22.1% | 4.0% | 17.3% | yes | — |
| Middle Tennessee Blue Raiders at Marshall Thundering Herd | Middle Tennessee Blue Raiders | 21.9% | 18.5% | 3.3% | 14.8% | yes | — |
| Wofford Terriers at Kent State Golden Flashes | Wofford Terriers | 20.2% | 17.4% | 2.7% | 16.9% | no | too_few_books |
| New Mexico State Aggies at Hawai'i Warriors | Hawai'i Warriors | 72.7% | 70.3% | 2.4% | -0.4% | no | ev_below_threshold |
| San Diego State Aztecs at UCLA Bruins | San Diego State Aztecs | 22.3% | 19.9% | 2.4% | 8.2% | yes | — |
| Mississippi State Bulldogs at Minnesota Golden Gophers | Mississippi State Bulldogs | 52.4% | 50.3% | 2.0% | 0.9% | no | ev_below_threshold |
| UTSA Roadrunners at Texas State Bobcats | UTSA Roadrunners | 49.9% | 48.1% | 1.8% | 0.3% | no | ev_below_threshold |
| Alabama Crimson Tide at Kentucky Wildcats | Alabama Crimson Tide | 79.0% | 77.3% | 1.7% | -0.7% | no | ev_below_threshold |
| Appalachian State Mountaineers at East Carolina Pirates | Appalachian State Mountaineers | 30.9% | 29.2% | 1.7% | 3.4% | no | ev_below_threshold |
| Ohio State Buckeyes at Texas Longhorns | Texas Longhorns | 54.2% | 52.6% | 1.5% | -1.1% | no | ev_below_threshold |
| UNLV Rebels at North Texas Mean Green | UNLV Rebels | 62.6% | 61.1% | 1.5% | -1.6% | no | edge_below_threshold|ev_below_threshold |
| Colgate Raiders at Central Michigan Chippewas | Colgate Raiders | 8.7% | 7.2% | 1.5% | 21.1% | no | too_few_books|edge_below_threshold |
| Southern Utah Thunderbirds at Colorado State Rams | Southern Utah Thunderbirds | 10.4% | 9.0% | 1.4% | 14.8% | no | too_few_books|edge_below_threshold |
| UL-Monroe Warhawks at UAB Blazers | UAB Blazers | 77.2% | 75.8% | 1.4% | -0.4% | no | edge_below_threshold|ev_below_threshold |
| UCF Knights at Pittsburgh Panthers | Pittsburgh Panthers | 70.7% | 69.3% | 1.3% | -1.9% | no | edge_below_threshold|ev_below_threshold |
| UC Davis Aggies at SMU Mustangs | SMU Mustangs | 93.9% | 92.6% | 1.3% | -2.2% | no | too_few_books|edge_below_threshold|ev_below_threshold |
| North Dakota State Bison at Air Force Falcons | North Dakota State Bison | 56.0% | 54.8% | 1.3% | -0.9% | no | edge_below_threshold|ev_below_threshold |

Challengers (`market_public_ensemble`, `fpi_only`, `ratings_only`, `market_only`) are stored in the ledger but cannot trigger paper bets.

