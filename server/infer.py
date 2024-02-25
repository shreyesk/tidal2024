import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import csv

# Load the pre-trained model
model = load_model('model.h5')

# Start the camera
cap = cv2.VideoCapture(0)

last_class = -1
classes_seen = [0 for i in range(10)]
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Convert the frame to RGB (OpenCV uses BGR by default)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize the frame to 256x256
        resized_frame = cv2.resize(rgb_frame, (256, 256))

        # Preprocess the frame for the model
        img_array = image.img_to_array(resized_frame)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make a prediction
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)

        if predicted_class != last_class:
            last_class = predicted_class
            classes_seen[predicted_class] += 1

        # Display the prediction
        cv2.putText(frame, f'Predicted class: {predicted_class}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

# write everything to csv
# Your dictionary with column headers as keys and row values as values
data = {
    'drive time': 1000, # TODO make this number actually be calculated
    'texting': classes_seen[1] + classes_seen[3],
    'talking on phone': classes_seen[2] + classes_seen[4],
    'operating the radio': classes_seen[5],
    'drinking': classes_seen[6],
    'reaching behind': classes_seen[7],
    'talking to passenger': classes_seen[9],
}

# Specify the file name for your CSV
file_name = 'data.csv'

# Open the file in append mode
with open(file_name, 'a', newline='') as csvfile:
    # Create a DictWriter object with the column headers
    writer = csv.DictWriter(csvfile, fieldnames=data.keys())
    
    # Write the header (column names)
    writer.writeheader()
    
    # Write the data row
    writer.writerow(data)