#coding utf-8

### Library(라이브러리) ###
import threading
import time
import sys

### Thread class ###
class ThreadTest2 :

    ## Member Variable. (멤버변수)
    __isThreadON = False
    __counter = 0
    thread = None

    ## Initialization. (생성자)
    def __init__(self):
        print('Initialization!')
        self.thread = threading.Thread(target=self.run)
        #self.thread.daemon = True

    ## Thread on method. (스레드의 요소를 반복 동작할지 여부)
    def setIsThreadOn(self, mode) :
        self.__isThreadON = mode

    ## Thread setting reset method. (사용한 스레드를 재사용하기 위함)
    def resetThreadSetting(self) :
        self.thread = threading.Thread(target=self.run)
        #self.thread.daemon = True

    ## Getter::__counter method. (카운터 값을 리턴함)
    def getCounter(self) :
        return int(self.__counter)

    ## Thread method. (스레드 시작 시 동작하는 메서드)
    def run(self):
        while self.__isThreadON :
            print('counter : %d' % (self.__counter))
            time.sleep(1)
            self.__counter = self.__counter + 1



### Main ###

## Variable
input_val = 0

## Create object
obj = ThreadTest2()


## Loop (반복)
while int(input_val) != -1 :
    print('[0 : Thread on, 1 : Thread off, 2 : check count, -1 : Exit]')
    input_val = input('Input : ') # 입력

    try:
        # 0번 입력 시 -> 스레드 시작
        if int(input_val) == 0 :
            obj.setIsThreadOn(True)
            obj.thread.start()

        # 1번 입력 시 -> 스레드 정지
        elif int(input_val) == 1 :
            obj.setIsThreadOn(False)

            # 스레드가 살아있을 경우 동작
            if obj.thread.is_alive() :
                # join thread untii the end of the run()
                # (스레드의 run()동작이 끝날때까지 대기함)
                obj.thread.join()

            # 스레드 재사용을 위한 함수 호출
            obj.resetThreadSetting()

        # 2번 입력 시 -> 카운터 값 가져와서 출력하기
        elif int(input_val) == 2 :
            print('current counter : %d' % (obj.getCounter()))

    # 예외 발생 시 프로그램 종료
    except RuntimeError :
        print('RuntimeError!')
        exit(0)


print('program exit...')
