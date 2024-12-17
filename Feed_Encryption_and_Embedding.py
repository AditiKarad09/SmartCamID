#
# import cv2
# from cryptography.fernet import Fernet
#
# # Generate a symmetric encryption key (use the same key for encryption and decryption)
# key = Fernet.generate_key()
# cipher = Fernet(key)
#
# # Function to encrypt metadata (e.g., camera ID)
# def encrypt_metadata(camera_id):
#     encrypted_data = cipher.encrypt(camera_id.encode())
#     print(f"Encrypted Camera ID \n {camera_id}: {encrypted_data.decode()}")
#     return encrypted_data
#
# # Function to decrypt metadata (e.g., encrypted camera ID)
# def decrypt_metadata(encrypted_data):
#     decrypted_data = cipher.decrypt(encrypted_data).decode()
#     print(f"Decrypted Camera ID: {decrypted_data}")
#     return decrypted_data
#
# def capture_and_display_separate_windows():
#     # Open MacBook camera (index 0)
#     laptop_camera = cv2.VideoCapture(0)
#     laptop_camera_id = "MacBook Camera"
#     encrypted_laptop_id = encrypt_metadata(laptop_camera_id)
#     decrypted_laptop_id = decrypt_metadata(encrypted_laptop_id)
#
#     # Open iPhone camera (assuming iPhone as a wireless webcam at index 1)
#     phone_camera = cv2.VideoCapture(1)
#     phone_camera_id = "iPhone Camera"
#     encrypted_phone_id = encrypt_metadata(phone_camera_id)
#     decrypted_phone_id = decrypt_metadata(encrypted_phone_id)
#
#     while True:
#         # Capture MacBook camera frame
#         ret_laptop, frame_laptop = laptop_camera.read()
#         if not ret_laptop:
#             print("Error: Could not capture from MacBook camera.")
#             break
#
#         # Capture iPhone camera frame
#         ret_phone, frame_phone = phone_camera.read()
#         if not ret_phone:
#             print("Error: Could not capture from iPhone camera.")
#             break
#
#         # Overlay decrypted camera IDs on each frame
#         cv2.putText(frame_laptop, f"{decrypted_laptop_id}", (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#         cv2.putText(frame_phone, f"{decrypted_phone_id}", (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#
#         # Display each camera feed in a full window for each
#         cv2.imshow("MacBook Camera Feed", frame_laptop)
#         cv2.imshow("iPhone Camera Feed", frame_phone)
#
#         # Press 'q' to quit the video windows
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     # Release resources
#     laptop_camera.release()
#     phone_camera.release()
#     cv2.destroyAllWindows()
#
# if __name__ == "__main__":
#     capture_and_display_separate_windows()
































import cv2
from cryptography.fernet import Fernet

# Function to generate a symmetric encryption key
# The generated key is used for both encryption and decryption.
def generate_encryption_key():
    print("Generating encryption key...")
    key = Fernet.generate_key()
    print(f"Encryption key generated: {key.decode()}\n")
    return key

# Function to create a cipher object using the provided key
# The cipher object is used to perform encryption and decryption operations.
def create_cipher(key):
    print("Creating cipher object with the provided encryption key...")
    cipher = Fernet(key)
    print("Cipher object successfully created.\n")
    return cipher

# Function to encrypt metadata (e.g., camera ID)
# This function takes plain text (e.g., camera ID) and encrypts it.
def encrypt_metadata(cipher, camera_id):
    print(f"Encrypting metadata for camera ID: {camera_id}...")
    encrypted_data = cipher.encrypt(camera_id.encode())
    print(f"Encrypted Camera ID: {encrypted_data.decode()}\n")
    return encrypted_data

# Function to decrypt metadata (e.g., encrypted camera ID)
# This function takes encrypted data and decrypts it to retrieve the original plain text.
def decrypt_metadata(cipher, encrypted_data):
    print(f"Decrypting metadata: {encrypted_data.decode()}...")
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    print(f"Decrypted Camera ID: {decrypted_data}\n")
    return decrypted_data

# Function to open a camera feed and capture video frames
# Displays the video feed in separate windows for each camera.
def capture_and_display_separate_windows(cipher):
    print("Initializing video capture for cameras...\n")

    # Open the MacBook camera (assuming camera index 0)
    print("Attempting to open MacBook camera (index 0)...")
    laptop_camera = cv2.VideoCapture(0)
    laptop_camera_id = "MacBook Camera"

    if not laptop_camera.isOpened():
        print("Error: Could not open MacBook camera.\n")
        return

    print("MacBook camera successfully opened.\n")

    # Encrypt and decrypt MacBook camera ID
    encrypted_laptop_id = encrypt_metadata(cipher, laptop_camera_id)
    decrypted_laptop_id = decrypt_metadata(cipher, encrypted_laptop_id)

    # Open the iPhone camera (assuming iPhone as a wireless webcam at index 1)
    print("Attempting to open iPhone camera (index 1)...")
    phone_camera = cv2.VideoCapture(1)
    phone_camera_id = "iPhone Camera"

    if not phone_camera.isOpened():
        print("Error: Could not open iPhone camera.\n")
        laptop_camera.release()
        return

    print("iPhone camera successfully opened.\n")

    # Encrypt and decrypt iPhone camera ID
    encrypted_phone_id = encrypt_metadata(cipher, phone_camera_id)
    decrypted_phone_id = decrypt_metadata(cipher, encrypted_phone_id)

    print("Starting video capture loop. Press 'q' to exit.\n")

    while True:
        # Capture a frame from the MacBook camera
        ret_laptop, frame_laptop = laptop_camera.read()
        if not ret_laptop:
            print("Error: Could not capture a frame from MacBook camera.")
            break

        # Capture a frame from the iPhone camera
        ret_phone, frame_phone = phone_camera.read()
        if not ret_phone:
            print("Error: Could not capture a frame from iPhone camera.")
            break

        # Overlay the decrypted camera ID on the MacBook camera frame
        # this is done just for user understanding
        cv2.putText(
            frame_laptop,
            f"{decrypted_laptop_id}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )

        # Overlay the decrypted camera ID on the iPhone camera frame
        cv2.putText(
            frame_phone,
            f"{decrypted_phone_id}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )

        # Display the video feed for MacBook camera in a separate window
        cv2.imshow("MacBook Camera Feed", frame_laptop)

        # Display the video feed for iPhone camera in another separate window
        cv2.imshow("iPhone Camera Feed", frame_phone)

        # Check if the 'q' key is pressed to break the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting video capture loop...\n")
            break

    # Release all resources after exiting the loop
    print("Releasing camera resources and closing windows...\n")
    laptop_camera.release()
    phone_camera.release()
    cv2.destroyAllWindows()
    print("Resources released and windows closed.\n")

# Main function to orchestrate the entire process
if __name__ == "__main__":
    print("Starting the camera metadata encryption program...\n")

    # Generate encryption key and create cipher object
    encryption_key = generate_encryption_key()
    cipher = create_cipher(encryption_key)

    # Start capturing video and displaying feeds
    capture_and_display_separate_windows(cipher)

    print("Program execution completed.")
