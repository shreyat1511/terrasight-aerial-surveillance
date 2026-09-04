# TerraSight : Agricultural & Wildlife Aerial Surveillance 

A computer vision system that simulates an aerial surveillance platform for agricultural and wildlife monitoring using Python and OpenCV.

## Overview

TerraSight processes video feeds through three analysis modules:

- **Soil Conservation** — HSV-based detection of exposed soil and potential erosion zones
- **Crop Health Analysis** — RGB-based vegetation index visualization
- **Wildlife Monitoring** — YOLOv3-tiny object detection for wildlife footage

A Tkinter GUI provides an interface for selecting and running each module.

## Tech Stack

- Python
- OpenCV
- YOLOv3-tiny
- TensorFlow
- NumPy
- Tkinter

## Project Structure

`main.py` — Main application and GUI  
`soil_module.py` — Soil conservation analysis  
`crop_module.py` — Crop health analysis  
`wildlife_module.py` — Wildlife object detection  
`coco.names` — YOLO object class labels  
`yoloV3-tiny.cfg` — YOLO network configuration

## Setup

Clone the repository:

`git clone https://github.com/shreyat1511/terrasight-aerial-surveillance.git`

`cd terrasight-aerial-surveillance`

Install the required packages:

`pip install opencv-python numpy tensorflow`

For wildlife detection, download the YOLOv3-tiny weights and place `yoloV3-tiny.weights` in the project directory alongside `yoloV3-tiny.cfg` and `coco.names`.

Add the required video files using the filenames expected by `main.py`.

## Run

`python main.py`

Use the GUI to select the desired analysis module.

Press `q` to exit an OpenCV video window.

## Applications

The project demonstrates computer vision applications in:

- Agricultural monitoring
- Soil and erosion assessment
- Crop health visualization
- Wildlife monitoring
- Aerial surveillance
