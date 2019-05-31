from enum import Enum, unique
'''
    A-1,2-2,3-3,4-4,5-5,6-6,7-7,8-8,9-9,10-10,J-11,Q-12,K-13
    black_joker-14,colored_joker-15
'''

@unique
class CardRank(Enum):
    CardNone = -1
    CardA = 1
    Card2 = 2
    Card3 = 3
    Card4 = 4
    Card5 = 5
    Card6 = 6
    Card7 = 7
    Card8 = 8
    Card9 = 9
    CardT = 10
    CardJ = 11
    CardQ = 12
    CardK = 13

@unique
class CardSuit(Enum):
    SuitNone = -1
    SuitHearts = 1
    SuitSpades =  2
    SuitClubs = 3
    SuitDiamonds = 4

@unique
class CardSpecial(Enum):
    CardNone = -1
    CardBlackJoker = 1
    CardColoredJoker = 2

class Card(object):
    def __init__(self, desc=None):
        self.rank = CardRank.CardNone
        self.suit = CardSuit.SuitNone
        self.special = CardSpecial.CardNone
        if desc is not None:
            desc = desc.strip().upper()
            if len(desc) != 2:
                print("card description is incorrect")
            
            if desc[0] == 'A':
                self.rank = CardRank.CardA
            elif desc[0] == '2':
                self.rank = CardRank.Card2
            elif desc[0] == '3':
                self.rank = CardRank.Card3
            elif desc[0] == '4':
                self.rank = CardRank.Card4
            elif desc[0] == '5':
                self.rank = CardRank.Card5
            elif desc[0] == '6':
                self.rank = CardRank.Card6
            elif desc[0] == '7':
                self.rank = CardRank.Card7
            elif desc[0] == '8':
                self.rank = CardRank.Card8
            elif desc[0] == '9':
                self.rank = CardRank.Card9
            elif desc[0] == 'T':
                self.rank = CardRank.CardT
            elif desc[0] == 'J':
                self.rank = CardRank.CardJ
            elif desc[0] == 'Q':
                self.rank = CardRank.CardQ
            elif desc[0] == 'K':
                self.rank = CardRank.CardK

            
            if desc[0] == 'S':
                if desc[1] == 'C':
                    self.special == CardSpecial.CardColoredJoker
                elif desc[1] == 'B':
                    self.special == CardSpecial.CardBlackJoker
            else:
                if desc[1] == 'H':
                    self.suit = CardSuit.SuitHearts
                elif desc[1] == 'S':
                    self.suit = CardSuit.SuitSpades
                elif desc[1] == 'C':
                    self.suit = CardSuit.SuitClubs
                elif desc[1] == 'D':
                    self.suit = CardSuit.SuitDiamonds

    def __str__(self):
        ret = ""
        if self.rank == CardRank.CardA:
            ret = 'A'
        elif self.rank == CardRank.Card2:
            ret = '2'
        elif self.rank == CardRank.Card3:
            ret = '3'
        elif self.rank == CardRank.Card4:
            ret = '4'
        elif self.rank == CardRank.Card5:
            ret = '5'
        elif self.rank == CardRank.Card6:
            ret = '6'
        elif self.rank == CardRank.Card7:
            ret = '7'
        elif self.rank == CardRank.Card8:
            ret = '8'
        elif self.rank == CardRank.Card9:
            ret = '9'
        elif self.rank == CardRank.CardT:
            ret = 'T'
        elif self.rank == CardRank.CardJ:
            ret = 'J'
        elif self.rank == CardRank.CardQ:
            ret = 'Q'
        elif self.rank == CardRank.CardK:
            ret = 'K'

        if self.special == CardSpecial.CardColoredJoker:
            ret = 'Colored Joker'
        elif self.special == CardSpecial.CardBlackJoker:
            ret = 'Black Joker'
        else:
            if self.suit == CardSuit.SuitHearts:
                ret += '♥'
            elif self.suit == CardSuit.SuitSpades:
                ret += '♠'
            elif self.suit == CardSuit.SuitClubs:
                ret += '♣'
            elif self.suit == CardSuit.SuitDiamonds:
                ret += '♦'
        
        return ret

    def __eq__(self, other):
        if self.rank == other.rank and \
            self.suit == other.suit and \
                self.special == other.special:
                return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)



class DouDizhuCard(Card):
    def __init__(self, desc=None):
        super(DouDizhuCard, self).__init__(desc)

    def __gt__(self, other):
        DouDizhuRank.gt(self, other)

    def __lt__(self, other):
        DouDizhuRank.lt(self, other)

    def __ge__(self, other):
        DouDizhuRank.ge(self, other)

    def __le__(self, other):
        DouDizhuRank.le(self, other)

    def __eq__(self, other):
        if self.rank == other.rank and \
            self.special == other.special:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def next(self):
        ret = DouDizhuCard()
        
        if self.rank == CardRank.CardA:
            ret.suit = self.suit
            ret.rank = CardRank.Card2
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card2:
            ret.suit = CardSuit.SuitNone
            ret.rank = CardRank.CardNone
            ret.special = CardSpecial.CardBlackJoker
        elif self.rank == CardRank.Card3:
            ret.suit = self.suit
            ret.rank = CardRank.Card4
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card4:
            ret.suit = self.suit
            ret.rank = CardRank.Card5
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card5:
            ret.suit = self.suit
            ret.rank = CardRank.Card6
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card6:
            ret.suit = self.suit
            ret.rank = CardRank.Card7
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card7:
            ret.suit = self.suit
            ret.rank = CardRank.Card8
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card8:
            ret.suit = self.suit
            ret.rank = CardRank.Card9
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card9:
            ret.suit = self.suit
            ret.rank = CardRank.CardT
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.CardT:
            ret.suit = self.suit
            ret.rank = CardRank.CardJ
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.CardJ:
            ret.suit = self.suit
            ret.rank = CardRank.CardQ
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.CardQ:
            ret.suit = self.suit
            ret.rank = CardRank.CardK
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.CardK:
            ret.suit = self.suit
            ret.rank = CardRank.CardA
            ret.special = CardSpecial.CardNone
    def prev(self):
        ret = DouDizhuCard()
        
        if self.rank == CardRank.CardA:
            ret.suit = self.suit
            ret.rank = CardRank.CardK
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card2:
            ret.suit = self.suit
            ret.rank = CardRank.CardJ
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card3:
            ret.suit = CardSuit.SuitNone
            ret.rank = CardRank.CardNone
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card4:
            ret.suit = self.suit
            ret.rank = CardRank.Card3
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card5:
            ret.suit = self.suit
            ret.rank = CardRank.Card4
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card6:
            ret.suit = self.suit
            ret.rank = CardRank.Card5
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card7:
            ret.suit = self.suit
            ret.rank = CardRank.Card6
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card8:
            ret.suit = self.suit
            ret.rank = CardRank.Card7
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.Card9:
            ret.suit = self.suit
            ret.rank = CardRank.Card8
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.CardT:
            ret.suit = self.suit
            ret.rank = CardRank.Card9
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.CardJ:
            ret.suit = self.suit
            ret.rank = CardRank.CardT
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.CardQ:
            ret.suit = self.suit
            ret.rank = CardRank.CardJ
            ret.special = CardSpecial.CardNone
        elif self.rank == CardRank.CardK:
            ret.suit = self.suit
            ret.rank = CardRank.CardQ
            ret.special = CardSpecial.CardNone

class DouDizhuRank(object):
    @staticmethod
    def card_to_int(card):        
        if card.rank == CardRank.CardA:
            return 14
        elif card.rank == CardRank.Card2:
            return 15
        elif card.rank == CardRank.Card3:
            return 3
        elif card.rank == CardRank.Card4:
            return 4
        elif card.rank == CardRank.Card5:
            return 5
        elif card.rank == CardRank.Card6:
            return 6
        elif card.rank == CardRank.Card7:
            return 7
        elif card.rank == CardRank.Card8:
            return 8
        elif card.rank == CardRank.Card9:
            return 9
        elif card.rank == CardRank.CardT:
            return 10
        elif card.rank == CardRank.CardJ:
            return 11
        elif card.rank == CardRank.CardQ:
            return 12
        elif card.rank == CardRank.CardK:
            return 13

        if card.special == CardSpecial.CardColoredJoker:
            return 15
        elif card.special == CardSpecial.CardBlackJoker:
            return 16
    @staticmethod
    def gt(lhs, rhs):
        return DouDizhuRank.card_to_int(lhs) > DouDizhuRank.card_to_int(rhs)

    @staticmethod
    def lt(lhs, rhs):
        return DouDizhuRank.card_to_int(lhs) < DouDizhuRank.card_to_int(rhs)

    @staticmethod
    def ge(lhs, rhs):
        return DouDizhuRank.card_to_int(lhs) >= DouDizhuRank.card_to_int(rhs)

    @staticmethod
    def le(lhs, rhs):
        return DouDizhuRank.card_to_int(lhs) <= DouDizhuRank.card_to_int(rhs)


if __name__ == "__main__":
    card = Card('th')
    print(card)


        
