import cv2
import numpy as np
from tensorflow.keras.models import load_model
from datetime import datetime
import csv
import math

# Load the pre-trained model
model = load_model('ani_model.h5')

# Start the camera
cap = cv2.VideoCapture(0)

last_class = -1
classes_seen = [0 for i in range(10)]
start_time = datetime.now()
translations = {
    1: 'texting',
    3: 'texting',
    2: 'talking on phone',
    4: 'talking on phone',
    5: 'operating radio', 
    6: 'drinking',
    7: 'reaching behind',
    9: 'talking to passenger'
}
while True:
    # Capture frame-by-frame in grayscale
    ret, frame = cap.read()
    if ret:
        # Convert the frame to grayscale (if not already in grayscale)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize the frame to 256x256
        resized_frame = cv2.resize(gray_frame, (256, 256))

        # Preprocess the frame for the model
        # Reshape the frame to add the channel dimension
        img_array = resized_frame.reshape(256, 256, 1)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize and add the batch dimension

        # Make a prediction
        prediction = model.predict(img_array)
        predicted_class = int(np.argmax(prediction, axis=1))
        print(f'predicted: {predicted_class}')
        if predicted_class != last_class:
            last_class = predicted_class
            classes_seen[predicted_class] += 1

        # Display the prediction (using the original frame for display)
        cv2.putText(frame, f'Predicted class: {predicted_class}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

end_time = datetime.now()
# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

# Write everything to CSV
data = {
    'drive time': int(math.ceil(((end_time - start_time).total_seconds()) / 60)),
    'normal_driving': classes_seen[5],
    'texting': classes_seen[0],
    'talking on phone': classes_seen[1],
    'drinking': classes_seen[2],
    'reaching behind': classes_seen[3],
    'talking to passenger': classes_seen[4],
}

# Specify the file name for your CSV
file_name = 'data.csv'

# Open the file in append mode
with open(file_name, 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data.keys())
    writer.writerow(data)
