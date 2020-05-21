#coding utf-8

### Class.
class FileManager:
    
    ## Member Variable.
    __file = None
    
    ## Initialization.
    def __init__(self):
        print("File manager initialization...")
        
    def CreateFile(self, name):
        self.__file = open("%s.txt" % (name), 'w')
        print("Success create file!")
        
    def ReadFile(self, name):
        self.__file = open("%s.txt" % (name), 'r')
        
        while True :
            linestr = self.__file.readline()
            if not linestr: break
            print(linestr)
            
            
        
    def AppendFile(self, name):
        self.__file = open("%s.txt" % (name), 'a')
        
    def CloseFile(self):
        if self.__file != None : 
            self.__file.close();
    
    ## Get _file Reference Method.
    def GetFileReference(self):
        return __file
