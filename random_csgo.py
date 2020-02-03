#! python3
# random_csgo.py - pick a random primary and secondary weapon, random map, random map pool, random teams

import json
import requests
import random
import os
import platform



# TODO: Se Google Keep for noter til dette program



ALL_MAPS = ['Dust II', 'Inferno', 'Train', 'Mirage', 'Nuke', 'Overpass', 'Vertigo', 'Cache', 'Cobblestone', 'Canals', 'Zoo', 'Abbey', 'Biome', 'Militia', 'Agency', 'Office', 'Italy', 'Assault']

WEAPONS_SMGS = ['MP9', 'MAC-10', 'PP-Bizon', 'MP7', 'UMP-45', 'P90', 'MP5-SD']
WEPONS_RIFLES = []
WEAPONS_HEAVY = []
WEAPONS_PRIMARY = WEAPONS_SMGS + WEPONS_RIFLES + WEAPONS_HEAVY
WEAPONS_PISTOLS = ['P2000', 'USP-S', 'Glock-18', 'P250', 'Five-SeveN', 'Tec-9', 'CZ75-Auto', 'Dual Berettas', 'Desert Eagle', 'R8 Revolver']
WEAPONS_ALL = WEAPONS_PRIMARY + WEAPONS_PISTOLS

WEAPONS_GRENADES = ['HE Grenade', 'Flashbang', 'Smoke Grenade', 'Decoy Grenade', 'Molotov', 'Incendiary Grenade']
GEAR = ['Kevlar Vest', 'Kevlar + Helmet', 'Zeus x27', 'Defuse Kit', 'None']


def rnd_all_map():
    return random.choice(ALL_MAPS)


def rnd_all_weapon():
    return random.choice(WEAPONS_ALL)


def rnd_primary_weapon():
    return random.choice(WEAPONS_PRIMARY)


def rnd_secondary_weapon():
    return random.choice(WEAPONS_PISTOLS)


def rnd_grenade():
    return random.choice(WEAPONS_GRENADES)


def rnd_gear():
    return random.choice(GEAR)


def rnd_full_set():
    rnd_map = rnd_all_map()
    weapon_pri = rnd_primary_weapon()
    weapon_sec = rnd_secondary_weapon()
    grenade = rnd_grenade()
    gear = rnd_gear()

# TODO: maybe use this class to make random teams
class Player:
    def __init__(self, name):
        self.name = name


def main():
    while True:
        start_input = input('Choose what to pick (map, weapons): ').lower()
        if start_input == 'map':
            print(f'{rnd_all_map()}\n')
        elif start_input == 'weapons':
            print(f'{rnd_all_weapon()}\n')
        else:
            print('Try again\n')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nProgram closed by the user\n')
