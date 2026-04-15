# imported cv2: use conda interpreter and install through conda
# use: open cam, read vid frames, show video window, save vid file
import cv2

# default cam block
# create cam video object named cam
cam = cv2.VideoCapture(0) # if multiple cam [cam1 = 0, cam2 = 1] index

# REQ: read over this
# set width (default for cv2)
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
#set height (default for cv2)
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    # Write the frame to the output file
    out.write(frame)

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()