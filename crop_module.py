import cv2
import numpy as np

def run_crop_analysis(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # --- VI CALCULATION (Your original code) ---
        B, G, R = cv2.split(frame)
        R_float = R.astype(float)
        G_float = G.astype(float)
        
        denominator = G_float + R_float + 1e-6
        vi_index = (G_float - R_float) / denominator
        
        vi_normalized = ((vi_index + 1.0) * 127.5).clip(0, 255).astype(np.uint8)
        vi_colored = cv2.applyColorMap(vi_normalized, cv2.COLORMAP_JET)

        # --- ADD GRADIENT LEGEND (Color Bar) ---
        
        height, width = vi_colored.shape[:2]
        bar_w, bar_h = 20, 150
        bar_x, bar_y = width - bar_w - 30, 50 # Top Right Position

        # 1. Create a color bar gradient 
        color_bar = np.arange(256, dtype=np.uint8).reshape(256, 1)
        color_bar = np.repeat(color_bar, bar_w, axis=1) 
        color_bar = cv2.flip(color_bar, 0) # Flip so 255 (healthy) is at the top
        color_bar_colored = cv2.applyColorMap(color_bar, cv2.COLORMAP_JET)
        color_bar_colored = cv2.resize(color_bar_colored, (bar_w, bar_h)) 
        
        # 2. Place the color bar onto the main image
        vi_colored[bar_y : bar_y + bar_h, bar_x : bar_x + bar_w] = color_bar_colored
        
        # 3. Add Labels to the color bar
        cv2.putText(vi_colored, "HEALTHY (High VI)", (bar_x - 120, bar_y + 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        
        cv2.putText(vi_colored, "SOIL/UNHEALTHY (Low VI)", (bar_x - 120, bar_y + bar_h - 5), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

        # Overlay title text
        cv2.putText(vi_colored, "Crop Health (VI Simulation)", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # --- END LEGEND ---
        
        cv2.imshow("Crop Health Analysis", vi_colored)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()