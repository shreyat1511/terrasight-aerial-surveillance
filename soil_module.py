import cv2
import numpy as np

def run_soil_detection(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Define the new text color for the legend: Bright Yellow (B=0, G=255, R=255)
    LEGEND_COLOR = (0, 255, 255) 

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Get frame dimensions for legend placement
        height, width = frame.shape[:2]

        # Convert to HSV 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define range for "brownish soil" (tweak values if needed)
        lower_brown = (10, 100, 20)
        upper_brown = (20, 255, 200)

        mask = cv2.inRange(hsv, lower_brown, upper_brown)

        # Highlight soil areas in red on the original frame
        frame[mask > 0] = (0, 0, 255) # Red highlight (BGR format)

        # --- ADD LEGEND ---
        
        # Define Legend Position (Top Right Corner)
        legend_x, legend_y = width - 200, 30
        
        # 1. Draw Text and Color Box for "Erosion/Soil" (RED)
        cv2.rectangle(frame, (legend_x, legend_y - 15), (legend_x + 15, legend_y), (0, 0, 255), -1) 
        # Text color changed to LEGEND_COLOR (Bright Yellow)
        cv2.putText(frame, "Erosion/Soil", (legend_x + 25, legend_y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, LEGEND_COLOR, 1, cv2.LINE_AA)

        # 2. Draw Text and Color Box for "Healthy Area" (GREEN - for contrast)
        cv2.rectangle(frame, (legend_x, legend_y + 15), (legend_x + 15, legend_y + 30), (0, 255, 0), -1) 
        # Text color changed to LEGEND_COLOR (Bright Yellow)
        cv2.putText(frame, "Healthy Area", (legend_x + 25, legend_y + 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, LEGEND_COLOR, 1, cv2.LINE_AA)
        
        # Overlay title text (for clarity, also in Bright Yellow)
        cv2.putText(frame, "Soil Erosion Detection", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, LEGEND_COLOR, 2)
        
        # --- END LEGEND ---

        cv2.imshow("Soil Erosion Detection", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


