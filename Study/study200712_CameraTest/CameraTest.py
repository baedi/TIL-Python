import picamera
import time
import threading
import os
import H264UploaderManager

class CameraManager:

    ### Variable
    __uploadManager = None
    __camera = None
    __width = 1280
    __height = 720
    __frame = 12
    __path = None
    __currentRecFilename = None

    __recordTime = -1


    ### Initialization
    def __init__(self, path):

        # start UploaderManager
        self.__uploadManager = H264UploaderManager.H264UploaderManager()

        self.__path = path
        self.__camera = picamera.PiCamera()
        self.__camera.resolution = (self.__width, self.__height)
        self.__camera.framerate = self.__frame
        self.__camera.annotate_text_size = 18
        self.__camera.annotate_background = picamera.Color('black')
        self.CamTimer()

        print("Camera initialization...")
        pass


    def StartPreview(self):
        self.__camera.start_preview()
        pass


    def StopPreview(self):
        self.__camera.stop_preview()
        self.__camera.close()
        pass


    def StartRecording(self):

        if not os.path.isdir(self.__path):
            os.makedirs(os.path.join(self.__path))

        currentDate = self.CurrentTimeDate()

        self.__camera.start_recording(self.__path + currentDate + ".h264")
        self.__currentRecFilename = str(currentDate + ".h264")
        print("Start Recording!")
        pass


    def StopRecording(self):
        self.__camera.stop_recording()
        print("Stop Recording!")
        pass


    def CamTimer(self):
        timer = threading.Timer(1, self.CamTimer)
        timer.daemon = True
        timer.start()

        self.__recordTime = self.__recordTime + 1
        pass


    def CurrentTimeDate(self):
        return time.strftime('[%Y-%m-%d] %I:%M:%S', time.localtime(time.time()))


    def UpdateText(self):

        # New video record. (30 minute = 1800s)
        if self.__recordTime > 1799 :
            self.__recordTime = 0
            self.StopRecording()

            uploaderThread = threading.Thread(target=self.Uploader, args=(self.__path, self.__currentRecFilename))
            uploaderThread.daemon= True
            uploaderThread.start()

            self.StartRecording()


        second = (int)(self.__recordTime % 60)
        minute = (int)((self.__recordTime % 3600) / 60)
        hour = (int)(self.__recordTime / 3600)

        timeStr = str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)
        curTimeStr = self.CurrentTimeDate()

        self.__camera.annotate_text = " %s " % (curTimeStr) + " (Rec time : %s) " % (timeStr)

        pass


    def Uploader(self, path, filename):
        try:
            self.__uploadManager.UploadVideo(path, filename)
            pass

        except Exception in exc:
            print("Upload error! : " + exc)
            pass

        pass

    pass


### Main
isLoop = True
try:
    cameraManager = CameraManager('/home/pi/Desktop/videos/')
    cameraManager.StartPreview()
    cameraManager.StartRecording()
except Exception as exc:
    print(exc)
    exit(1)

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
