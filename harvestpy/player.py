class Player(object):
    def __init__(self, max_moves=20, gold=1000, name='player'):
        self.max_moves = max_moves
        self.gold = gold
        self.name = name
        self.aval_moves = self.max_moves
    def __repr__(self):
        return '<Player name: {name}, aval_moves: {aval}, max_moves: {max_moves}, gold: {gold}>'.format(name = self.name, max_moves = self.max_moves, gold = self.gold, aval=self.aval_moves)