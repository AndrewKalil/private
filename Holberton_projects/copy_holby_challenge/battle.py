#!/usr/bin/python3
""""""
from time import sleep

def battle(p1, p2):
    ele1 = p1.element
    ele2 = p2.element
    red = "\033[1;31m"
    blue = "\033[1;34m"
    reset = "\033[0;0m"

    while True:
        if p1.health <= 0 or p2.health <= 0:
            if p1.health > 0:
                print("{}PLAYER 1 WINS".format(reset))
                p1.win()
                p2.lose()
            elif p2.health > 0:
                print("{}PLAYER 2 WINS".format(reset))
                p2.win()
                p1.lose()
            break

        if p1.health > 0:
            dmg1 = p1.attack_action(ele2)
            print("{}Player 1 Attacking...".format(reset))
            print()
            sleep(3)
            p2.total_defence(dmg1, ele1)
            print("{}Player 1 stats after attack:".format(red))
            print("Name: {}\nHealth: {:.2f}\nEnergy: {:.2f}".format(p1.name, p1.health, p1.energy))
            print()
            print("{}Player 2 stats after attack".format(blue))
            print("Name: {}\nHealth: {:.2f}\nEnergy: {:.2f}".format(p2.name, p2.health, p2.energy))
            sleep(6)
            print()

        if p2.health > 0:
            dmg2 = p2.attack_action(ele1)
            print("{}Player 2 Attacking...".format(reset))
            print()
            sleep(3)
            p1.total_defence(dmg2, ele2)
            print("{}Player 1 stats after attack:".format(red))
            print("Name: {}\nHealth: {:.2f}\nEnergy: {:.2f}".format(p1.name, p1.health, p1.energy))
            print()
            print("{}Player 2 stats after attack".format(blue))
            print("Name: {}\nHealth: {:.2f}\nEnergy: {:.2f}".format(p2.name, p2.health, p2.energy))
            sleep(6)
            print()
