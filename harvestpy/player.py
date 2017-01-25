class Player(object):
    def __init__(self, max_moves=20, gold=1000, name='player'):
        self.max_moves = max_moves
        self.gold = gold
        self.name = name
        self.aval_moves = self.max_moves
        
    def _do_move(self, power=1):
        '''Do a move
        checks if a move with a set power can be done
        Returns true if done false if otherwise
        '''
        if self.aval_moves > power:
            self.aval_moves -= power
            return True
        else:
            return False
    
    def _sleep(self):
        self.aval_moves = self.max_moves
        return 'Player: [{}] slept'.format(self.name)
        
    def __repr__(self):
        return '<Player name: {name}, aval_moves: {aval}, max_moves: {max_moves}, gold: {gold}>'.format(name = self.name, max_moves = self.max_moves, gold = self.gold, aval=self.aval_moves)