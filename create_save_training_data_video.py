import cv2
import os

def main():
    # Prompt the user for a folder name
    folder_name = input("Enter the folder name where you want to save the frames: ")

    # Create the folder if it does not exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")

    # Start the camera
    cap = cv2.VideoCapture(0)

    print("Starting video capture. Press 'q' to stop and save frames.")

    frame_count = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Save the frame
        frame_path = os.path.join(folder_name, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_path, frame)
        frame_count += 1

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    print(f"Video capture stopped. {frame_count} frames were saved in '{folder_name}'.")

if __name__ == "__main__":
    main()
