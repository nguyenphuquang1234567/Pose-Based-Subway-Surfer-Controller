# 🕹️ Pose-Based Subway Surfer Controller

Control the game **Subway Surfer** using your body movements detected through webcam, powered by **MediaPipe Pose** and **OpenCV**.

## 🎮 Controls

| Body Movement                        | Game Action      |
|-------------------------------------|------------------|
| 🤸 Lean to the left                  | Move left (`←`)  |
| 🤸‍♂️ Lean to the right               | Move right (`→`) |
| 🙌 Raise both hands above your head | Jump (`↑`)       |
| 🤐 Bend down / lower your head       | Slide (`↓`)      |

> Each action is throttled with a 0.5-second delay to prevent spamming.

---

## ▶️ How to Run

1. **Install required libraries:**

```bash
pip install opencv-python mediapipe pyautogui numpy
```
⚙️ Requirements
Python 3.7+

Working webcam

Desktop environment (required by PyAutoGUI to send keyboard events)

Subway Surfer running in an Android emulator (e.g., LDPlayer, BlueStacks)

💡 Tips
Make sure the emulator window is focused to receive key presses.

Stay centered in the webcam frame for accurate pose detection.

You can tweak the detection thresholds and delay to better suit your body type or responsiveness.

🛠 Technologies Used
MediaPipe Pose

OpenCV

PyAutoGUI

Python 3

🧠 Project Idea
This fun project connects computer vision with game interaction, using real-time body tracking to simulate keyboard input — perfect for exploring pose estimation and hands-free control.

