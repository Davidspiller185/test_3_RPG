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
        while attack.hp>0 and attacked.hp>0:
            v,s=Game.roll_dice(20)
            sum_val=v+attack.speed
            if sum_val>attacked.armor_rating:
                val, side = Game.roll_dice(6)
                damage = val + attack.power
                attacked.hp-=damage
                if attacked.hp<=0:
                    return "the play finish"
                else:
                    attack,attacked=attacked,attack


