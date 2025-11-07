from core.PlayerGame import PlayerGame
import game
class Goblin(PlayerGame):
    def __init__(self,name:str,weapon:str, speed=8,power=7,typ="goblin",hp=20,armor_rating=1):
        super().__init__(name,hp,speed,power,armor_rating)
        self.type=typ
        self.weapon=weapon
    def speak(self):
        print(f"{self.type}{self.name} is not happy")


    def attack(self,attack, attacked):
        while attack.hp > 0 and attacked.hp > 0:
            v, s = game.Game.roll_dice(20)
            sum_val = v + attack.speed
            print(f"the sum val is:{sum_val}")
            if sum_val > attacked.armor_rating:
                val, side = game.Game.roll_dice(6)
                damage = val + attack.power
                print(f"the damage is:{damage}")
                if type(attack) is Goblin:
                    if attack.weapon == "knife":
                        damage = damage * 0.5
                        print(f"the damage is:{damage}")
                    elif attack.weapon == "sword":
                        damage = damage
                        print(f"the damage is:{damage}")
                    elif attack.weapon == "ax":
                        damage = damage * 1.5
                        print(f"the damage is:{damage}")
                attacked.hp -= damage
                print(f"the hp of the attacked is:{attacked.hp}")
                if attacked.hp <= 0:
                     print("the play finish")
            else:
                self.attack(attacked,attack)



