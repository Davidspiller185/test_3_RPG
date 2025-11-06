from PlayerGame import PlayerGame
class Goblin(PlayerGame):
    def __init__(self,name:str,weapon:str, speed=8,power=7,type="goblin",hp=20,armor_rating=1):
        super().__init__(name,hp,speed,power,armor_rating)
        self.type=type
        self.weapon=weapon
    def speak(self):
        print(f"{self.type}{self.name} is not happy")

    def attack(self):
        pass
    def run_away(self):
        pass
