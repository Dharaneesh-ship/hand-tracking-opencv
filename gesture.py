import os
import warnings
import logging
import sys
import cv2
import mediapipe as mp

# Fix TensorFlow & MediaPipe Warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3" 
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  
warnings.filterwarnings("ignore") 
logging.getLogger("tensorflow").setLevel(logging.ERROR) 
sys.stderr = open(os.devnull, "w") 

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Define fingertip landmarks and their names
FINGERTIPS = {
    4: "Thumb Tip",
    8: "Index Tip",
    12: "Middle Tip",
    16: "Ring Tip",
    20: "Pinky Tip"
}

# OpenCV Video Capture
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5,
    max_num_hands=2  
) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR to RGB (MediaPipe requires RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        # Draw hand landmarks if detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Highlight fingertips and display names
                for idx, name in FINGERTIPS.items():
                    landmark = hand_landmarks.landmark[idx]
                    x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                    
                    # Draw red circles for fingertips
                    cv2.circle(frame, (x, y), 8, (0, 0, 255), -1)
                    
                    # Display names in green
                    cv2.putText(frame, name, (x + 10, y - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Display the output
        cv2.imshow("Fingertip Detection with Names", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
