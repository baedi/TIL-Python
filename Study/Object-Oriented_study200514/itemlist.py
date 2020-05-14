#coding utf-8

### Parent class.
class Item :

    ## Member variable.
    name = 'Default'
    amount = 5
    
    ## Initialization.
    def __init__(self):
        print('Item initialization!')
    
    ## method.
    def using(self, ea):
        
        if self.amount > ea : 
            self.amount = self.amount - ea
            print('Using %d item' % (ea))
        
        else :
            print('Not enought item...')
        
    ## method2.
    def checkAmount(self) :
        print('%s amount : %d' % (self.name, self.amount))
    
    
### Child class.
class Potion(Item):
    
    ## Member Variable.
    effect = 100
    
    ## Initialization.
    def __init__(self):
        super().__init__()
        print('Potion initialization!')
        self.name = 'Potion'
        
    ## Override method.
    def using(self, ea):
        super().using(ea)
        return self.effect * ea
        