import os
import matplotlib.pyplot as plt
import cv2

def visualize_image(image_path, title='Image'):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found at: {image_path}")

    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image file could not be read: {image_path}")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()

def find_images(directory):
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_files.append(os.path.join(root, file))
    return image_files

def main():
    image_dir = r'C:\Users\Hein Htoo Naing\Computer_Vision\Processed_Ayutthaya'
    image_files = find_images(image_dir)

    if not image_files:
        raise FileNotFoundError("No image files found in the directory or subdirectories.")

    for image_path in image_files:
        visualize_image(image_path, title=f'Visualizing {os.path.basename(image_path)}')

if __name__ == "__main__":
    main()
