import cv2

def process_frame(frame):

        #Edge detection
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #Gaussian Bluring
        blurred = cv2.GaussianBlur(frame_rgb, (5, 5), 0)
        edges = cv2.Canny(blurred, 100, 700)
        #looks for strong changes in brightness and color and outlines hte boundries
        #black images, white edges

        #100 - lower threshold
        #700 - upper threshold
        #change after testing

        # Contours
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #within the white edges finds shapes

        output = frame.copy()

        if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                cv2.drawContours(output, [largest_contour], -1, (0, 255, 0), 2)
            #find the largest one and draw it on the output


        return output


