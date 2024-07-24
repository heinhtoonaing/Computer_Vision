import cv2
import numpy as np
import os

def extract_features(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(img, None)
    return keypoints, descriptors

def process_images(image_directory, output_features_file, output_labels_file):
    features = []
    labels = []
    
    for label, subdir in enumerate(os.listdir(image_directory)):
        subdir_path = os.path.join(image_directory, subdir)
        if os.path.isdir(subdir_path):
            for filename in os.listdir(subdir_path):
                if filename.endswith('.jpg') or filename.endswith('.png'):
                    image_path = os.path.join(subdir_path, filename)
                    print(f"Processing: {image_path}")
                    _, descriptors = extract_features(image_path)
                    if descriptors is not None:
                        features.append(descriptors)
                        labels.extend([label] * descriptors.shape[0])

    features = np.vstack(features)  # Stack all descriptors
    labels = np.array(labels)  # Convert labels to numpy array

    np.save(output_features_file, features)
    np.save(output_labels_file, labels)

image_directory = r'C:\Users\Hein Htoo Naing\Computer_Vision\Processed_Ayutthaya'
output_features_file = r'C:\Users\Hein Htoo Naing\Computer_Vision\features.npy'
output_labels_file = r'C:\Users\Hein Htoo Naing\Computer_Vision\labels.npy'

process_images(image_directory, output_features_file, output_labels_file)
