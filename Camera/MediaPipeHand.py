
import cv2
import mediapipe as mp
import time
from pathlib import Path

# MediaPipe setup
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Path to the downloaded model
model_path = Path(__file__).resolve().parent / "hand_landmarker.task"

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=str(model_path)), #where to find model
    running_mode=VisionRunningMode.VIDEO, # how to process images
    num_hands=2    #up to two hands
) 

# Open the webcam
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    raise RuntimeError("Could not open camera")

# Get camera dimensions
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set up video recording
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0,
                      (frame_width, frame_height))

start_time = time.monotonic()

try:
    # Initialize MediaPipe
    with HandLandmarker.create_from_options(options) as landmarker: #creates the detector

        while True:
            ret, frame = cam.read()

            if not ret:
                print("Could not read camera")
                break

            # Convert OpenCV BGR image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert to MediaPipe Image
            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb_frame
            )

            # Timestamp in milliseconds
            timestamp_ms = int((time.monotonic() - start_time) * 1000)

            # Detect hand landmarks
            result = landmarker.detect_for_video(
                mp_image, timestamp_ms
            )

            # Draw landmarks on the original frame
            for hand in result.hand_landmarks: 
                for landmark in hand:
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)

                    cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

            # Save and display
            out.write(frame)
            cv2.imshow('Camera - Hand Tracking', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

finally:
    cam.release()
    out.release()
    cv2.destroyAllWindows()
    