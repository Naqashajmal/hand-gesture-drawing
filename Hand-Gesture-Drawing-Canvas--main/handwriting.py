import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize MediaPipe Drawing Utils
mp_drawing = mp.solutions.drawing_utils

# Set up the webcam
cap = cv2.VideoCapture(0)

# Create a blank canvas for drawing
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# To store the points for drawing
points = []

while True:
    # Capture the frame from the webcam
    ret, frame = cap.read()
    
    # Flip the frame horizontally for a mirror view
    frame = cv2.flip(frame, 1)
    
    # Convert the frame to RGB (MediaPipe uses RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)
    
    # If hand landmarks are detected
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the frame
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Loop through the landmarks to track the tip of the index finger (for drawing)
            for i in range(0, 21):
                x = int(landmarks.landmark[i].x * frame.shape[1])
                y = int(landmarks.landmark[i].y * frame.shape[0])
                
                # Check if the index finger is close to the canvas
                if i == 8:  # The tip of the index finger (landmark 8)
                    points.append((x, y))
    
    # Draw on the canvas using the points
    if len(points) > 1:
        for i in range(1, len(points)):
            cv2.line(canvas, points[i-1], points[i], (255, 0, 0), 5)
    
    # Show the frame and the canvas
    cv2.imshow("Frame", frame)
    cv2.imshow("Canvas", canvas)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
