from . player import Player

class Game(object):
    def __init__(self, players = [Player()]):
        self.players = players
        self.day = 1
    
    def sleep(self):
        for i in self.players:
            i._sleep()
        self.day += 1
        