import gym
from gym import spaces
import numpy as np

import pokercard



class DouDizhuEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }
    def __init__(self):
        self.card_num = 1 * 54
        self.round = 0
        self.player_states = []
        
        pass

    def addPlayer(self, seat_id, stack):
        pass
    
    def step(self, action):
        return self.state, reward, done, {}
    
    def reset(self):
        return self.state
        
    def render(self, mode='human'):
        return None
        
    def close(self):
        return None

    def _is_single(self, cards):
        return len(cards) == 1

    def _is_double(self, cards):
        return len(cards) == 2 and cards[0] == cards[1]
    
    def _is_triple(self, cards):
        if len(cards) == 3:
            if cards[0] == cards[1] and cards[1] == cards[2]:
                return True
        return False
    
    def _is_triple_one(self, cards):
        if len(cards) == 4:
            unique = list(set(cards))
            if len(unique) == 2:
                if cards.count(unique[0]) == 3 and cards.count(unique[1]) == 1 \
                    or cards.count(unique[0]) == 1 and cards.count(unique[1]) == 3:
                    return True
        return False

    def _is_triple_two(self, cards):
        if len(cards) == 5:
            unique = list(set(cards))
            if len(unique) == 2:
                if cards.count(unique[0]) == 3 and cards.count(unique[1]) == 2 \
                    or cards.count(unique[0]) == 2 and cards.count(unique[1]) == 3:
                    return True
        return False

    def _is_chain(self, cards):
        if len(cards) >= 5:
            cards.sort()
            for i in range(len(cards)):
                if i != 0:
                    if cards[i+1] != cards[i].next():
                        return False
                if cards[i].special != pokercard.CardSpecial.CardNone:
                    return False
            return True
        return False

    def _is_rocket(self, cards):
        if len(cards) == 2:
            if cards[0].special == pokercard.CardSpecial.CardBlackJoker and \
                cards[1].special == pokercard.CardSpecial.CardColoredJoker or \
                    cards[0].special == pokercard.CardSpecial.CardColoredJoker and \
                        cards[1].special == pokercard.CardSpecial.CardBlackJoker:
                return True

        return False

    def _is_bomb(self, cards):
        if len(cards) > 4:
            first = cards[0]
            for each in cards:
                if each != first:
                    return False
            return True
        return False

if __name__ == "__main__":
    pass