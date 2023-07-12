# Install in phone IP webcam and init server
# Important: be connected to the same network
# Import libraries cv2
import cv2

# Replace the below URL with your own. Make sure to add "/video" at last.
url = "http://192.168.18.44:8080/video"

#Open video file of url
cp = cv2.VideoCapture(url)

# While loop to continuously fetching data from the Url
while(True):
    
    #Read video capture
    camera, frame = cp.read()
    
    #Resizing the video frame
    frame = cv2.resize(frame, (960, 540))
    
    # Displaying the image frame:
    cv2.imshow("Phone webcam", frame)
    
    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break
    
# Closing windows and ending the program  
cv2.destroyAllWindows()