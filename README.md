# Hand Landmark Detection using Computer Vision

## Project Overview
This project implements a real-time hand landmark detection system using computer vision algorithms. The system utilizes MediaPipe and OpenCV to detect hand landmarks, focusing on fingertips and joints, and displays the detected landmarks in a live video stream.

## Problem Statement
Implement a system that detects hand landmarks (e.g., fingertips, joints) using computer vision algorithms.

## Features
- **Real-time Hand Landmark Detection**: Detects hand landmarks using MediaPipe's pre-trained model.
- **Fingertip Highlighting**: Identifies and highlights fingertips with red circles.
- **Landmark Labeling**: Displays names of detected fingertips on the video feed.
- **Supports Multiple Hands**: Can detect up to two hands simultaneously.
- **Efficient Processing**: Uses optimized settings to minimize latency.

## Technologies Used
- **OpenCV**: For video capture and real-time processing.
- **MediaPipe**: For hand landmark detection.
- **Python**: Main programming language.

## Setup & Installation

### Prerequisites
Ensure you have the required dependencies installed:

```bash
pip install opencv-python mediapipe numpy
```

### Running the Program
1. Connect a webcam to your system.
2. Run the script:

   ```bash
   python hand_landmark_detection.py
   ```

3. A window will open displaying the detected hand landmarks in real-time.
4. Press 'q' to exit the program.

## Output & Visualization
- The system detects hands and marks landmarks in real-time.
- Fingertips are highlighted with red circles.
- Labels for detected fingertips are displayed in green.
- The processed video feed is shown in an OpenCV window.

## Future Enhancements
- Implement gesture recognition using detected landmarks.
- Support for hand pose classification.
