
class TestClass_List:
    
    ## Member Variable.
    __number = None
    __name = None

    ## Initialization
    def __init__(self, number, name):
        
        self.__number = number
        self.__name = name
        
        print('TestClass_List Initialization!')
        
    
    ## get, set
    def GetNumber(self) : return self.__number
    def GetName(self) : return self.__name
    
    def SetNumber(self, number) : self.__number = number
    def SetName(self, name) : self.__name = name