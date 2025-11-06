from PlayerGame import PlayerGame
class Orc(PlayerGame):
    def __init__(self,name:str,weapon:str,speed=2,power=12,armor_rating=5,type="orc",hp=50):
        super().__init__(name,hp,speed,power,armor_rating)
        self.type=type
        self.weapon=weapon
    def speak(self):
        print(f"{self.type}{self.name} is not happy")

    def attack(self):
        pass #חייב למלאות
