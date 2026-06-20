# imported cv2: use conda interpreter and install through conda
# use: open cam, read vid frames, show video window, save vid file
import cv2
from Camera.hand_detection import preprocessed

# default cam block
# create cam video object named cam
cam = cv2.VideoCapture(0) # if multiple cam [cam1 = 0, cam2 = 1] index


#testing camera for debugging
if not cam.isOpened():
    print('Could not open camera')


while True:
    ret, frame = cam.read()

    #checking for frame being read
    if not ret:
        print('Could not read camera')
        break



    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()