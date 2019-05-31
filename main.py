import gym
import doudizhu
import numpy as np

if __name__ == "__main__":
    env = gym.make('DouDizhuEnv-v0')
    env.reset()
    while True:
        state, reward, done, debug = env.step(None)
        if done:
            break
        env.render()
    env.close()