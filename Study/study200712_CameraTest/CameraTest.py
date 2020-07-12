import picamera
import time
import threading

class CameraPreview:
    
    ### Variable
    __camera = None
    
    ### Initialization
    def __init__(self):
        print("Camera initialization...")
        self.__camera = picamera.PiCamera()
        pass
        
    def StartPreview(self):
        self.__camera.start_preview()
        pass
    
    def StopPreview(self):
        self.__camera.stop_preview()
        self.__camera.close()
        pass
    
    def StartRecording(self):
        self.__camera.start_recording('/home/pi/Desktop/video.h264')
        print("Start Recording!")
        pass
    
    def StopRecording(self):
        self.__camera.stop_recording()
        print("Stop Recording!")
        pass
    
    pass


### Main
isLoop = True

cameraManager = CameraPreview()
cameraManager.StartPreview()
cameraManager.StartRecording()

try:
    while isLoop:
        pass
    pass

except KeyboardInterrupt:
    isLoop = False
    cameraManager.StopPreview()
    cameraManager.StopRecording()
    pass

print("Program exit")

# Source : https://projects.raspberrypi.org/en/projects/getting-started-with-picamera