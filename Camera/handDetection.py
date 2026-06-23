import cv2

def process_frame(frame):

        #bg_subtractor = cv2.createBackgroundSubtractorMOG2()
        #put outside function to train what is background and what is not...

        #Edge detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #_, mask = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
        #has a threshold for black and white (no shades)
        #later, try adaptive thresholding or HSV masking depending on your goal

        #fg_mask = bg_subtractor.apply(frame)

        #Gaussian Bluring
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 100, 700)
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        #looks for strong changes in brightness and color and outlines hte boundries
        #black images, white edges

        #100 - lower threshold
        #700 - upper threshold
        #change after testing


        return edges_bgr


