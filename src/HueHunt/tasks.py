from live_game.views import complete_live_games, create_new_games


# to complete games
def complete_games():
    print("completing games task running")
    complete_live_games()
    print("completing games task completed")


# to create new games
def add_games():
    print("creating new games task running")
    create_new_games()
    print("creating new games task completed")
