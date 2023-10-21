import random

class BigCat:
    def __init__(self, speed=5,strength=5,intelligence=5,health=5,durability=5):
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.health = health
        self.durability = durability

class Lion(BigCat):
    def __init__(self, speed=5,strength=50,intelligence=5,health=50,durability=5):
        super().__init__(speed,strength,intelligence,health,durability)
    
    def king(self,bigcat):
        if(isinstance(bigcat,Cheetah)):
            chance = random.randint(1,100)
            if chance <= 60:
                print("The Cheetah Got Away!")
                self.health -= 20
            else:
                bigcat.speed = 0
                bigcat.strength = 0
                bigcat.intelligence=0
                bigcat.health=0
                bigcat.durability=0
        else:
            bigcat.speed = 0
            bigcat.strength = 0
            bigcat.intelligence=0
            bigcat.health=0
            bigcat.durability=0


class Leopard(BigCat):
    def __init__(self, speed=5,strength=30,intelligence=30,health=30,durability=5):
        super().__init__(speed,strength,intelligence,health,durability)  

    def attack(self,bigcat):
        if(isinstance(bigcat,Lion)):
            bigcat.king(self)
        elif(isinstance(bigcat,Cheetah)):
            chance = random.randint(1,100)
            if chance <= 60:
                print("The Cheetah Got Away!")
                self.health -= 20
            else:
                bigcat.health -=15
        else:
            bigcat.health -=15   

class Cheetah(BigCat):
    def __init__(self, speed=75,strength=25,intelligence=25,health=25,durability=25):
        super().__init__(speed,strength,intelligence,health,durability)

    def run(self,bigcat):
        if(isinstance(bigcat,Lion)):
            bigcat.king(self)
        elif(isinstance(bigcat,Leopard)):
            bigcat.attack(self)

cheetah = Cheetah()
lion = Lion()
leopard = Leopard()

cheetah.run(lion)
leopard.attack(cheetah)
lion.king(leopard)
    

        
        