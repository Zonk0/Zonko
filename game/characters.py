#defines different entities in the game
class Charcater:
    def __init__(self,name,hp,dmg):
        self.name= name 
        self.hp= hp 
        self.dmg= dmg

        self.dead=False

        def attack(self,other):
            pass
        def update(self):
            if self.hp<0:
                self.dead = True
                self.hp=0

#default player= your name choice, 5hp, 5dmg of melee attack and 10dmg of ranged

class Player(Charcater):
    def __init__(self,name,hp,dmg,int):
        Character.__init__(self,name,hp,dmg)
        self.int=int
    def dead(self):
        self.hp=0
        self.dead=True
#enemies are shooters(5hp,2dmg), melee(10hp,2dmg) and maybe tanks (20hp,1dmg) or hybrids both melee and ranged(15hp,3dmg)
class Enemy(Charcater):
    def __init__(self,name,hp,dmg):
        Character.__init__(self,name,hp,dmg)
    

class Weapon:
    def __init__(self,name,dmg):
        self.dmg=dmg[]
    def Damage(self):
        pass

class Ranged(Weapon):
    def __init__(self,name,dmg):
        pass
class Melee(Weapon):
    def __init__(self,name,dmg):
        pass