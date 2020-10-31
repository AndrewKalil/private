#!/usr/bin/python3
""""""
from champ import Champ
import random

class Fighter(Champ):
    def __init__(
        self, name, race, gender, element=None, id=None, weapon="sword and shield", armor="heavy", champ_class="Fighter",
        health=100, attack=35, defence= 65, magic=0, speed=3, dmg_reduction=10):
        super().__init__(name, race, gender, element, id, weapon, armor, champ_class, health, attack, defence, magic, speed, dmg_reduction)

    def rush_attack(self, enemy=None):
        Total_dmg = (self.attack * .80) + ((self.speed/50)*self.attack)
        self.energy -= 45
        if self.energy <= 0:
            self.energy = 0
        value = Total_dmg
        self.T_dmg += value
        return value

    def elemental_slam(self, enemy=None):
        """unlocks at level 3"""
        if self.Level >= 3:
            Total_dmg = (self.attack * .90) + ((self.speed/50)*self.attack)
            self.energy -= 45
            if self.energy <= 0:
                self.energy = 0
            value = Total_dmg
            self.T_dmg += value
            return value

    def pound_hits(self, enemy=None):
        """unlock at level 7"""
        if self.Level >= 7:
            value = random.randint(1, self.speed)
            Total_dmg = value * self.attack
            self.energy -= 55
            if self.energy <= 0:
                self.energy = 0
            value = Total_dmg
            self.T_dmg += value
            return value

    def ultimate(self, enemy=None):
        """unlocks at level 10"""
        if self.Level >= 10:
            Total_dmg = (1.5 * self.attack) + 15
            self.energy -= 100
            if self.energy <= 0:
                self.energy = 0
            value = Total_dmg
            self.T_dmg += value
            return value
