

class PLayer(object):
    def __init__(self, player_id, stack =2000):
        self.player_id = player_id

        self.hand = []
        self.seat = -1
        self.is_landlord = False
        self.bid_score = 0
        