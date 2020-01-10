from gym.envs.registration import load

from maml_rl.envs.utils.normalized_env import NormalizedActionWrapper

def mujoco_wrapper(entry_point, **kwargs):
    # Load the environment from its entry point
    env_cls = load(entry_point)
    env = env_cls(**kwargs)
    # Normalization wrapper
    env = NormalizedActionWrapper(env, scale=10.)
    return env
