import cv2

class Game:
    def __init__(self):
        # Initialize game targets and score
        self.targets = [(100, 100), (400, 200)]  # Example targets
        self.score = 0
    
    def update(self, hand_landmarks, frame):
        if hand_landmarks:
            # Assuming we're using the first detected hand for interaction
            hand = hand_landmarks[0]
            
            # Index finger tip coordinates (landmark 8)
            index_tip = hand.landmark[8]
            index_pos = (int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0]))
            
            # Check if the index finger is close to any target
            for target in self.targets:
                if abs(index_pos[0] - target[0]) < 30 and abs(index_pos[1] - target[1]) < 30:
                    self.targets.remove(target)  # Remove the hit target
                    self.score += 1
                    print(f"Target hit! Score: {self.score}")
        
        # Draw current targets on the frame
        for target in self.targets:
            cv2.circle(frame, target, 20, (0, 255, 0), -1)

        # Display the current score on the frame
        cv2.putText(frame, f"Score: {self.score}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
