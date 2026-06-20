# imported cv2: use conda interpreter and install through conda
# use: open cam, read vid frames, show video window, save vid file
import cv2
import numpy as np
from Camera.handDetection import process_frame

# default cam block
# create cam video object named cam
cam = cv2.VideoCapture(0) # if multiple cam [cam1 = 0, cam2 = 1] index


#testing camera for debugging
if not cam.isOpened():
    print('Could not open camera')


# REQ: read over this
# set width (default for cv2)
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
#set height (default for cv2)
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
original = cv2.VideoWriter('original.mp4', fourcc, 20.0, (frame_width, frame_height)) # just for original
preprocessed = cv2.VideoWriter('pprocessed.mp4', fourcc, 20.0, (frame_width, frame_height))
#add 1

while True:
    ret, frame = cam.read()

    #checking for frame being read
    if not ret:
        print('Could not read camera')
        break

    # add function - preprocessed
    pProcessed = process_frame(frame)

    # Write the frame to the output file
    original.write(frame) #out - original
    preprocessed.write(pProcessed)
    #preprocessed.write(preprocessed)

    # Display the captured frame
    cv2.imshow('Original', frame) #Original
    cv2.imshow('Preprocessed', pProcessed)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and writer objects
cam.release()
preprocessed.release()
original.release()
cv2.destroyAllWindows()




