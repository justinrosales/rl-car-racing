# Car Racing Reinforcement Learning

A benchmarking project for training autonomous agents in the **Gymnasium CarRacing-v2** environment using various Reinforcement Learning (RL) algorithms.

## How it Works

### 1. The Playground: CarRacing-v2
The project uses the **Gymnasium** toolkit to load the `CarRacing-v2` environment. In this simulation, the car receives rewards for visiting new track tiles and penalties for driving off-road or moving too slowly. The "input" the AI interprets is a top-down pixel image (96x96 RGB) of the car and the track.

### 2. The Brain: Deep Reinforcement Learning
Instead of manual programming (like "if you see green, turn left"), the agents use algorithms from the **Stable Baselines3** library. This is a deep learning approach where:
*   **Exploration**: The agent starts by driving randomly to explore the environment.
*   **Feedback**: It receives a numerical "reward" based on its performance.
*   **Vision**: It uses a **Convolutional Neural Network (CNN)** to process the visual pixels and determine which actions (steering, gas, braking) lead to the highest cumulative scores.

### 3. The Workflow
Across all algorithms in this project, the implementation follows a consistent process:
*   **Environment Wrapping**: A wrapper ensures the Gymnasium environment is compatible with the learning library's API.
*   **Training**: The `model.learn()` command runs the car through the track for thousands of steps to optimize its driving policy.
*   **Persistence**: Once training is complete, the learned "intelligence" is saved as a `.zip` file for later evaluation without needing to retrain.
*   **Monitoring**: Training metrics are exported to **TensorBoard** to visualize performance improvements and stability over time.

---

## Project Structure
- `ppo_car_racing/`: PPO algorithm implementation and models.
- `a2c_car_racing/`: A2C algorithm implementation and models.
- `docs/`: Technical guides and performance analysis.

## Key Technologies
- **Gymnasium**: The environment standard.
- **Stable-Baselines3**: Reliable implementation of RL algorithms.
- **TensorBoard**: Metric visualization and benchmarking.
- **PyTorch**: Deep learning backend.

## Documentation
- [**Installation & Usage Guide**](./docs/usage.md): How to setup, train, and test models.
- [**TensorBoard Workflow**](./docs/tensorboard.md): How to visualize and compare training results.
