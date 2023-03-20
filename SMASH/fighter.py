class Fighter:
    def __init__(self, name, origin, character_type, weapon, weight, strength, height, speed=5):
        #name, origin, type, speed, weight, strength, height, weapon, percentage
        self.name = name
        self.origin = origin
        self.character_type = character_type
        self.weapon = weapon
        self.weight = weight
        self.strength = strength
        self.height = origin
        self.speed = speed
        self.percentage = 0

    def attack(self,opponent):
        damage = 10
        print(f"{self.name} attacked {opponent.name} and dealt {damage}%!!!")
        opponent.percentage += damage
    
    def status(self):
        print(f"Name: {self.name}, origin: {self.origin}, type: {self.character_type}, percentage: {self.percentage}%")
    
    def special(self, opponent):
        damage = 15
        print(f"{self.name} attacked {opponent.name} and dealt {damage}%!!!")
        opponent.percentage += damage


pac_man = Fighter("Pac Man","Pac Man","Pac Man","mouth",6,6,4,3)
roy = Fighter("Roy","Fire Emblem","Human","Sword",5,8,6,6)

# roy.status()
# pac_man.attack(roy)
# roy.status()
# pac_man.attack(roy)
# roy.status()

# roy.special(pac_man)
# pac_man.status()
