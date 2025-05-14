execute at @s run particle minecraft:happy_villager ~ ~ ~ 0.3 1 0.3 100 250
playsound minecraft:entity.experience_orb.pickup ambient @a[distance=..8] ~ ~ ~ 30

tag @s add wf_rod_vendor
tag @s add global.ignore
tag @s add global.ignore.pos
tag @s add global.ignore.gui
tag @s add global.ignore.kill

data merge entity @s {VillagerData:{profession:fisherman,level:5,type:savanna},PersistenceRequired:1,CustomName:"Rod Vendor",\
    Offers: {\
        Recipes: [\
        {\
            maxUses: 999999,\
            rewardExp: 0,\
            buy: {count: 1, id: "minecraft:stick"},\
            buyB: {count: 2, id: "minecraft:string"},\
            sell: {count: 1, id: "minecraft:fishing_rod",\
                components: {\
                    custom_name: {"text":"Dull Rod", "color": "#9d9d9d", "italic": false},\
                    custom_model_data: {"strings": ["wf_roddull"]},\
                    custom_data: {wf_dull: "1b"}\
                }\
            },\
        },\
        {\
            maxUses: 999999,\
            rewardExp: 0,\
            buy: {count: 10, id: "minecraft:iron_nugget",\
                components: {\
                    custom_name: {"text":"Copper Fish Coin", "color": "#b6743d", "italic": false},\
                    custom_model_data: {"strings": ["wf_copper"]},\
                }\
            },\
            sell: {count: 1, id: "minecraft:fishing_rod",\
                components: {\
                    custom_name: {"text":"Common Rod", "color": "#ffffff", "italic": false},\
                    custom_model_data: {"strings": ["wf_rodcommon"]},\
                    custom_data: {wf_common: "1b"}\
                }\
            },\
        },\
        {\
            maxUses: 999999,\
            rewardExp: 0,\
            buy: {count: 2, id: "minecraft:iron_nugget",\
                components: {\
                    custom_name: {"text":"Silver Fish Coin", "color": "#abb0b6", "italic": false},\
                    custom_model_data: {"strings": ["wf_silver"]},\
                }\
            },\
            sell: {count: 1, id: "minecraft:fishing_rod",\
                components: {\
                    custom_name: {"text":"Uncommon Rod", "color": "#1eff00", "italic": false},\
                    custom_model_data: {"strings": ["wf_roduncommon"]},\
                    custom_data: {wf_uncommon: "1b"}\
                }\
            },\
        },\
        {\
            maxUses: 999999,\
            rewardExp: 0,\
            buy: {count: 10, id: "minecraft:iron_nugget",\
                components: {\
                    custom_name: {"text":"Silver Fish Coin", "color": "#abb0b6", "italic": false},\
                    custom_model_data: {"strings": ["wf_silver"]},\
                }\
            },\
            sell: {count: 1, id: "minecraft:fishing_rod",\
                components: {\
                    custom_name: {"text":"Rare Rod", "color": "#0070dd", "italic": false},\
                    custom_model_data: {"strings": ["wf_rodrare"]},\
                    custom_data: {wf_rare: "1b"}\
                }\
            },\
        },\
        {\
            maxUses: 999999,\
            rewardExp: 0,\
            buy: {count: 5, id: "minecraft:iron_nugget",\
                components: {\
                    custom_name: {"text":"Gold Fish Coin", "color": "#c79623", "italic": false},\
                    custom_model_data: {"strings": ["wf_gold"]},\
                }\
            },\
            sell: {count: 1, id: "minecraft:fishing_rod",\
                components: {\
                    custom_name: {"text":"Epic Rod", "color": "#a335ee", "italic": false},\
                    custom_model_data: {"strings": ["wf_rodepic"]},\
                    custom_data: {wf_epic: "1b"}\
                }\
            },\
        },\
        {\
            maxUses: 999999,\
            rewardExp: 0,\
            buy: {count: 30, id: "minecraft:iron_nugget",\
                components: {\
                    custom_name: {"text":"Gold Fish Coin", "color": "#c79623", "italic": false},\
                    custom_model_data: {"strings": ["wf_gold"]},\
                }\
            },\
            sell: {count: 1, id: "minecraft:fishing_rod",\
                components: {\
                    custom_name: {"text":"Legendary Rod", "color": "#ff8000", "italic": false},\
                    custom_model_data: {"strings": ["wf_rodlegendary"]},\
                    custom_data: {wf_legendary: "1b"}\
                }\
            },\
        }]\
    }\
}