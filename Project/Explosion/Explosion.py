import RPi.GPIO as gpio
import time
import threading


class Explosion:

    ### Variable
    __value = 60
    __pinList = [7, 11, 12, 13, 15, 16, 18]
    __pinArgs = [35, 36]
    __pinBuzzer = 32
    __hexList = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]

    __timer = None
    __thread = None
    __buzzerManager = None

    __time_current = 0
    __time_prev = 0

    isThreadOn = False
    buzCount = 0


    ### Initialization
    def __init__(self):
        gpio.setmode(gpio.BOARD)

        for count in range(0, len(self.__pinList)):
            gpio.setup(self.__pinList[count], gpio.OUT, initial = gpio.LOW)
            pass


        gpio.setup(self.__pinArgs[0], gpio.OUT, initial = gpio.HIGH)
        gpio.setup(self.__pinArgs[1], gpio.OUT, initial = gpio.HIGH)
        gpio.setup(self.__pinBuzzer, gpio.OUT, initial = gpio.HIGH)

        self.__buzzerManager = gpio.PWM(self.__pinBuzzer, 100)

        self.__time_current = time.time() + (self.__value * 0.05)

        self.beginTimer()
        self.beginThread()

        pass


    def ComSettings(self):

        for index in range(0, len(self.__pinArgs)):

            result = 0

            # a digit of '10'
            if index == 0 :
                result = int(self.__value / 10)
                pass

            # a digit of '1'
            elif index == 1 :
                result = int(self.__value % 10)
                pass


            # ...
            forCount = 0
            for segNumPart in self.__pinList:
                if (self.__hexList[result] & (1 << forCount)) == 0 :
                    gpio.output(self.__pinList[forCount], gpio.LOW)
                    pass

                else :
                    gpio.output(self.__pinList[forCount], gpio.HIGH)
                    pass

                forCount = forCount + 1
                pass


            # target argunent only 'LOW'
            for index2 in range(0, len(self.__pinArgs)):
                if index == index2 :
                    gpio.output(self.__pinArgs[index2], gpio.LOW)
                    pass

                else :
                    gpio.output(self.__pinArgs[index2], gpio.HIGH)
                    pass

                pass


            time.sleep(0.01)
            pass

        pass


    def GetValue(self):
        return self.__value


    def beginTimer(self):
        self.__timer = threading.Timer(1, self.beginTimer)
        self.__timer.daemon = True
        self.__timer.start()

        self.__value = self.__value - 1
        pass


    def beginThread(self):
        self.__thread = threading.Thread(target = self.ThreadManager)
        self.__thread.daemon = True
        self.isThreadOn = True
        self.__thread.start()
        pass


    def ThreadManager(self):
        while self.isThreadOn :

            if self.__time_current - time.time() < 0:
                self.buzCount = self.buzCount + 1
                print("count : " + str(self.buzCount))
                self.__time_current = time.time() + (self.__value * 0.05)

                self.__buzzerManager.start(100)
                self.__buzzerManager.ChangeDutyCycle(50)
                self.__buzzerManager.ChangeFrequency(650)
                time.sleep(0.02)
                self.__buzzerManager.stop()


        pass


    pass


### Main

manager = Explosion()

try:
    while manager.GetValue() >= 0:
        manager.ComSettings()
        pass
    pass
except KeyboardInterrupt:
    pass

gpio.cleanup()
manager.isThreadOn = False
print("Exit program")
