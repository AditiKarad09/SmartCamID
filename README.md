

# **SmartCamID: Real-Time Camera Stream Encoding and Metadata Embedding**

## **Project Overview**

SmartCamID is a system designed for **real-time video processing** and **metadata embedding** to improve live broadcasting workflows. This project ensures **source identification**, **secure metadata encryption**, and **low-latency streaming** while supporting multi-camera setups.  

**Key Features**:
- Secure metadata embedding using **Fernet encryption**.
- Support for multi-camera feeds, including iPhone Continuity Camera and laptop webcams.
- Real-time video stream overlay with metadata for source identification.
- Output integration with **OBS Studio** for streaming to platforms like **YouTube, Zoom, and Twitch**.
- Performance optimized with minimal latency and high video quality.

---

## **Workflow**

### **High-Level Steps**  
1. **Camera Input**: Capture feeds from laptop cameras or iPhones (using Continuity Camera).  
2. **Processing Stage**:  
   - Video feed capture using OpenCV.  
   - Secure metadata encryption (Fernet).  
   - Embed metadata into video frames.  
3. **Output Preparation**: Virtual camera setup via PyVirtualCam or OBS Studio.  
4. **Streaming Targets**: Stream output to YouTube, Zoom, or Twitch.

---

## **Installation**

Follow these steps to set up and run SmartCamID on your machine.

### **1. Prerequisites**
Ensure you have the following installed:
- Python 3.8+  
- OpenCV  
- Cryptography Library  
- Matplotlib  
- PyVirtualCam  
- OBS Studio  

### **2. Install Required Packages**

Run the following commands in your terminal:
```bash
pip install opencv-python
pip install cryptography
pip install matplotlib
pip install pyvirtualcam
```

### **3. Install OBS Studio**

Download and install OBS Studio from the official website:  
[OBS Studio Download](https://obsproject.com/)

---

## **File Structure**

```plaintext
SmartCamID/
│
├── camera.py                  # Main script to run metadata embedding
├── frame_rate_graph.py        # Script to generate frame rate graph
├── flowchart.py               # Script for processing flowchart
├── metadata_time_graph.png    # Performance graph for embedding times
├── SmartCamID_Flowchart.png   # Workflow diagram
├── SmartCamID_Methodology.png # Detailed methodology diagram
└── frame_rate_data.json       # JSON file storing frame rate metrics
```

---

## **Execution Instructions**

### **1. Run the Main Program**

Execute the `camera.py` file to capture live feeds, encrypt metadata, and display video streams with overlay.

```bash
python camera.py
```

**Features**:
- Multi-camera capture.
- Metadata encryption and overlay.
- Press **'q'** to exit the live feed.

The frame rate data will be automatically saved to `frame_rate_data.json`.

---

### **2. Generate Frame Rate Graph**

After running the main script, use `frame_rate_graph.py` to generate a bar graph of the frame rates for each camera:

```bash
python frame_rate_graph.py
```

**Output**:
- A bar graph will be saved as `frame_rate_graph.png` and displayed.  
---

## **Performance Metrics**

- **Average Metadata Embedding Time**: ~3ms per frame  
- **Latency**: ~50ms for end-to-end processing  
- **Platform Testing**:
   - **YouTube**: High resolution, 200ms latency  
   - **Zoom**: Low latency, moderate resolution  
   - **Twitch**: Balanced quality and latency  

---

## **Challenges and Solutions**

| **Process**         | **Tools/Technologies**      | **Challenges**                    |  
|----------------------|-----------------------------|-----------------------------------|  
| Feed Capture        | OpenCV, Continuity Camera  | macOS Continuity Camera setup    |  
| Encryption          | Fernet                     | Real-time performance optimization|  
| Streaming           | OBS Studio, PyVirtualCam   | macOS restrictions and OBS latency|  

---

## **References**

1. [OpenCV Documentation](https://docs.opencv.org)  
2. [Python Cryptography Library](https://cryptography.io/en/latest/)  
3. [OBS Studio Documentation](https://obsproject.com/wiki/)  
4. [AVFoundation Guide](https://developer.apple.com/documentation/avfoundation/)

---
