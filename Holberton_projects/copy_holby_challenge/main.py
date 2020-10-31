#!/usr/bin/python3
""""""

from fighter import Fighter
from mage import Mage
from rogue import Rogue
from champ import Champ
from base import Base
from time import sleep
battle = __import__('battle').battle
create_champ = __import__('create_champ').create_champ

if __name__ == '__main__':
  """obj = tuple()
  obj = create_champ()
  print(obj)"""

  name = "Andrew"
  race = "Human"
  gender = "Male"
  element = "Void"

  """dic = Fighter.load_from_file("Andrew")
  p1 = Fighter("Dummy", 1, 1)
  p1.update(**dic)
  p1.level_up()
  p1.increase_stats(health=1, defence=1, armor=1)"""

  p1 = Mage(name, race, gender, element)
  p2 = Fighter("Sasuke", "Elf", "Male", "Arc")

  """print(p1, end="\n")
  print(p2, end="\n")"""

  battle(p1, p2)
