from game import Game
from core.player import Player
def main():
    start=Game.start()
    if start == "exit":
        return "exit from the game"
    player_1=Player("david","fighter")
    monster_1=Game.choose_random_monster()
    print(type(monster_1))
    Game.battle(player_1,monster_1)

if __name__=="__main__":
    print(main())








