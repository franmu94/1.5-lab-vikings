
# Soldier
import random
class Soldier:

    def __init__(self, health, strength):
        self.health  = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return(self.name+" has received "+str(damage)+" points of damage")
        else: return(self.name+" has died in act of combat")

    def battleCry(self):
        return("Odin Owns You All!")

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return("A Saxon has received "+str(damage)+" points of damage")
        else: return("A Saxon has died in combat")
    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        idxSaxon = random.randint(0,len(self.saxonArmy)-1)
        idxViking = random.randint(0,len(self.vikingArmy)-1)


        unsaxon = self.saxonArmy[idxSaxon]
        unviking = self.vikingArmy[idxViking]

        result = unsaxon.receiveDamage(unviking.strength)

        if unsaxon.health <= 0:
            self.saxonArmy.pop(idxSaxon)
        
        return (result)
    
    def saxonAttack(self):
        idxSaxon = random.randint(0,len(self.saxonArmy)-1)
        idxViking = random.randint(0,len(self.vikingArmy)-1)

        unsaxon = self.saxonArmy[idxSaxon]
        unviking= self.vikingArmy[idxViking]

        result = unviking.receiveDamage(unsaxon.strength)

        if unviking.health <= 0:
            self.vikingArmy.pop(idxViking)
        
        return (result)

    def showStatus(self):
        if len(self.saxonArmy) == 0: return("Vikings have won the war of the century!") 
        elif len(self.vikingArmy) == 0: return("Saxons have fought for their lives and survive another day...")
        else: return "Vikings and Saxons are still in the thick of battle."


        
        
        
        
        
        