import tkinter as tk
from tkinter import ttk
import soil_module
import wildlife_module
import crop_module

# Define all video paths at the top for easy management
VIDEO_PATHS = {
    # Agricultural Videos
    "agri": "sample_videos/videoplayback.mp4", 
    
    # Wildlife Videos - VERIFY THESE NAMES!
    "wildlife_1": "sample_videos/wildlife_footage.mp4",
    "wildlife_2": "sample_videos/videoplayback(1).mp4",    
    "wildlife_3": "sample_videos/videoplayback(2).mp4"       
}

class DroneVisionApp:
    def __init__(self, root):
        self.root = root
        root.title("AeroSense Conservation System") # Using one of the recommended names
        
        # --- Configure Styles ---
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=10)
        
        # --- Main Frame for Centering ---
        main_frame = ttk.Frame(root, padding="20 20 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # --- Title Label ---
        ttk.Label(main_frame, text="Conservation Vision Modules", 
                  font=('Arial', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=15)
        
        # --- Buttons ---

        # 1. Soil Module Button
        ttk.Button(main_frame, text="1. Soil Conservation (Erosion)", 
                   command=lambda: self.run_module(soil_module.run_soil_detection, VIDEO_PATHS['agri'])
                  ).grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        # 2. Crop Module Button
        ttk.Button(main_frame, text="2. Crop Health Analysis (VI)", 
                   command=lambda: self.run_module(crop_module.run_crop_analysis, VIDEO_PATHS['agri'])
                  ).grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

        # 3. Wildlife Button (Opens Sub-Menu)
        ttk.Button(main_frame, text="3. Wildlife Monitoring (Select Video)", 
                   command=self.show_wildlife_menu
                  ).grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

        # 4. Exit Button
        ttk.Button(main_frame, text="4. Exit Application", command=root.destroy
                  ).grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")

    def run_module(self, module_function, video_path):
        """Standard handler to run a module and log the action."""
        print(f"Running module: {module_function.__name__} with video: {video_path}")
        # Disable the GUI during video processing to prevent multiple simultaneous calls
        self.root.withdraw() 
        
        # Execute the OpenCV function
        module_function(video_path)
        
        # Re-enable the GUI after the OpenCV window is closed
        self.root.deiconify() 
        print("Module finished. Returning to menu.")


    def show_wildlife_menu(self):
        """Creates and displays a sub-window for wildlife video selection."""
        
        sub_window = tk.Toplevel(self.root)
        sub_window.title("Select Wildlife Video")
        sub_window.grab_set() # Focus on the sub-window
        
        ttk.Label(sub_window, text="Choose Wildlife Scenario:", font=('Arial', 14, 'bold')).pack(pady=10, padx=20)
        
        video_options = {
            "3.1. Open Habitat Monitoring": VIDEO_PATHS['wildlife_1'],
            "3.2. Predator Hunting Detection": VIDEO_PATHS['wildlife_2'],
            "3.3. Birds/Close Range Simulation": VIDEO_PATHS['wildlife_3']
        }
        
        for text, path in video_options.items():
            ttk.Button(sub_window, text=text, 
                       command=lambda p=path: [sub_window.destroy(), self.run_module(wildlife_module.run_wildlife_detection, p)]
                      ).pack(pady=5, padx=20, fill='x')

        ttk.Button(sub_window, text="Cancel", command=sub_window.destroy).pack(pady=10, padx=20, fill='x')
        

if __name__ == "__main__":
    # The command-line menu is now gone, replaced by the GUI setup
    root = tk.Tk()
    app = DroneVisionApp(root)
    root.mainloop()