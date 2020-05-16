#coding utf-8

### Parent class. (부모 클래스)
class Fruit:
    ## Member variable (멤버변수)
    name = 'None' # public (누구나 접근 가능)
    _fresh = 100  # protected (상속 관계인 클래스만 접근 가능)
    __amount = 0  # private (자신 외엔 접근 불가능)


    ## Initialization. (생성자)
    def __init__(self, ea):
        self.__amount = ea
        print('create %d fruit...' % (self.__amount))


    ## 멤버변수 출력 메서드
    def printInfo(self):
        print('name : ' + self.name)
        print('fresh : ' + str(self._fresh) + '%')
        print('amount : ' + str(self.__amount) + '\n')


    ## 상속 관계를 가진 자만 접근 가능한 메서드
    def _Protected_Level(self):
        print('protected lv\n')


    ## 자신 외엔 접근 불가능한 메서드
    def __Private_Level(self):
        print('private lv\n')



### Child class-1
class Apple(Fruit):

    ## Initialization.
    def __init__(self, ea):
        super().__init__(ea)
        self.name = 'apple'
        print('I am %s!\n' % (self.name))


    ## Member variable enter test. (접근 테스트 - 멤버변수)
    def EnterTest(self):
        # 예외 검사
        try:
            print('name : ' + self.name)
            print('fresh : ' + str(self._fresh) + '%')
            print('amount : ' + str(self.__amount))

        # 예외 발생 시 동작
        except AttributeError as exc :
            print('[Exception :: can\'t enter private variable.]\n')


    ## Method enter test. (접근 테스트 - 메서드)
    def EnterTest2(self):
        # 예외 검사
        try:
            self._Protected_Level()
            self._Private_Level()

        # 예외 발생 시 동작
        except Exception as exc :
            print('[Exception :: can\'t enter private method.]')

        # 예외 발생유무 상관없이 동작함
        finally:
            print('EnterTest2 close...\n')


    ## Override method.
    def printInfo(self):
        super().printInfo()
