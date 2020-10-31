#!/usr/bin/python3
""""""
from base import Base
import json
import random

class Champ(Base):
    T_dmg_done = 0
    T_dmg_taken = 0
    T_dmg = 0
    CRIT = 0
    reset = 0
    energy = 200
    energy_reset = energy

    def __init__(
        self, name, race, gender, element=None, id=None, weapon="", armor="", champ_class="",
        health=0, attack=0, defence= 0, magic=0, speed=0, dmg_reduction=0):
        self.champ_class = champ_class
        self.name = name
        self.race = race
        self.gender = gender
        self.element = element
        self.health = health
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.weapon = weapon
        self.armor = armor
        self.speed = speed
        self.dmg_reduction = dmg_reduction
        self.T_dmg_done = Champ.T_dmg_done
        self.T_dmg_taken = Champ.T_dmg_taken
        self.T_dmg = Champ.T_dmg
        self.CRIT = Champ.CRIT
        self.reset = health
        self.energy = Champ.energy
        self.energy_reset = Champ.energy_reset
        super().__init__(id)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validator('name', value)
        self.__name = value

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, value):
        if type(value) is int:
            self.validator('race', int(value))
            race_list = ["Human", "Elf", "Dwarf", "Hobbit", "Orc"]
            self.__race = str(race_list[int(value) - 1])
        else:
            self.__race = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if type(value) is int:
            self.validator('gender', int(value))
            gender_list = ["Male", "Female", "Other"]
            self.__gender = str(gender_list[int(value) - 1])
        else:
            self.__gender = value

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, value):
        if type(value) is int:
            self.validator('element', int(value))
            element_list = ['Solar', 'Arc', 'Void']
            self.__element = str(element_list[int(value) - 1])
        else:
            self.__element = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def dmg_reduction(self):
        return self.__dmg_reduction

    @dmg_reduction.setter
    def dmg_reduction(self, value):
        self.__dmg_reduction = value

    def validator(self, name, value):
        if name is 'name' and len(value) > 10:
            raise Exception("Name is too long, only 10 characters allowed")
        if name is 'race' and (1 > value > 5):
            raise Exception("No race was chosen")
        if name is 'gender' and (1 > value > 3):
            raise Exception("No gender was chosen")
        if name is 'element' and (1 > value > 3):
            raise Exception("No element was chosen")

    def validate_list(self, name, value):
        if name is 'race' and value not in ["Human", "Elf", "Dwarf", "Hobbit", "Orc"]:
            raise Exception("Not a valid race")
        if name is 'gender' and value not in ["Male", "Female", "Other"]:
            raise Exception("Not a valid gender")
        if name is 'element' and value not in ['Solar', 'Arc', 'Void']:
            raise Exception("Not a valid element")

    def __str__(self):
        str = "Class: {}\nName: {}\nRace: {}\nGender: {}\nElement: {}\nHealth: {}\nAttack: {}\nDefence: {}\nMagic: {}\nWeapon: {}\nArmor: {}\nSpeed: {}%\nDamage Reduction: {}%\nLevel: {}\nEXP for Next Level: {}\nCurrent EXP: {}\nTotal EXP: {}\nStat Points: {}\nChampion id: {}\n"
        return (str.format(
            self.champ_class, self.name, self.race, self.gender, self.element, self.health, self.attack, self.defence, self.magic, self.weapon,
            self.armor, self.speed, self.dmg_reduction, self.Level, self.EXP_N_L, self.C_EXP, self.T_EXP, self.S_Points, self.id))

    def to_dictionary(self):
        """turns attributes to a dictionary

        Returns:
            dict: dictionary with all attributes
        """
        dic = {}
        ls = [
            'champ_class', 'name', 'race', 'gender', "element", 'health', 'attack', 'defence', 'magic',
            'weapon', 'armor', 'speed', 'dmg_reduction', 'Level', 'EXP_N_L', 'C_EXP', 'T_EXP', 'S_Points', 'id'
        ]
        for i in ls:
            dic[i] = getattr(self, i)
        return dic

    def update(self, **kwargs):
        """udates an object
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save_to_file(self):
        """saves a json string to a file

        Args:
            list_objs (objcet): object to convert to string
        """
        with open("{}.json".format(self.name), mode='w') as fd:
            fd.write(self.to_json_string(self.to_dictionary()))

    def level_up(self):
        self.S_Points += 3
        self.Level += 1
        self.EXP_N_L =  self.EXP_N_L + (self.EXP_N_L * self.Level)
        self.T_EXP += self.EXP_N_L
        self.C_EXP = 0
        self.energy += 50
        self.energy_reset = self.energy

    def gain_xp(self):
        self.C_EXP = (0.5 * self.T_dmg) + 10
        if self.C_EXP >= self.EXP_N_L:
            self.level_up()

    def death(self):
        self.C_EXP -= (0.5 * self.C_EXP)
        if self.C_EXP <= 0:
            self.C_EXP = 0

    def stat_reset(self):
        self.health = self.reset
        self.T_dmg = 0
        self.energy = self.energy_reset

    def increase_stats(self, **kwargs):
        """udates an object
        """
        if len(kwargs) <= self.S_Points:
            for key, value in kwargs.items():
                if key in ['health', 'attack', 'defence', 'magic']:
                    value = getattr(self, key) + 5
                    setattr(self, key, value)
                elif key in ['armor']:
                    value_speed = getattr(self, "speed") + 0.5
                    setattr(self, "speed", value_speed)
                    value_dmg_reduction = getattr(self, "dmg_reduction") + 0.5
                    setattr(self, "dmg_reduction", value_dmg_reduction)
                else:
                    print("You cannot access that attribute")
            self.S_Points -= len(kwargs)
        else:
            print("You can only use the attribute points available")
        self.reset = self.health

    def attack_action(self, enemy=None):
        value = random.randint(1, 100)
        if 1 <= value <= self.speed:
            self.CRIT = (self.speed / 100)
        if self.champ_class is "Rogue":
            self.T_dmg_done = (.60*self.attack) + (self.CRIT * self.attack)
        elif self.champ_class is "Fighter":
            self.T_dmg_done = (self.attack) + (self.CRIT * self.attack)
        elif self.champ_class is "Mage":
            self.T_dmg_done = (.60*self.magic) + (self.CRIT * self.magic)
        value = self.T_dmg_done
        self.T_dmg += value
        self.energy -= (value * .05)
        if self.energy <= 0:
            self.energy = 0
        self.CRIT = 0
        return value

    def defend_action(self):
        value = (.40 * self.defence) + ((self.dmg_reduction/100)*self.defence)
        return value

    def total_defence(self, dmg, enemy=None):
        if self.element is "Solar" and enemy is "Void":
            value = dmg + (dmg * .25)
        elif self.element is "Arc" and enemy is "Solar":
            value = dmg + (dmg * .25)
        elif self.element is "Void" and enemy is "Arc":
            value = dmg + (dmg * .25)
        else:
            value = dmg
        rand = random.randint(1, 100)
        if 1 <= rand <= self.speed:
            self.T_dmg_taken = 0
        else:
            self.T_dmg_taken = value - self.defend_action()
        self.health -= self.T_dmg_taken
        if self.health <= 0:
            self.health = 0


    def display_battle_stats(self):
        str = "Name: {}\nHealth: {:.2f}\nEnergy: {:.2f}"
        if self.health <= 0:
            self.health = 0
        print(str.format(self.name, float(self.health), float(self.energy)))

    def win(self):
        self.gain_xp()
        self.stat_reset()
        self.save_to_file()

    def lose(self):
        self.death()
        self.stat_reset()
        self.save_to_file()
