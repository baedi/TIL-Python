#coding utf-8

### Library
import threading    # 스레드
import time         # 타이머

# 스레드를 상속받은 TimerManager 클래스
class TimerManager(threading.Thread) :

    ### Member Variable (멤버변수)
    count = -1          # 타이머용 카운터 변수
    th_count2 = -1      # 스레드용 카운터 변수

    timer = 0       # 타이머용 객체
    thread = 0      # 스레드용 객체


    ### Initialization. (생성자)
    def __init__(self):
        print('Init!')
        threading.Thread.__init__(self)
        self.interruptTimer()
        thread = threading.Thread(target=self.threadProcess)
        thread.start()

    ### timer
    def interruptTimer(self):
        # 자기 자신 메서드를 타이머로 지정 (1초마다 호출됨)
        self.timer = threading.Timer(1, self.interruptTimer)
        self.timer.start();
        self.count = self.count + 1
        print('[timer] Count : %d' % (self.count))

    ### thread (can't use self)
    # 클래스 내에서 호출된 스레드 메서드. 이 클래스 내에서의 멤버변수는 사용 못함.
    def threadProcess(self):
        th_count = 0

        while th_count < 10 :
            time.sleep(1.5)
            th_count = th_count + 1
            print('[threadProcess()] thCount : %d' % (th_count))

    ### thread2 (use self)
    # 외부에서의 객체 인스턴스에서 start 호출 시 이 함수가 실행됨.
    def run(self):
        # th_count2가 20보다 작으면 참, th_count 1씩 증가
        while self.th_count2 < 20 :
            time.sleep(0.2)
            self.th_count2 = self.th_count2 + 1
            print('[run()] th_count2 : %d' % (self.th_count2))
