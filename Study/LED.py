#coding utf-8

### GPIO Library import     ... GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)    # Pin number (할당 방법 설정 : GPIO 핀으로 할당)
# GPIO.setwarnings(False)   # GPIO.cleanup이 되지 않았을 때 나오는 Warning 방지
LED_PIN = 12                # GPIO LED Pin (GPIO 12번 핀)

### LED_PIN <- Output Mode (Start : LowMode)        ... LED_PIN을 출력 모드로 설정, 초기값은 LOW
GPIO.setup(LED_PIN, GPIO.OUT, initial = GPIO.LOW)

### Exception check     ... 예외 검사
try:
    while True :
        ## input 0 or 1
        print('Input (0 or 1) : ')
        input_value = input()

        ## LED ON
        if int(input_value) == 1 :
            GPIO.output(LED_PIN, GPIO.HIGH)

        ## LED OFF
        elif int(input_value) == 0 :
            GPIO.output(LED_PIN, GPIO.LOW)

        ## Exit
        else :
            break


### Ctrl + C 눌렀을 시 예외 발생.
except KeyboardInterrupt:
    pass        # 아무것도 하지 않음.

### GPIO Cleanup
GPIO.cleanup()

print('\n\nExit py')
