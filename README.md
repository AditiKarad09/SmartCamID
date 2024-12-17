Project Overview

SmartCamID is a system designed for real-time video processing and metadata embedding to improve live broadcasting workflows. This project ensures source identification, secure metadata encryption, and low-latency streaming while supporting multi-camera setups.

Key Features:

Secure metadata embedding using Fernet encryption.
Support for multi-camera feeds, including iPhone Continuity Camera and laptop webcams.
Real-time video stream overlay with metadata for source identification.
Output integration with OBS Studio for streaming to platforms like YouTube, Zoom, and Twitch.
Performance optimized with minimal latency and high video quality.
Workflow

High-Level Steps
Camera Input: Capture feeds from laptop cameras or iPhones (using Continuity Camera).
Processing Stage:
Video feed capture using OpenCV.
Secure metadata encryption (Fernet).
Embed metadata into video frames.
Output Preparation: Virtual camera setup via PyVirtualCam or OBS Studio.
Streaming Targets: Stream output to YouTube, Zoom, or Twitch.
Installation

Follow these steps to set up and run SmartCamID on your machine.

1. Prerequisites
Ensure you have the following installed:

Python 3.8+
OpenCV
Cryptography Library
Matplotlib
PyVirtualCam
OBS Studio
2. Install Required Packages
Run the following commands in your terminal:

pip install opencv-python
pip install cryptography
pip install matplotlib
pip install pyvirtualcam
3. Install OBS Studio
Download and install OBS Studio from the official website:
OBS Studio Download

File Structure

SmartCamID/
│
├── camera.py                  # Main script to run metadata embedding
├── frame_rate_graph.py        # Script to generate frame rate graph
├── flowchart.py               # Script for processing flowchart
├── metadata_time_graph.png    # Performance graph for embedding times
├── SmartCamID_Flowchart.png   # Workflow diagram
├── SmartCamID_Methodology.png # Detailed methodology diagram
└── frame_rate_data.json       # JSON file storing frame rate metrics
Execution Instructions

1. Run the Main Program
Execute the camera.py file to capture live feeds, encrypt metadata, and display video streams with overlay.

python camera.py
Features:

Multi-camera capture.
Metadata encryption and overlay.
Press 'q' to exit the live feed.
The frame rate data will be automatically saved to frame_rate_data.json.

2. Generate Frame Rate Graph
After running the main script, use frame_rate_graph.py to generate a bar graph of the frame rates for each camera:

python frame_rate_graph.py
Output:

A bar graph will be saved as frame_rate_graph.png and displayed.
Workflow Diagrams

Methodology Diagram
High-Level Workflow
Performance Metrics

Average Metadata Embedding Time: ~3ms per frame
Latency: ~50ms for end-to-end processing
Platform Testing:
YouTube: High resolution, 200ms latency
Zoom: Low latency, moderate resolution
Twitch: Balanced quality and latency
