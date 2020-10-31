#!/usr/bin/python3
""""""
from fighter import Fighter
import random

class Mage(Fighter):

    def __init__(
        self, name, race, gender, element=None, id=None, weapon="staff", armor="medium", champ_class="Mage",
        health=100, attack=0, defence= 35, magic=65, speed=6, dmg_reduction=6):
        super().__init__(name, race, gender, element, id, weapon, armor, champ_class, health, attack, defence, magic, speed, dmg_reduction)

    def soul_burn(self, enemy=None):
        Total_dmg = (self.magic * .68) + ((self.speed/100)*self.magic)
        self.energy -= 45
        if self.energy <= 0:
            self.energy = 0
        value = Total_dmg
        self.T_dmg += value
        return value

    def elemental_staff(self, enemy=None):
        """unlocks at level 3"""
        if self.Level >= 3:
            Total_dmg = (self.magic * .76) + ((self.speed/100)*self.magic)
            self.energy -= 45
            if self.energy <= 0:
                self.energy = 0
            value = Total_dmg
            self.T_dmg += value
            return value

    def legion_attack(self, enemy=None):
        """unlock at level 10"""
        if self.Level >= 7:
            value = random.randint(1,int((1/1.5)*self.speed))
            Total_dmg = value * self.magic
            self.energy -= 75
            if self.energy <= 0:
                self.energy = 0
            value = Total_dmg
            self.T_dmg += value
            return value

    def ultimate(self, enemy=None):
        if self.Level >= 10:
            Total_dmg = (self.magic) + 25
            self.energy -= 100
            if self.energy <= 0:
                self.energy = 0
            value = Total_dmg
            self.T_dmg += value
            return value
