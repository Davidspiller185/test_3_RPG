import random

import core.orc


from core.goblin import Goblin
class Game:
    @staticmethod
    def start():
        decision=Game.show_menu()
        return decision
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
            monster_1=core.orc.Orc("mon","knife")
            return monster_1
        else:
            monster_1=Goblin("gob","sword")
            return monster_1
    @staticmethod
    def battle(player_1, monster_1):
        value,sides=Game.roll_dice(6)
        play=value+player_1.speed
        print(f"the play value roll is:{play}")
        val,side=Game.roll_dice(6)
        mon=val+monster_1.speed
        print(f"the monster value roll is:{mon}")
        max_val=max(play,mon)
        if (max_val==play) or (max_val==play and max_val==mon):
            player_1.attack(player_1, monster_1)

        else:
            monster_1.attack(monster_1,player_1)


    @staticmethod
    def roll_dice(sides:int):
        value=random.randint(1 ,sides)
        return value,sides


