if __name__=="__main__":
    from game import Game
    from core.player import Player
    Game.start()
    player_1=Player("david","fighter")
    monster_1=Game.choose_random_monster()
    game=Game.battle(player_1,monster_1)
    print(game)








