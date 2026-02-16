---
description: How to run TensorBoard to visualize RL training results
---

# TensorBoard Visualization Workflow

This workflow shows you how to visualize your Stable Baselines3 training results using TensorBoard.

## Prerequisites

- You've already trained your RL model with tensorboard logging enabled
- You have a tensorboard log directory (e.g., `ppo_car_racing_tensorboard/`)

## Step 1: Install TensorBoard (One-time setup)

If TensorBoard is not already installed in your environment:

```bash
pip install tensorboard
```

**Note:** This only needs to be done once per environment. If you're using a conda/virtual environment, make sure it's activated first.

## Step 2: Launch TensorBoard

Navigate to your project directory and run:

```bash
tensorboard --logdir=<your_log_directory> --port=6006
```

**Example:**
```bash
tensorboard --logdir=ppo_car_racing_tensorboard --port=6006
```

**What this does:**
- `--logdir`: Points to the directory containing your `.tfevents` files
- `--port=6006`: Specifies which port to run TensorBoard on (6006 is default)

**Expected output:**
```
TensorFlow installation not found - running with reduced feature set.
Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.11.2 at http://localhost:6006/ (Press CTRL+C to quit)
```

## Step 3: Open TensorBoard in Your Browser

Open your web browser (Chrome, Firefox, Edge, etc.) and navigate to:

```
http://localhost:6006/
```

## Step 4: View Your Training Metrics

Once TensorBoard loads:

1. **Click on the "Scalars" tab** - This shows all numerical metrics over time
2. **Key plots to look for:**
   - `rollout/ep_rew_mean` - Average episode reward (main metric for your report)
   - `rollout/ep_len_mean` - Average episode length
   - `train/learning_rate` - Learning rate over time
   - `train/loss` - Training loss
   - `train/policy_loss` - Policy network loss
   - `train/value_loss` - Value network loss

3. **Other useful tabs:**
   - `Images` - If you logged any images during training
   - `Graphs` - Neural network architecture visualization
   - `Distributions` - Weight/activation distributions

## Step 5: Export Plots for Your Report

To save plots for your deliverable:

### Method 1: Screenshot
- Take screenshots of the important plots
- Use Windows Snipping Tool (Win + Shift + S) or similar

### Method 2: Download from TensorBoard
- Hover over a plot
- Click the download icon (usually bottom-left of the plot)
- Save as PNG or SVG

### Method 3: Export Data as CSV
- Click the three dots menu on a plot
- Select "Download CSV" to get raw data
- Use this to create custom plots in Python/Excel

## Step 6: Stop TensorBoard

When you're done viewing:

- Go back to your terminal/PowerShell
- Press `Ctrl + C` to stop the TensorBoard server

## Understanding the Log Files

Your tensorboard directory structure looks like:
```
ppo_car_racing_tensorboard/
└── PPO_1/
    └── events.out.tfevents.1770892209.Leywin.23592.0
```

- **PPO_1/** - Algorithm name and run number
- **events.out.tfevents.*** - Binary log files (don't open directly!)
- TensorBoard reads these files and generates the visualizations

## Tips

1. **Multiple runs:** If you train multiple times, each run will appear as a separate line in TensorBoard, making it easy to compare experiments
2. **Refresh:** TensorBoard auto-refreshes as new data is written during training
3. **Smoothing:** Use the smoothing slider in TensorBoard to reduce noise in plots
4. **Custom port:** If port 6006 is busy, use a different port: `--port=6007`

## Common Issues

**Issue:** `tensorboard: command not found`
- **Solution:** Install tensorboard: `pip install tensorboard`

**Issue:** Port already in use
- **Solution:** Use a different port: `tensorboard --logdir=... --port=6007`

**Issue:** No data showing in TensorBoard
- **Solution:** Check that your log directory path is correct and contains `.tfevents` files

## For Your Deliverable

To complete your assignment requirements:

1. ✅ Run baseline RL algorithm (PPO) on Car Racing environment
2. ✅ Generate tensorboard logs during training
3. ✅ Launch TensorBoard to view results
4. 📸 Export reward over time plot
5. 📝 Write one-page report including:
   - Link to GitHub repo
   - Reward over time plot
   - Analysis of results
   - Any other relevant plots (episode length, loss, etc.)
