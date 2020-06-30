import RPi.GPIO as GPIO
import time


class Seg7Manager:
    
    ### VARIABLE
    __segNumber = int(0)
    __gpio_pinList = [7, 11, 12, 13, 15, 16, 18]
    __button1_state = None
    __button2_state = None
    
    ### INITIALIZATION
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.__gpio_pinList[0], GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.__gpio_pinList[1], GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.__gpio_pinList[2], GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.__gpio_pinList[3], GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.__gpio_pinList[4], GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.__gpio_pinList[5], GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.__gpio_pinList[6], GPIO.OUT, initial = GPIO.LOW)
        
        GPIO.setup(37, GPIO.IN)
        GPIO.setup(38, GPIO.IN)
        
        self.__button1_state = GPIO.input(37)
        self.__button2_state = GPIO.input(38)
        
        print("Success GPIO Setup")
        self.OutputSegmentNumber()
        pass
    
    
    ### Check button state
    def ButtonState(self):
        button1 = GPIO.input(37)
        button2 = GPIO.input(38)
        
        # button1 check
        if button1 != self.__button1_state:
            self.__button1_state = button1
            
            if button1 == GPIO.LOW:
                self.__segNumber = self.__segNumber + 1
                print("Button1 pressed " + "(count : " + str(self.__segNumber) + ")")
                
                self.OutputSegmentNumber()
                pass
            pass
        
        # button2 check
        if button2 != self.__button2_state:
            self.__button2_state = button2
            
            if button2 == GPIO.LOW:
                self.__segNumber = self.__segNumber - 1
                print("Button2 pressed " + "(count : " + str(self.__segNumber) + ")")
                
                self.OutputSegmentNumber()
                pass
            pass
        
        pass
    
    
    ### Print 7-Segment
    def OutputSegmentNumber(self):
        
        hexList = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]
        result = abs(self.__segNumber) % 10
        forCount = 0
        
        for segNumPart in self.__gpio_pinList:
            if (hexList[result] & (1 << forCount)) == 0 :
                GPIO.output(self.__gpio_pinList[forCount], GPIO.LOW)
                pass
            
            else :
                GPIO.output(self.__gpio_pinList[forCount], GPIO.HIGH)                
                pass
            
            forCount = forCount + 1
        
        
        pass
    
        
    pass



### MAIN

segManager = Seg7Manager()

try:
    while True:
        segManager.ButtonState()
        pass
    pass

except KeyboardInterrupt:
    pass



print("Exit program")
GPIO.cleanup()