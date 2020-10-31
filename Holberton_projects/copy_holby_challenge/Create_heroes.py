#!/usr/bin/python3
import json

if __name__ == "__main__":

    hero = {}

    hero['Heroe_0'] = []
    hero['Heroe_1'] = []
    hero['Heroe_2'] = []
    hero['Heroe_3'] = []
    hero['Heroe_4'] = []
    hero['Heroe_5'] = []

    hero['Heroe_0'].append({
        'class': 'Fighter',
        'Name': 'Pekka',
        'Gender': 'Gay',
        'Level': 0,
        'Health': 100,
        'Attack': 45,
        'Defense': 75,
        'Armor': 'Heavy Armor',
        'Weapon': 'Sword',
        'Magic': 'None',
        'Speed': 3

        })

    hero['Heroe_1'].append({
        'class': 'Mage',
        'Name': 'Merlin',
        'Gender': 'Female',
        'Level': 0,
        'Health': 100,
        'Attack': 5,
        'Defense': 20,
        'Armor': 'Medium Armor',
        'Weapon': 'staff',
        'Magic': 60,
        'Speed': 10
        })

    hero['Heroe_2'].append({
        'class': 'Rogue',
        'Name': 'Sasuke',
        'Gender': 'other',
        'Level': 0,
        'Health': 100,
        'Attack': 80,
        'Defense': 30,
        'Armor': 'Light Armor',
        'Weapon': 'daggers',
        'Magic': 'None',
        'Speed': 15

    })

    hero['Heroe_3'].append({
        'class': 'Fighter',
        'Name': 'Goku',
        'Gender': 'Male',
        'Level': 0,
        'Health': 100,
        'Attack': 45,
        'Defense': 30,
        'Armor': 'Heavy Armor',
        'Weapon': 'Sword',
        'Magic': 'None',
        'Speed': 5

    })

    hero['Heroe_4'].append({
        'class': 'Mage',
        'Name': 'Cleopatra',
        'Gender': 'Female',
        'Level': 0,
        'Health': 100,
        'Attack': 7,
        'Defense': 20,
        'Armor': 'Medium Armor',
        'Weapon': 'staff',
        'Magic': 63,
        'Speed': 10

    })

    hero['Heroe_5'].append({
        'class': 'Rogue',
        'Name': 'Homero',
        'Gender': 'Male',
        'Level': 0,
        'Health': 100,
        'Attack': 81,
        'Defense': 30,
        'Armor': 'Light Armor',
        'Weapon': 'daggers',
        'Magic': 'None',
        'Speed': 15

    })


    with open("champions.json", mode='w') as file:
        json.dump(hero, file, indent=4)
