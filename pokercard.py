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
    def __init__(self, desc):
        self.rank = CardRank.CardNone
        self.suit = CardSuit.SuitNone
        self.special = CardSpecial.CardNone

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



if __name__ == "__main__":
    card = Card('th')
    print(card)


        
