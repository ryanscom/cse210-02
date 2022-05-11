from game.director import Director
from game.introduction import Introduction

full_name = Introduction()
full_name.get_name()

director = Director()
director.start_game()
