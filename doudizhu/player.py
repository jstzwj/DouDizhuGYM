

class PLayer(object):
    def __init__(self, player_id, seat_id):
        self.player_id = player_id

        self.hand = []
        self.seat = seat_id
        self.is_landlord = False
        self.bid_score = 0

    def set_name(self, name):
        self.name = name
        