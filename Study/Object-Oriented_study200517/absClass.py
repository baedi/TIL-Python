from abc import * #abc : abctract base class

### 추상 클래스
class Abs_Mode(metaclass=ABCMeta):

    ## 자식 클래스에서 반드시 오버라이드해야 되는 메서드 3개
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def play(self, value):
        pass

    @abstractmethod
    def loop(self):
        pass


### 자식 클래스 1
class MainMenu(Abs_Mode):

    ## 멤버변수
    name = 'MainMenu Title'
    version = 0.1
    volume = 50


    def info(self):
        print('name : ' + self.name)
        print('version : %d\n' % (self.version))

    def play(self, value):
        self.volume = value
        print('change volume : %d\n' % (self.volume))

    def loop(self):
        counter = 0
        while counter < 5 :
            print('counter : %d' % (counter))
            counter = counter + 1
        print('\n')


### 자식 클래스 2
class GamePlay(Abs_Mode):

    ## 멤버변수
    playerHP = 200
    power = 300


    def info(self):
        print('player HP : %d' % (self.playerHP))
        print('power : %d\n' % (self.power))

    def play(self, value):
        self.playerHP = self.playerHP - value
        print('ouch! player HP is %d...\n' % (self.playerHP))

    def loop(self):
        counter = 0
        while counter < 10 :
            print('counter : %d' % (counter))
            counter = counter + 2
        print('\n')
