# Realtime-Facial-Recognition
Developers:
  Saakshi Mathur
  Mithun Menon
This code continuously captures video frames from a webcam, identifies and labels recognized faces in real-time based on pre-encoded known faces, and displays the annotated video stream until the user decides to exit by pressing the "Esc" key. It is a basic implementation of real-time face recognition using OpenCV and a custom face recognition library.

# 1. Importing Libraries: The code starts by importing the necessary libraries:

cv2: This library, known as OpenCV (Open Source Computer Vision Library), is widely used for computer vision tasks, including image and video processing.

SimpleFacerec: This appears to be a custom package or module for face recognition.

# 2. Creating a SimpleFacerec Object: 
An instance of the SimpleFacerec class is created and assigned to the variable sfr. This object will be used for face recognition tasks.

# 3. Loading Encoded Face Images: 
The load_encoding_images method of the SimpleFacerec object (sfr) is used to load encoded face images from a folder named "faces." These encoded images serve as a reference for recognizing faces.

# 4. Setting up the Camera: 
The code configures the camera (in this case, a webcam) using OpenCV (cv2). It sets the resolution of the camera feed to 640x480 pixels using the cap.set method.

# 5. Entering a Video Capture Loop: 
The code enters an infinite loop (while True) to continuously capture video frames from the webcam.

# 6. Frame Capture and Face Recognition:

Inside the loop, it captures a frame from the webcam using the cap.read() method. The captured frame is stored in the frame variable.

The sfr.detect_known_faces method is used to detect and recognize faces within the captured frame. This method returns two lists: face_locations (locations of detected faces) and face_names (names of recognized faces).

For each detected face, the code performs the following actions:

It retrieves the coordinates of the face bounding box (top-left and bottom-right corners) from face_locations.
It adds a label with the recognized name just above the detected face using the cv2.putText method.
A rectangle is drawn around the detected face using cv2.rectangle, highlighting it.
The processed frame with face recognition results is displayed in a window named "Frame" using cv2.imshow.

The code waits for a key press using cv2.waitKey(1) and checks if the pressed key is the "Esc" key (key code 27). If the "Esc" key is pressed, the loop is exited.

# 7. Releasing Resources and Closing Windows: 
After exiting the loop (typically by pressing the "Esc" key), the code releases the webcam feed (cap.release()) and closes all OpenCV windows (cv2.destroyAllWindows()).
