import cv2

# Create a face recognizer using EigenFaceRecognizer
face_recognizer = cv2.face.EigenFaceRecognizer_create()

# Check if the recognizer was created successfully
if face_recognizer is not None:
    print("Face recognizer created successfully")
else:
    print("Failed to create face recognizer")
