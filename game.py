import cv2
from hand_tracking import HandTracker
from game_logic import Game

# Initialize the webcam and hand tracking
cap = cv2.VideoCapture(0)
hand_tracker = HandTracker()
game = Game()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip frame horizontally to act as a mirror
    frame = cv2.flip(frame, 1)
    
    # Detect hand landmarks
    hand_landmarks = hand_tracker.detect_hands(frame)
    
    # Update the game state based on hand movements
    game.update(hand_landmarks, frame)
    
    # Display the frame with game elements and hand tracking
    cv2.imshow('Hand Tracking Game', frame)
    
    # Exit when 'Esc' key is pressed
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
