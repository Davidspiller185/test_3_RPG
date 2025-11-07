from core.PlayerGame import PlayerGame
from game import Game
class Player(PlayerGame):

    def __init__(self,name:str,profession:str,speed=7,power=6,armor_rating=14,hp=50):
        super().__init__(name,hp,speed,power,armor_rating)
        self.profession=profession

    def speak(self):
        print(f"{self.name} say i play in the game")

    def attack(self,attack,attacked):
        while attack.hp>0 and attacked.hp>0:
            v,s=Game.roll_dice(20)
            sum_val=v+attack.speed
            print(f"the sum val is:{sum_val}")
            if sum_val>attacked.armor_rating:
                val, side = Game.roll_dice(6)
                damage = val + attack.power
                print(f"the damage is:{damage}")
                attacked.hp-=damage
                print(f"the hp of the attacked is:{attacked.hp}")
                if attacked.hp<=0:
                     print("the play finish")
                else:
                    self.attack(attacked,attack)


