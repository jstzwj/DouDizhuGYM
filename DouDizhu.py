import gym
from gym import spaces
import numpy as np

class DouDizhuEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }
    '''
    A-1,2-,3-3,4-4,5-5,6-6,7-7,8-8,9-9,10-10,J-11,Q-12,K-13
    black_joker-14,red_joker-15
    '''
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