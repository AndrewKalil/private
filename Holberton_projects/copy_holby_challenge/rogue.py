#!/usr/bin/python3
""""""
from champ import Champ
import random

class Rogue(Champ):

    def __init__(
        self, name, race, gender, element=None, id=None, weapon="daggers", armor="light", champ_class="Rogue",
        health=100, attack=70, defence= 30, magic=0, speed=10, dmg_reduction=3):
        super().__init__(name, race, gender, element, id, weapon, armor, champ_class, health, attack, defence, magic, speed, dmg_reduction)

    def shadow_attack(self, enemy=None):
        Total_dmg = (self.attack * .68) + ((self.speed/100)*self.attack)
        self.energy -= 45
        if self.energy <= 0:
            self.energy = 0
        value = Total_dmg
        self.T_dmg += value
        return value

    def elemental_dancing_daggers(self, enemy=None):
        """unlocks at level 3"""
        if self.Level >= 3:
            Total_dmg = (self.attack * .76) + ((self.speed/100)*self.attack)
            self.energy -= 45
            if self.energy <= 0:
                self.energy = 0
            value = Total_dmg
            self.T_dmg += value
            return value

    def multiple_stab(self, enemy=None):
        """unlock at level 10"""
        if self.Level >= 7:
            value = random.randint(1,int((1/4)*self.speed))
            Total_dmg = value * self.attack
            self.energy -= 75
            if self.energy <= 0:
                self.energy = 0
            value = Total_dmg
            self.T_dmg += value
            return value

    def ultimate(self, enemy=None):
        if self.Level >= 10:
            Total_dmg = (self.attack) + 30
            self.energy -= 100
            if self.energy <= 0:
                self.energy = 0
            value = Total_dmg
            self.T_dmg += value
            return value
