import cv2

# Utility function to draw text with shadow effect
def draw_text_with_shadow(frame, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, size=1, color=(255, 255, 255), thickness=2, shadow_color=(0, 0, 0), shadow_thickness=5):
    x, y = position
    # Draw shadow
    cv2.putText(frame, text, (x + 2, y + 2), font, size, shadow_color, shadow_thickness)
    # Draw main text
    cv2.putText(frame, text, (x, y), font, size, color, thickness)
