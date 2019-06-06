import gym
import doudizhu
import numpy as np
import random

if __name__ == "__main__":
    env = gym.make('DouDizhuEnv-v0')
    env.reset()
    # add players
    env.add_player(0, name='Wang')
    env.add_player(1, name='Li')
    env.add_player(2, name='Zhao')

    # dealt cards
    cards = list(range(0,54))
    random.shuffle(cards)
    env.dealt_card(cards[3:])

    while True:
        state, reward, done, debug = env.step(None)
        if done:
            break
        env.render()
    env.close()