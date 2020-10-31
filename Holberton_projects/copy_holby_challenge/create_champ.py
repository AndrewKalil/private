#!/usr/bin/python3

from fighter import Fighter
from mage import Mage
from rogue import Rogue

def create_champ():
    name = input("Enter the name of the Champion (Less that 10 characters): ")
    print()

    race = input("Choose the race of your champion:\n1) Human\n2) Elf\n3) Dwarf\n4) Hobbit\n5) Orc\nChoose number: ")
    print()

    gender = input("Choose your champion's gender:\n1) Male\n2) Female\n3) Other\nChoose number: ")
    print()

    champ_class = input("Choose the champion's class:\n1) Fighter\n2) Mage\n3) Rogue\nChoose a number: ")
    print()

    element = input("Choose your desired element:\n1) Solar\n2) Arc\n3) Void\nChoose a number: ")
    print()

    champ_class = int(champ_class)
    if champ_class is 1:
        _class = Fighter
    elif champ_class is 2:
        _class = Mage
    elif champ_class is 3:
        _class = Rogue
    return (name, race, gender, element, _class)