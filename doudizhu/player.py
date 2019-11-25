

class PLayer(object):
    def __init__(self, player_id, seat_id):
        self.player_id = player_id

        self.hand = []
        self.seat = seat_id
        self.is_landlord = False
        self.bid_score = 0

    def set_name(self, name):
        self.name = name

    def set_bid_score(self, score):
        self.bid_score = score

    def set_landlord(self, is_landlord = True):
        self.is_landlord = is_landlord

    def set_seat(self, seat):
        self.seat = seat

    def left_cards_num(self):
        return len(self.hand)

    
        