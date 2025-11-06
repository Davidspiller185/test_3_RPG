if __name__=="main":
    from game import Game
    from core.player import Player
    Game.start()
    player_1=Player("david","fighter")
    monster_1=Game.choose_random_monster()
    Game.battle(player_1,monster_1)







