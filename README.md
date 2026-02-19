# Car Racing RL

Training autonomous agents to drive in the **Gymnasium CarRacing-v2** environment using Stable Baselines3.

## How it Works

### 1. Playground: CarRacing-v2
The project uses the **Gymnasium** toolkit to load the `CarRacing-v2` environment. In this simulation, the car receives rewards for visiting new track tiles and penalties for driving off-road or moving too slowly. The "input" the AI interprets is a top-down pixel image (96x96 RGB) of the car and the track.

### 2. Brain: Deep Reinforcement Learning
Instead of manual programming (like "if you see green, turn left"), the agents use algorithms from the **Stable Baselines3** library. This is a deep learning approach where:
*   **Exploration**: The agent starts by driving randomly to explore the environment.
*   **Feedback**: It receives a numerical "reward" based on its performance.
*   **Vision**: It uses a **Convolutional Neural Network (CNN)** to process the visual pixels and determine which actions (steering, gas, braking) lead to the highest cumulative scores.

### 3. Workflow
Across all algorithms in this project, the implementation follows a consistent process:
*   **Environment Wrapping**: A wrapper ensures the Gymnasium environment is compatible with the learning library's API.
*   **Training**: The `model.learn()` command runs the car through the track for thousands of steps to optimize its driving policy.
*   **Persistence**: Once training is complete, the learned "intelligence" is saved as a `.zip` file for later evaluation without needing to retrain.
*   **Monitoring**: Training metrics are exported to **TensorBoard** to visualize performance improvements and stability over time.

---

## Project Structure
- `src/ppo/`: PPO training script and saved models.
- `src/a2c/`: A2C implementation (In-progress).
- `docs/`: Setup and usage guides.

## Tech Stack
- **Gymnasium**: Environment toolkit.
- **Stable-Baselines3**: RL algorithms.
- **PyTorch**: Deep learning backend.
- **TensorBoard**: Benchmarking & visualization.

## Links
- [**Installation & Usage Guide**](./docs/usage.md)
- [**TensorBoard Workflow**](./docs/tensorboard.md)
