from PlayerGame import PlayerGame
from game import Game
class Player(PlayerGame):

    def __init__(self,name:str,profession:str,speed=7,power=6,armor_rating=14,hp=50):
        super().__init__(name,hp,speed,power,armor_rating)
        self.profession=profession

    def speak(self):
        print(f"{self.name} say i play in the game")
    @staticmethod
    def attack(attack,attacked):
        v,s=Game.roll_dice(20)
        sum_val=v+attack.speed
