#! python3
# random_csgo.py - pick a random primary and secondary weapon, random map, random map pool, random teams

import json
import requests
import random
import os
import platform



# TODO: Se Google Keep for noter til dette program

# TODO: Have info about the weapons, such as damage and ammo



ALL_MAPS = ['Dust II', 'Inferno', 'Train', 'Mirage', 'Nuke', 'Overpass', 'Vertigo', 'Cache', 'Cobblestone', 
    'Canals', 'Zoo', 'Abbey', 'Biome', 'Militia', 'Agency', 'Office', 'Italy', 'Assault']

WEAPONS_SMGS = ['MP9', 'MAC-10', 'PP-Bizon', 'MP7', 'UMP-45', 'P90', 'MP5-SD']
WEPONS_RIFLES = []
WEAPONS_HEAVY = []
WEAPONS_PRIMARY = WEAPONS_SMGS + WEPONS_RIFLES + WEAPONS_HEAVY
WEAPONS_PISTOLS = ['P2000', 'USP-S', 'Glock-18', 'P250', 'Five-SeveN', 'Tec-9', 'CZ75-Auto', 'Dual Berettas', 'Desert Eagle', 'R8 Revolver']
WEAPONS_ALL = WEAPONS_PRIMARY + WEAPONS_PISTOLS

WEAPONS_GRENADES = ['HE Grenade', 'Flashbang', 'Smoke Grenade', 'Decoy Grenade', 'Molotov', 'Incendiary Grenade']
GEAR = ['Kevlar Vest', 'Kevlar + Helmet', 'Zeus x27', 'Defuse Kit', 'None']

TEAMS = ['Counter Terrorist', 'Terrorist']


def rnd_all_map():
    """Returns a random map"""
    return random.choice(ALL_MAPS)


def rnd_all_weapon():
    """Returns a random weapon from all weapons"""
    return random.choice(WEAPONS_ALL)


def rnd_primary_weapon():
    """Returns a random primary weapon"""
    return random.choice(WEAPONS_PRIMARY)


def rnd_secondary_weapon():
    """Returns a random secondary weapon"""
    return random.choice(WEAPONS_PISTOLS)


def rnd_grenade():
    """Returns a random grenade"""
    return random.choice(WEAPONS_GRENADES)


def rnd_gear():
    """Returns a random gear"""
    return random.choice(GEAR)


def rnd_full_set():
    """Returns a random map, a random primary and secondary weapon, a random grenade and random gear"""
    rnd_map = rnd_all_map()
    weapon_pri = rnd_primary_weapon()
    weapon_sec = rnd_secondary_weapon()
    grenade = rnd_grenade()
    gear = rnd_gear()
    return rnd_map, weapon_pri, weapon_sec, grenade, gear


# TODO: maybe use this class to make random teams
class Player:
    def __init__(self, name, team=''):
        self.name = name
        self.team = team
    
    def rnd_team(self):
        # TODO: Check if a team is full
        self.team = random.choice(TEAMS)
    
    def print_team(self):
        if not self.team == '':
            print(f'{self.name} is on team {self.team}')
        else:
            print(f'{self.name} is not on a team')


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
