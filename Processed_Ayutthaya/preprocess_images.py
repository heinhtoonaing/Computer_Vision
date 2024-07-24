import os
import cv2

def preprocess_images(input_dir, output_dir, img_size=(256, 256), convert_gray=True, normalize=True):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(root, file)
                
                # Debug: Print the file path
                print(f"Processing: {img_path}")
                
                # Read image
                img = cv2.imread(img_path)
                
                # Check if the image was loaded correctly
                if img is None:
                    print(f"Failed to load image at {img_path}. Skipping...")
                    continue
                
                # Resize image
                img_resized = cv2.resize(img, img_size)
                
                # Convert to grayscale if needed
                if convert_gray:
                    img_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
                
                # Normalize pixel values
                if normalize:
                    img_resized = img_resized.astype('float32') / 255.0
                
                # Save processed image
                output_path = os.path.join(output_dir, os.path.relpath(img_path, input_dir))
                output_folder = os.path.dirname(output_path)
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                
                # Save as single-channel if grayscale, otherwise save as 3-channel
                if convert_gray:
                    cv2.imwrite(output_path, (img_resized * 255).astype('uint8'))
                else:
                    cv2.imwrite(output_path, (img_resized * 255).astype('uint8'))

# Example usage
input_directory = r'C:\Users\Hein Htoo Naing\Computer_Vision\Ayutthaya'
output_directory = r'C:\Users\Hein Htoo Naing\Computer_Vision\Processed_Ayutthaya'
preprocess_images(input_directory, output_directory)
