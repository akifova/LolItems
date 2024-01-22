from src.Champion import Champion
from src.Item import Item


def get_input():
    characters = input("Enter the first 3 characters of the champion name: ")
    if len(characters) < 3:
        print("Please enter at least 3 characters.")
        return get_input()
    return characters


def search(characters):
    champion_list = create_champion_list(characters)
    if len(champion_list) == 0:
        print("Champion not found.")
        return
    print("Champions you are looking for:")
    for champ in champion_list:
        print(champ.name)
    return champion_list


def create_champion_list(characters):
    return_list = []
    for champ in champions:
        champ_name = champ.name.lower()
        lower_characters = characters.lower()

        if champ_name.startswith(lower_characters):
            return_list.append(champ)
    return return_list


def display_output(champion):
    print("Recommended item build:")
    for item in champion.recommended_item_list:
        print(item.name + ": " + str(item))


def make_selection(champs):
    selection = input("Select a champion: ")

    for champ in champs:
        champ_name = champ.name.lower()
        lower_selection = selection.lower()
        if champ_name == lower_selection:
            return champ
    return selection


item_list = [
    Item("Doran's Blade", "A basic sword that grants you attack damage and health regeneration.",
         {"attack_damage": 80, "health_regeneration": 8}),
    Item("Boots of Speed", "Basic boots that grant you movement speed.", {"movement_speed": 45}),
    Item("Vampiric Scepter", "A basic lifesteal item that grants you attack damage and lifesteal.",
         {"attack_damage": 40, "lifesteal": 10}),
    Item("Phage", "A basic attack speed item that grants you attack speed and movement speed.",
         {"attack_speed": 25, "movement_speed": 20}),
    Item("Sheen", "A basic item that grants you attack damage and ability power.",
         {"attack_damage": 50, "ability_power": 50}),
    Item("Bilgewater Cutlass", "A basic item that grants you attack damage, lifesteal, and a slow.",
         {"attack_damage": 60, "lifesteal": 12, "slow_duration": 2}),
]

champions = [
    Champion("Aatrox", "Top", [item_list[0], item_list[1], item_list[2], item_list[3], item_list[4], item_list[5]]),
    Champion("Ahri", "Mid", [item_list[0], item_list[1], item_list[2], item_list[3], item_list[4], item_list[5]]),
    Champion("Akali", "Top", [item_list[0], item_list[1], item_list[2], item_list[3], item_list[4], item_list[5]]),
]
