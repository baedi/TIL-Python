import socket
import threading

class SockServer:
    
    ## Member variable.
    __host = None
    __port = 50000
    __server_sock = None
    __client_sock = None
    __thread = None
    __threadOn = False
    
    
    ## Initialization.
    def __init__(self, host):
        ## Set host and port
        self.__host = host
        self.__thread = threading.Thread(target=self.ReceiveMessage)
        self.__thread.daemon = True
        self.__threadOn = True
        pass
        
        
    ## Server open.
    def OpenServer(self):
        self.__server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("%s:%d\n" % (self.__host, self.__port))
        self.__server_sock.bind((self.__host, self.__port))
        
        # Wait client connect...
        print("Wait...\n")
        self.__server_sock.listen()
        self.__client_sock, addr = self.__server_sock.accept()
        
        print("Client connected! (info : %s)\n" % (str(addr)))
        pass
    
    
    ## Receive Message. 
    def ReceiveMessage(self):
        
        while True:
            # receive message...
            message = self.__client_sock.recv(4)
            length = int.from_bytes(message, "big")
        
            message = self.__client_sock.recv(length)
            print("Client : %s\n" % (message.decode('utf-8')))
            self.__client_sock.sendall(message)
            pass
    
        pass
    
    
    ## Send Message
    def SendMessage(self):
        
        while True:
            
            message = input()
            self.__client_sock.send(message.encode())
            
            if str(message) == " " : break
            pass
        pass
    
    
    
    def GetThread(self): return self.__thread
    
    
    def StopThread(self):
        self.__threadOn = False
        self.__thread.join()
        
    
    def DisconectSever(self):
        # Disconnect.
        self.__client_sock.close()
        self.__server_sock.close()
        pass
    
    pass


### Main
host = input("Host : ")

server = SockServer(str(host))
server.OpenServer()

server.GetThread().start()
server.SendMessage()

server.DisconectSever()