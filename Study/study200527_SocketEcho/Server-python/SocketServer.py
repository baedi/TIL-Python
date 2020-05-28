import socket

class SockServer:
    
    ## Member variable.
    __host = None
    __port = None
    __server_sock = None
    __client_sock = None
    
    
    ## Initialization.
    def __init__(self, host, port):
        ## Set host and port
        self.__host = host
        self.__port = port
        pass
        
        
    ## Server open.
    def OpenServer(self):
        self.__server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("%s :%d" % (self.__host, self.__port))
        self.__server_sock.bind((self.__host, self.__port))
        
        # Wait client connect...
        print("Wait...")
        self.__server_sock.listen()
        self.__client_sock, addr = self.__server_sock.accept()
        
        print("Client connected! (info : %s)" % (str(addr)))

        # receive message...
        comment = self.__client_sock.recv(1024)
        print("Client : %s" % (comment.decode('utf-8')))
        self.__client_sock.sendall(comment)
        
        self.__client_sock.close()
        self.__server_sock.close()
        pass
    
    pass


### Main
host = input("Host : ")
port = input("Port : ")

server = SockServer(str(host), int(port))
server.OpenServer()