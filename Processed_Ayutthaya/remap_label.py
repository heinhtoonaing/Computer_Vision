import numpy as np

# Load your labels
labels = np.load(r'C:\Users\Hein Htoo Naing\Computer_Vision\labels.npy')

# Check unique labels
print("Unique labels before remapping:", np.unique(labels))

# Define a mapping function
def remap_labels(labels, old_labels, new_range):
    # Create a dictionary to map old labels to new labels
    mapping = {old: new for new, old in enumerate(old_labels)}
    # Remap the labels
    return np.array([mapping.get(label, -1) for label in labels])  # Using -1 to flag unmapped labels

# Unique labels before mapping
unique_labels = np.unique(labels)
print("Unique labels to remap:", unique_labels)

# Define the old labels and the new range
old_labels = np.array([2, 3, 5])
new_range = range(len(old_labels))  # New range should be [0, len(old_labels) - 1]

# Remap labels
remapped_labels = remap_labels(labels, old_labels, new_range)

# Save the fixed labels
np.save(r'C:\Users\Hein Htoo Naing\Computer_Vision\fixed_labels.npy', remapped_labels)

# Verify the result
print("Unique labels after remapping:", np.unique(remapped_labels))
