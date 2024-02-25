import os

import cv2
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from tensorflow.keras.utils import to_categorical

# Load your dataset
data = pd.read_csv('data/train_labels.csv')

# Assuming the 'Image' column contains image filenames (e.g., '12470.png')
image_folder = 'data/train_256x256'  # Change this to the actual path

# Assuming your images are RGB and have shape (image_height, image_width, num_channels)
image_height = 256
image_width = 256
num_channels = 3  # Assuming RGB

# Assuming the last 10 columns are your labels
num_classes = 10
labels = data.iloc[:, -num_classes:].values

# Load and preprocess images
images = []
skipped_images = 0
count = 0

for filename in data['Image'][:1000]:  # Select the first 1000 samples
    count += 1
    filename = str(filename) + '.png'
    image_path = os.path.join(image_folder, filename)
    print(f"img {filename}")
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise Exception(f"Unable to read image {filename}")

        img = cv2.resize(img, (image_width, image_height))
        images.append(img)
    except Exception as e:
        print(f"Warning: {e}. Skipping.")
        skipped_images += 1

if skipped_images == len(data):
    print("Error: No valid images found. Check your file paths.")
    exit()

images = np.array(images) / 255.0

# Select the first 1000 labels
labels = labels[:1000]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)


# Build the model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(image_height, image_width, num_channels)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))  # Make sure this line is correct

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# Define a ModelCheckpoint callback to save the best model
checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True, monitor='val_accuracy', mode='max', verbose=1)

# Train the model

print(num_classes)
print(y_train.shape)
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test), callbacks=[checkpoint])

# Evaluate the model
accuracy = model.evaluate(X_test, y_test)[1]
model.save("final_model.h5")
print(f'Test Accuracy: {accuracy * 100:.2f}%')
