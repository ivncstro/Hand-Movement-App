import cv2

# open default cam
cam = cv2.VideoCapture(0)

# default frame
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# define the codec and create videoWriter obj
fourcc = cv2.VideoWriter_fourcc(*'mp4v')