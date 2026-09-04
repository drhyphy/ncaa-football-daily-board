# College Football Daily Moneyline Board

This repository runs and publishes the NCAA football moneyline board without relying on a local computer. GitHub Actions launches guarded attempts at 6:30, 6:45, and 7:00 AM Eastern each day; a date-based publication lock means only the first successful attempt runs the model. It refreshes the full FBS and FCS market, executes the frozen 75%-residual model, appends the forward timing ledger, grades completed games, and publishes the resulting board to the hosted site.

## Production model

The only recommendation-eligible candidate is `ncaaf-market-residual-v2-alpha75`:

- the de-vigged median moneyline across allowed books is the prior;
- the model retains 75% of the historically fitted FPI residual, producing a 21% effective FPI weight in Weeks 0–4 and 29.25% thereafter;
- every FBS–FBS, FBS–FCS, and FCS–FCS matchup returned by the market feed is scanned;
- a recommendation requires a schedule match, at least three books, no more than 4.5% consensus probability dispersion, at least 1.5% model probability edge, and at least 4% modeled EV;
- stakes are one-tenth Kelly, capped at 0.5% of bankroll, for paper tracking only.

The public-ratings blend, FPI-only, ratings-only, and market-only candidates remain in the append-only ledger as shadow benchmarks.

## Cloud workflow

`.github/workflows/daily-board.yml` is the independent production runner. It needs one repository secret:

- `ODDS_API_KEY`

The workflow can also be started manually from the GitHub Actions page. Its committed ledger survives ephemeral runners, and `site-data/boards.json` is the site&apos;s public, cloud-generated data feed. The dashboard therefore continues to refresh even when the local model never runs.

## Local validation

```bash
python -m pip install -e model pytest
python -m pytest -q model/tests tests
python scripts/site_board.py
npm install
npm run build
```

This is forward paper research, not a profitability guarantee or an automated wagering system.
