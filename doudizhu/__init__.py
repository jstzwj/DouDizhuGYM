from gym.envs.registration import register

register(
    id='DouDizhuEnv-v0',
    entry_point='doudizhu.env:DouDizhuEnv',
)