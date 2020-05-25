
### Class
class StaticTest:
    __name = None
    __number = 0
    __state = False
    __CREATE_NUMBER = 20200524
    
    def __init__(self):
        print("StaticTest Initialization!")
        
    def Info_objmode(self):
        print("[Called Info_objmode]")
        print("Name : " + str(self.__name))
        print("Number : " + str(self.__number))
        print("State : " + str(self.__state))
        print("C-Num : " + str(self.__CREATE_NUMBER))
        print("\n")
    
    @staticmethod
    def StaticMethod():
        print("Oh you called StaticMethod!\n")
    
    @staticmethod
    def PlusCal(x, y):
        return x + y
    
    @classmethod
    def Info(cls):
        print("[Called Info_staticmode]")
        print("Name : " + str(cls.__name))
        print("Number : " + str(cls.__number))
        print("State : " + str(cls.__state))
        print("C-Num : " + str(cls.__CREATE_NUMBER))
        print("\n")
        
    @classmethod
    def ChangeName(cls, input_):
        cls.__name = input_
        
        
        
### Main

# call static method 1
StaticTest.StaticMethod()

# call static method 2
print("Result : %d\n" % (StaticTest.PlusCal(10, 20)))

# call class-static method 1
StaticTest.Info()

# call class-static method 2
StaticTest.ChangeName("Hoon")
StaticTest.Info()

# create object
obj1 = StaticTest()
obj1.Info_objmode()

# change name (static mode)
StaticTest.ChangeName("Taekuun")
obj1.Info_objmode()
