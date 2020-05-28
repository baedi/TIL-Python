import socket

class SockServer:
    
    ## Member variable.
    __host = None
    __port = 50000
    __server_sock = None
    __client_sock = None
    
    
    ## Initialization.
    def __init__(self, host):
        ## Set host and port
        self.__host = host
        pass
        
        
    ## Server open.
    def OpenServer(self):
        self.__server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("%s:%d" % (self.__host, self.__port))
        self.__server_sock.bind((self.__host, self.__port))
        
        # Wait client connect...
        print("Wait...")
        self.__server_sock.listen()
        self.__client_sock, addr = self.__server_sock.accept()
        
        print("Client connected! (info : %s)" % (str(addr)))

        # receive message...
        message = self.__client_sock.recv(4)
        print("Received!")
        length = int.from_bytes(message, "big")
        
        message = self.__client_sock.recv(length)
        print("Client : %s" % (message.decode('utf-8')))
        
        
        
        self.__client_sock.sendall(message)
        
        
        # Disconnect.
        self.__client_sock.close()
        self.__server_sock.close()
        pass
    
    pass


### Main
host = input("Host : ")

server = SockServer(str(host))
server.OpenServer()