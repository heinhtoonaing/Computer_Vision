import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load features and updated fixed labels
features = np.load(r'C:\Users\Hein Htoo Naing\Computer_Vision\features.npy', allow_pickle=True)
features = np.vstack(features)  # Flatten list of arrays

labels = np.load(r'C:\Users\Hein Htoo Naing\Computer_Vision\fixed_labels.npy')

# Check the shapes
print(f"Features shape: {features.shape}")
print(f"Labels shape: {labels.shape}")

# Ensure labels array length matches features length
if len(labels) != features.shape[0]:
    raise ValueError(f"Number of labels ({len(labels)}) does not match number of feature vectors ({features.shape[0]})")

# Split data
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Create a simple model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(len(set(labels)), activation='softmax')  # Ensure the number of output units matches the number of classes
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test loss: {loss:.4f}")
print(f"Test accuracy: {accuracy:.4f}")

# Save model
model.save('model.h5')
