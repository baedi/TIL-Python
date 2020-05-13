#coding utf-8

class TestClass:

    # Member variable   (멤버변수)
    name = ' '
    number = 0

    # Initialization Method.    (생성자)
    def __init__(self, number, str_):
        super().__init__()
        print('initialization')
        print('Hello %s! your number is %d' % (str_, number))

        self.name = str_
        self.number = number


    # Infomation print Method.  (사용자 정의 메서드)
    def printer(self):
        print('\n' + 'name : ' + self.name)
        print('number : ' + str(self.number) + '\n')
