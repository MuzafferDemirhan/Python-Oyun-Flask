import random

LOCATIONS = {
    "village":  {"name": "Köy",          "enemies": ["goblin"],            "level_req": 1},
    "forest":   {"name": "Karanlık Orman","enemies": ["goblin", "orc"],     "level_req": 2},
    "dungeon":  {"name": "Zindan",        "enemies": ["skeleton", "orc"],   "level_req": 5},
    "mountain": {"name": "Ejder Dağı",    "enemies": ["dragon"],            "level_req": 10},
}

def get_random_encounter(location_key: str, player_level: int) -> str:
    loc = LOCATIONS.get(location_key)
    if not loc or player_level < loc["level_req"]:
        return None
    return random.choice(loc["enemies"])

def get_available_locations(player_level: int) -> list:
    return [
        {"key": k, **v}
        for k, v in LOCATIONS.items()
        if player_level >= v["level_req"]
    ]