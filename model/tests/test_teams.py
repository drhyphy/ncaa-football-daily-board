from ncaaf_model.teams import best_prefix_match, normalize_team, pair_key


def test_aliases_and_prefixes() -> None:
    assert normalize_team("Hawai'i Rainbow Warriors") == "hawaii"
    assert normalize_team("UConn") == "connecticut"
    assert best_prefix_match("USC Trojans", ["USC", "UCLA"]) == "USC"
    assert best_prefix_match("NC State Wolfpack", ["NC State", "North Carolina"]) == "NC State"
    assert pair_key("UConn Huskies", "UMass Minutemen") == "connecticut@massachusetts"

