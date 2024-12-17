import threading
from camera_feed import capture_camera_feed
from monitor import monitor_system

# List of camera indices and their IDs
cameras = [(0, 'Cam 1'), (1, 'Cam 2')]  # Add more cameras as needed


def start_camera_system():
    threads = []

    # Start a thread for each camera feed
    for camera_index, camera_id in cameras:
        thread = threading.Thread(target=capture_camera_feed, args=(camera_index, camera_id))
        threads.append(thread)
        thread.start()

    # Monitor system resources in a separate thread
    monitor_thread = threading.Thread(target=monitor_system)
    monitor_thread.start()

    # Wait for all camera threads to finish
    for thread in threads:
        thread.join()


