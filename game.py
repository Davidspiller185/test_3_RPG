import random

from core.orc import Orc
from core.goblin import Goblin
class Game:
    @staticmethod
    def start():
        decision=Game.show_menu()
        if decision=="exit":
            print("exit from the game")
            return
    @staticmethod
    def show_menu():
        choice=input("if you want to play press:play, if you want to exit press:exit")
        while choice!="play" and choice!="exit":
            choice = input("if you want to play press:play, if you want to exit press:exit")
        return choice
    @staticmethod
    def choose_random_monster():
        monster=random.randint(0,1)
        if 0<=monster<=0.5:
            monster_1=Orc("mon","knife",)
            return monster_1
        else:
            monster_2=Goblin("gob","sword")
            return monster_2
    @staticmethod
    def battle(player, monster):
        value,sides=Game.roll_dice(6)
        play=value+player.speed
        val,side=Game.roll_dice(6)
        mon=val+monster.speed
        max_val=max(play,mon)
        if (max_val==play) or (max_val==play and max_val==mon):
            attack_return=player.attack(player, monster)
            return attack_return

        else:
            attack_return=monster.attack(monster,player)





        elif max_val==mon:
            monster.attack(monster,player)




    @staticmethod
    def roll_dice(sides):
        value=random.randint(1,sides)
        return value,sides


