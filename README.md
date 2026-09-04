# TerraSight — Aerial Surveillance for Agriculture & Wildlife

A computer vision system that simulates an aerial surveillance platform for
agricultural and environmental monitoring using Python and OpenCV.

TerraSight analyzes video feeds across three domains:
- Soil conservation and erosion detection
- Crop health analysis
- Wildlife monitoring and object detection

## Overview

TerraSight is a software-based computer vision system designed to simulate
the analysis pipeline of an aerial surveillance platform such as a drone.

The system processes video feeds and extracts visual information related to
agricultural conditions and wildlife activity. A Tkinter-based interface
allows users to select and run the different analysis modules.

## Analysis Modules

### 🌱 Soil Conservation

**Method:** HSV color filtering

Identifies exposed/bare soil regions in agricultural imagery that may
indicate potential erosion zones.

**Output:** Highlighted regions of detected bare soil.

### 🌾 Crop Health Analysis

**Method:** Simulated vegetation index using RGB imagery

Processes agricultural video frames to estimate vegetation density/health
and visualize variations across the scene.

**Output:** Color-mapped visualization indicating areas of higher and
lower vegetation health/density.

### 🦌 Wildlife Monitoring

**Method:** YOLOv3-tiny object detection

Detects objects in wildlife video feeds using the lightweight YOLOv3-tiny
model and overlays bounding boxes and class labels on detected objects.

**Output:** Real-time object detection with bounding boxes and labels.


## System Workflow

Video Feed
   ↓
Frame Acquisition
   ↓
Module Selection
   ↓
Computer Vision Processing
   ↓
Analysis / Detection
   ↓
Visualized Results
