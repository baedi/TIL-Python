import picamera
import time
import threading

class CameraPreview:
    
    ### Variable
    __camera = None
    __width = 1280
    __height = 720
    __frame = 12
    
    __recordTime = -1
    
    
    ### Initialization
    def __init__(self):
        print("Camera initialization...")
        self.__camera = picamera.PiCamera()
        self.__camera.resolution = (self.__width, self.__height)
        self.__camera.framerate = self.__frame
        self.__camera.annotate_text_size = 24
        self.__camera.annotate_background = picamera.Color('black')
        self.CamTimer()
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
    
    def CamTimer(self):
        timer = threading.Timer(1, self.CamTimer)
        timer.start()
        
        self.__recordTime = self.__recordTime + 1
        pass
    
    def UpdateText(self):
        second = (int)(self.__recordTime % 60)
        minute = (int)((self.__recordTime % 3600) / 60)
        hour = (int)(self.__recordTime / 3600)
        
        timeStr = str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)
        
        self.__camera.annotate_text = " Date : (comming soon) \n" + " Record time : %s " % (timeStr)
        pass
    
    
    pass


### Main
isLoop = True

cameraManager = CameraPreview()
cameraManager.StartPreview()
cameraManager.StartRecording()

try:
    while isLoop:
        cameraManager.UpdateText()
        pass
    pass

except KeyboardInterrupt:
    isLoop = False
    cameraManager.StopRecording()    
    cameraManager.StopPreview()
    pass

print("Program exit")

# Source : https://projects.raspberrypi.org/en/projects/getting-started-with-picamera