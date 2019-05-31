import gym
from gym import spaces
import pyglet
import numpy as np

from .pokercard import DouDizhuCard, CardSpecial, CardRank, Card, CardSuit
from .player import PLayer


class GameState(object):
    def __init__(self):
        self.card_num = 1 * 54
        self.round = 0
        self.player_states = []

class DouDizhuEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }
    def __init__(self):
        self.state = GameState()
        self.viewer = None
        pass

    def addPlayer(self, seat_id, stack):
        pass
    
    def step(self, action):
        reward = 0
        done = False
        return self.state, reward, done, {}
    
    def reset(self):
        return self.state
        
    def render(self, mode='human'):
        screen_width = 600
        screen_height = 600

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)

            def draw_card(card, pos):
                upline = rendering.Line((pos[0],pos[1]), (pos[0] + 22, pos[1]))
                downline = rendering.Line((pos[0] + 22,pos[1] + 44), (pos[0], pos[1] + 44))
                leftline = rendering.Line((pos[0],pos[1] + 44), (pos[0], pos[1]))
                rightline = rendering.Line((pos[0] + 22,pos[1]), (pos[0] + 22, pos[1] + 44))

                self.viewer.add_geom(upline)
                self.viewer.add_geom(downline)
                self.viewer.add_geom(leftline)
                self.viewer.add_geom(rightline)

                if card.suit == CardSuit.SuitHearts:
                    suit = rendering.Image('doudizhu/resource/h.PNG', 18, 18)

                suit_tran = rendering.Transform(translation=(pos[0] + 11, pos[1] + 11))
                suit.add_attr(suit_tran)
                suit.set_color(255,255,255)

                self.viewer.add_geom(suit)

            draw_card(DouDizhuCard('Ah'), (100,100))

            
        return self.viewer.render(return_rgb_array=mode == 'rgb_array')
        
    def close(self):
        return None


    # catalog
    def _is_solo(self, cards):
        return len(cards) == 1

    def _is_pair(self, cards):
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
                if cards[i].special != CardSpecial.CardNone:
                    return False
            return True
        return False

    def _is_rocket(self, cards):
        if len(cards) == 2:
            if cards[0].special == CardSpecial.CardBlackJoker and \
                cards[1].special == CardSpecial.CardColoredJoker or \
                    cards[0].special == CardSpecial.CardColoredJoker and \
                        cards[1].special == CardSpecial.CardBlackJoker:
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
    env = gym.make('GridWorld-v1')
    env.reset()
    env.render()
    env.close()