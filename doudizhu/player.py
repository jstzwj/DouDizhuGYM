

class PLayer(object):
    def __init__(self, player_id, stack =2000):
        self.player_id = player_id

        self.hand = []
        self.stack = stack
        self.seat = -1