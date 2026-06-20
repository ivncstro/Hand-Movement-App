import cv2

def process_frame(frame):

        #Edge detection
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(frame_rgb, 120, 255, cv2.THRESH_BINARY)

        #Gaussian Bluring
        #blurred = cv2.GaussianBlur(frame_rgb, (5, 5), 0)
        edges = cv2.Canny(mask, 100, 700)
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        #looks for strong changes in brightness and color and outlines hte boundries
        #black images, white edges

        #100 - lower threshold
        #700 - upper threshold
        #change after testing

        # Contours
        #contours, _ = cv2.findContours(blurred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #within the white edges finds shapes

        #output = frame.copy()

        #if contours:
        #        largest_contour = max(contours, key=cv2.contourArea)
        #        cv2.drawContours(output, [largest_contour], -1, (0, 255, 0), 2)
        #    #find the largest one and draw it on the output


        return edges_bgr


