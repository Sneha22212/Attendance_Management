import cv2

# Check if 'face' module exists
if 'face' in dir(cv2):
    # Create the LBPH face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    print("LBPHFaceRecognizer created successfully!")
else:
    print("Face module not found.")
