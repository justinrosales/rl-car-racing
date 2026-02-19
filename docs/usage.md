# Running the Algorithms

Detailed instructions for training and evaluating reinforcement learning agents in the CarRacing-v2 environment.

## 1. Prerequisites

Ensure you have the required dependencies installed:
```bash
pip install gymnasium[box2d] stable-baselines3 shimmy tensorboard torch
```

## 2. PPO (Proximal Policy Optimization)

### Training
To start training the PPO agent:
```bash
python ppo_car_racing/src/ppo_car_racing.py
```

### Monitoring
Logs are saved in `ppo_car_racing/src/ppo_car_racing_tensorboard/`. You can view them with:
```bash
tensorboard --logdir=ppo_car_racing/src/ppo_car_racing_tensorboard/
```

---

## 3. A2C (Advantage Actor Critic)

### Training
Once the implementation is complete, run:
```bash
python a2c_car_racing/src/a2c_car_racing.py
```

### Monitoring
Logs will be saved in the corresponding `src/` directory. View them with:
```bash
tensorboard --logdir=a2c_car_racing/src/a2c_car_racing_tensorboard/
```

## 4. Evaluation
After training, the models are saved as `.zip` files. To evaluate a trained model, load it within your script:
```python
from stable_baselines3 import PPO
model = PPO.load("ppo_car_racing/src/ppo_car_racing")
```
