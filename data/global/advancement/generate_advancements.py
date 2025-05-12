import os
import json
from pathlib import Path
import sys

# Ensure UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

# Define rarities
rarities = {
    "dull": "Dull",
    "common": "Common",
    "uncommon": "Uncommon",
    "rare": "Rare",
    "epic": "Epic",
    "legendary": "Legendary"
}

rarities_with_prefix = {
    "Dull": "wf_dull",
    "Common": "wf_common",
    "Uncommon": "wf_uncommon",
    "Rare": "wf_rare",
    "Epic": "wf_epic",
    "Legendary": "wf_legendary"
}

rarity_to_color = {
    "dull": '#9d9d9d',
    "common": '#ffffff',
    "uncommon": '#1eff00',
    "rare": '#0070dd',
    "epic": '#a335ee',
    "legendary": '#ff8000',
}

# Load fish data
fish_json_path = os.path.join(os.path.dirname(__file__), "../../minecraft/loot_table/gameplay/fishing/fish.json")
with open(fish_json_path, "r", encoding="utf-8") as f:
    fish_data = json.load(f)

fish_map = {}

for entry in fish_data['pools'][0]['entries']:
    fish_tag = entry['functions'][0]['components']['minecraft:custom_model_data']['strings'][0]
    fish_name = entry['functions'][0]['components']['minecraft:custom_name']['text']
    fish_rarity = rarities_with_prefix[fish_name.split()[0]]
    fish_map[f'{fish_tag}_{fish_rarity}'] = {
        "name": fish_name,
        "rarity": fish_rarity,
        "tag": fish_tag
    }

freshwater_fish_tags = [
      "wf_adamantitearowana",
      "wf_adonispleco",
      "wf_altheiaticray",
      "wf_canvasfish",
      "wf_catasterfishi",
      "wf_char",
      "wf_cobaltkoi",
      "wf_enderfish",
      "wf_firefly",
      "wf_geneticmistake",
      "wf_kittyfin",
      "wf_krapikgam",
      "wf_matchafish",
      "wf_maxyfish",
      "wf_minnow",
      "wf_mythrilmackrel",
      "wf_olivekoi",
      "wf_platypus",
      "wf_plurblefimsh",
      "wf_pochaflop",
      "wf_pompompupfish",
      "wf_pridefin",
      "wf_prismapatch",
      "wf_quackshank",
      "wf_rainbowtrout",
      "wf_skrimpy",
      "wf_stevefish",
      "wf_frogbert"
]
saltwater_fish_tags = [
    "wf_bubbles",
    "wf_cinnamofloat",
    "wf_diamondswordfish",
    "wf_dietdrkelp",
    "wf_dreadnoughtciscol",
    "wf_eelris",
    "wf_fihs",
    "wf_fishcake",
    "wf_frogfish",
    "wf_glorbfish",
    "wf_glormaw",
    "wf_hondacivic",
    "wf_jabbinggar",
    "wf_mapletuna",
    "wf_orichalcumoarfish",
    "wf_palladiumperch",
    "wf_pinkfrogmouth",
    "wf_pugfish",
    "wf_queenoffulgaria",
    "wf_seahorse",
    "wf_secretagenthat",
    "wf_shrimpmiku",
    "wf_stinkfish",
    "wf_titaniumtrout",
    "wf_vampiresquid"
]

print(f"Fish map: {fish_map}")

advancements_dir = "wf_individual/"
if not os.path.exists(advancements_dir):
    os.makedirs(advancements_dir)

# Generate advancements for each fish in fish_map using fish_salt/fish_fresh structure
print("\nGenerating advancements...")
advancement_count = 0

for fish_id, fish_data in fish_map.items():
    # File name: wf_<fish_tag>_<rarity>.json
    file_name = f"caught_{fish_data['rarity'].split('_')[1]}_{fish_data['tag'].split('_')[1]}.json"
    advancement_path = os.path.join(advancements_dir, file_name)
    criteria_key = f"fished_{fish_data['tag']}"
    advancement = {
        "display": {
            "icon": {
                "id": f"{'minecraft:cod' if fish_data['tag'] in saltwater_fish_tags else 'minecraft:salmon'}",
                "components": {
                    "custom_model_data": {
                        "strings": [fish_data['tag']]
                    }
                }
            },
            "title": {
                "color": rarity_to_color[fish_data['rarity'].split('_')[1].lower()],
                "text": fish_data['name']
            },
            "description": "You caught this fish!",
            "announce_to_chat": False,
            "show_toast": True,
            "hidden": True,
            "frame":"goal",
        },
        "parent": "global:wf_individual_root",
        "criteria": {
            criteria_key: {
                "trigger": "minecraft:fishing_rod_hooked",
                "conditions": {
                    "item": {
                        "predicates": {
                            "minecraft:custom_data": {
                                fish_data['tag']: "1b",
                                fish_data['rarity']: "1b"
                            }
                        }
                    }
                }
            }
        },
        "rewards": {
            "function": "webfishing:schedule_clear_loot_tracker"
        }
    }
    with open(advancement_path, "w", encoding="utf-8") as f:
        json.dump(advancement, f, indent=2, ensure_ascii=False)
    advancement_count += 1

print(f"\nGenerated {advancement_count} advancements!")
