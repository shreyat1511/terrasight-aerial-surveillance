# Aerial Surveillence for wildlife and agriculture conservation using OpenCV
🛰️ TerraSight Multi-Habitat Analysis System
Project Overview
The TerraSight Multi-Habitat Analysis System is a pure-software computer vision project designed to simulate the real-time analysis pipeline of an aerial surveillance platform (such as a drone). The goal is to extract critical intelligence regarding agricultural and environmental conditions across multiple domains using Python and OpenCV.

The application is controlled via a user-friendly Tkinter GUI and features three distinct analysis modules running on simulated video feeds.

✨ Key Features
This system provides automated analysis across three critical areas:

Soil Conservation (Erosion Detection):

Technique: HSV Color Filtering.

Output: Highlights bare soil and potential erosion zones in Bright Red for easy identification. Includes a high-contrast legend for clarity.

Crop Health Analysis (VI Simulation):

Technique: Simulated Vegetation Index (VI) calculation ( 
G+R
G−R
​
 ) using standard RGB imagery.

Output: Displays the video using a JET Colormap gradient, where red/yellow indicates high health/density and blue/black indicates stress or bare ground. Features a vertical gradient color bar legend.

Wildlife Monitoring (Object Detection):

Technique: Real-time object detection using the lightweight YOLOv3-tiny Convolutional Neural Network (CNN).

Output: Draws bounding boxes and class labels (e.g., 'horse', 'bird') over animals detected in various challenging scenarios (Open Habitat, Predator Hunting).

🛠️ Technology Stack
Core Language: Python 3.x

Computer Vision & Video: OpenCV (cv2)

Deep Learning Backend: TensorFlow (used for underlying YOLO model structure)

Numerical Processing: NumPy

User Interface (GUI): Tkinter (built-in Python GUI library)

🚀 Setup and Installation
1. Prerequisites
Ensure you have Python 3.x installed. Then, install the required libraries:

pip install opencv-python numpy tensorflow

(Note: Tkinter is usually included with standard Python installations.)

2. Required ML Assets (YOLO Files)
To run the Wildlife Monitoring module, you must download the following three configuration files and place them directly in the root of the project directory:

File

Type

Purpose

yolov3-tiny.cfg

Configuration

Defines the YOLO network architecture.

yolov3-tiny.weights

Weights

The pre-trained weights for object recognition.

coco.names

Class Names

Contains the 80 object labels recognized by the model.

3. Video Setup
Create a folder named sample_videos in the root directory and place your three unique wildlife videos and the agricultural video inside it, ensuring their names match the paths defined in main.py.

▶️ How to Run the Application
Navigate to the project root directory in your terminal.

Execute the main script:

python main.py

The TerraSight GUI window will launch.

Click "1. Soil Conservation" or "2. Crop Health Analysis" to immediately run the agricultural video analysis.

Click "3. Wildlife Monitoring" to open a sub-menu where you can select one of the specific wildlife scenario videos (Open Habitat, Predator Hunting, Birds).

To exit any video stream, press the 'q' key while the OpenCV video window is focused.
