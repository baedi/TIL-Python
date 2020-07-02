import RPi.GPIO as gpio
import time as timeManager

class MotionSensor:
    
    ### VAR
    __pin_motionSensor = 40
    __pin_led = 35
    __count = 0
    
    
    ### INITIALIZATION
    def __init__(self):
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.__pin_motionSensor, gpio.IN)
        gpio.setup(self.__pin_led, gpio.OUT, initial = gpio.LOW)
        print("Complete initialization.")
        pass
    
    def Check(self):
        result = gpio.input(self.__pin_motionSensor)
        if result == 0 :
            print("No detect.")
            if self.__count > 0:
                self.__count = self.__count - 1
                
            else : self.__count = 0
            
        else :
            print("Detected!")
            self.__count = 8
            
        
        gpio.output(self.__pin_led, self.__count)
        
        timeManager.sleep(1)
    
    pass


### MAIN
manager = MotionSensor()

while True:
    try:
        manager.Check()
        pass
    
    except KeyboardInterrupt:
        break
    
    pass

print("System Exit...")
gpio.cleanup()