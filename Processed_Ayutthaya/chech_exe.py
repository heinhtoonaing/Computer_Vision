import os

# Path to the directory
image_dir = r'C:\Users\Hein Htoo Naing\Computer_Vision\Processed_Ayutthaya'

# List all files in the directory
files = os.listdir(image_dir)

# Print file names and extensions
for file in files:
    print(f"File: {file}, Extension: {os.path.splitext(file)[1]}")
