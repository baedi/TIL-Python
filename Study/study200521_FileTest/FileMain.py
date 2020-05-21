#coding utf-8

### Library
import FileManager

fileManager = FileManager.FileManager()
select = None

while True :
    print("[SELECT] (1 : CREATE | 2 : READ | 3 : APPEND | 4 : WRITE | 0 : EXIT) ")
    select = int(input("Input : "))
    
    if select == 1 :
        fileManager.CreateFile(input("File name : "))
        fileManager.CloseFile()
        
    elif select == 2 :
        print("Read file...\n")
        fileManager.ReadFile(input("File name : "))
        fileManager.CloseFile()
        
    elif select == 3 :
        print('')
        
    elif select == 4 :
        print('')
        
    elif select == 0 :
        print("Close file...")
        fileManager.CloseFile()
        break
        
    else :
        print("Invalid access...")