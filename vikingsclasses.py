# -*- coding: utf-8 -*-
"""vikingsClasses.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DeLVtgC7-rpxd_F-PegghxY9EiDchniK
"""

import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength

    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        return "Odin owns you all!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War
class War:
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        # your code here
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = viking.attack()
        result = saxon.receiveDamage(damage)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result

    def saxonAttack(self):
        # your code here
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = saxon.attack()
        result = viking.receiveDamage(damage)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        # your code here
        if not self.saxonArmy:
            return "The Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "The Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

# Yop
class War2:
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        # your code here
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        # your code here
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        # your code here
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = viking.attack()
        result = saxon.receiveDamage(damage)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result

    def saxonAttack(self):
        # your code here
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = saxon.attack()
        result = viking.receiveDamage(damage)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        # your code here
        if not self.saxonArmy:
            return "The Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "The Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."