import numpy as np

# Load and inspect labels
labels = np.load(r'C:\Users\Hein Htoo Naing\Computer_Vision\labels.npy')
print("Labels shape:", labels.shape)
print("Unique labels:", np.unique(labels))
