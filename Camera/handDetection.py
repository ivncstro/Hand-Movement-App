import cv2

def process_frame(frame):

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        edges = cv2.Canny(frame_rgb, 100, 700)
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        #looks for strong changes in brightness and color and outlines hte boundries
        #black images, white edges

        #100 - lower threshold
        #700 - upper threshold
        #change after testing

        return edges_bgr


