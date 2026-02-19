import os
import gymnasium
from stable_baselines3 import PPO
import gym

# Custom wrapper to make gymnasium environments compatible with stable-baselines3
class GymnasiumWrapper(gym.Env):
    def __init__(self, gym_env):
        self.gym_env = gym_env
        self.action_space = self._convert_space(gym_env.action_space)
        self.observation_space = self._convert_space(gym_env.observation_space)
        
    def _convert_space(self, space):
        """Convert gymnasium space to gym space"""
        if isinstance(space, gymnasium.spaces.Box):
            return gym.spaces.Box(
                low=space.low, 
                high=space.high, 
                shape=space.shape, 
                dtype=space.dtype
            )
        elif isinstance(space, gymnasium.spaces.Discrete):
            return gym.spaces.Discrete(n=space.n)
        else:
            return space
    
    def reset(self, **kwargs):
        obs, info = self.gym_env.reset(**kwargs)
        return obs
    
    def step(self, action):
        obs, reward, terminated, truncated, info = self.gym_env.step(action)
        done = terminated or truncated
        return obs, reward, done, info
    
    def render(self, mode='human'):
        return self.gym_env.render()
    
    def close(self):
        return self.gym_env.close()

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the script
log_path = os.path.join(script_dir, "tensorboard_logs")
model_path = os.path.join(script_dir, "ppo_car_racing")

# Create the gymnasium environment
gym_env = gymnasium.make("CarRacing-v2")

# Wrap it for compatibility with stable-baselines3
env = GymnasiumWrapper(gym_env)

# Instantiate the agent
model = PPO("CnnPolicy", env, verbose=1, tensorboard_log=log_path)

# Train the agent
model.learn(total_timesteps=10000)

# Save the model
model.save(model_path)