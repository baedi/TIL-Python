#coding utf-8

class PropertyTest:
    
    ## Property.
    @property
    def name(self) : return self.__name
    
    @property
    def money(self) : return self.__money
    
    @name.setter
    def name(self, value) : self.__name = value
    
    @money.setter
    def money(self, value) : self.__money = value
        
        
    ## Initialization.
    def __init__(self):
        print('Initialization!')
        self.__name = 'Default'
        self.__money = 0
        
    def Info(self):
        print("Info...")
        print("Name : %s" % (self.__name))
        print("Money : %d" % (self.__money))
        
        
### Main
test1 = PropertyTest()
test1.name = 'HongJa'
test1.money = 300000
print("Name : %s" % (test1.name))
print("Money : %d" % (test1.money))