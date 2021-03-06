import gym
from gym import spaces
import pyglet
import numpy as np
import uuid
import random

from .pokercard import DouDizhuCard, CardSpecial, CardRank, Card, CardSuit
from .player import PLayer


class MultiAgentEnv(gym.Env):

    def step(self, action_n):
        obs_n    = list()
        reward_n = list()
        done_n   = list()
        info_n   = {'n': []}
        # ...
        return obs_n, reward_n, done_n, info_n

class DouDizhuEnv(MultiAgentEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }
    def __init__(self):
        self.n_cards = 1 * 54
        self.n_players = 3
        self.n_bid_score = 4
        self.n_pocket_cards = 20
        self.n_round_limit = self.n_cards

        self.round = 0
        self.cur_player = 0
        self.last_cards = None
        self.player_states = []

        self.observation_space = spaces.Dict({
            'player_states':
                spaces.Dict(
                    {
                        'player_infos':
                            spaces.Dict({
                                'bid_score':
                                    spaces.Tuple(
                                        [spaces.Discrete(self.n_bid_score)] * self.n_players
                                    ),
                                'landlord':
                                    spaces.Discrete(self.n_players),
                                'left_cards':
                                    spaces.Tuple(
                                        [spaces.Discrete(self.n_cards)] * self.n_players
                                    )
                            }),
                        'player_hands':
                            spaces.MultiBinary(self.n_cards)
                    }
                )
            ,
            'round':
                spaces.Discrete(self.n_round_limit),
            'game_stage':
                spaces.Discrete(self.n_players)
        })

        self.action_space = spaces.Tuple([spaces.MultiBinary(self.n_cards), spaces.Discrete(self.n_bid_score)])
        self.viewer = None
        pass

    def add_player(self, seat_id, name='player'):
        p = PLayer(uuid.uuid4(), seat_id)
        p.set_name(name)
        self.player_states.append(p)
    
    def _get_obs(self, player_id):
        pass

    def step(self, action):
        
        # bid or play update env
        if self.round == 0:
            action = action[1]
            if action < 0 or action >= 4:
                print("invalid bid score")
                return
            self.player_states[self.cur_player].set_bid_score(action)
        else:
            action = action[0]

            for each_card in action:
                if each_card in self.player_states[self.cur_player].hand:
                    self.player_states[self.cur_player].hand.remove(each_card)
                else:
                    print("invalid action, card no found in player's hand")
                    return

        # reward
        reward = [0] * self.n_players
        for i, each_player in enumerate(self.player_states):
            if each_player.left_cards_num() == 0:
                done = True

                reward = [-1 for _each in reward]
                reward[i] = 1
                break

        # switch player
        self.cur_player = self.cur_player + 1
        if self.cur_player == self.n_players:
            self.cur_player = 0
            self.round += 1
        return self.observation_space, reward, done, {}
    
    def reset(self):
        return self.observation_space
        
    def render(self, mode='human'):
        print('round:{round}'.format(round=self.round))
        
    def close(self):
        return None

    def dealt_card(self, cards):
        player_num = len(self.player_states)
        dealt_round = 0
        for each in cards:
            self.player_states[dealt_round%player_num].hand.append(each)
            dealt_round += 1

    def _make_action_space(self):
        
        ret = None

        return ret

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