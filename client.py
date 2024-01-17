import socket
import os
import sys


class Client:
    def __init__(self, address, server_address, port, server_port) -> None:
        self.address = address
        self.server_address = server_address
        self.port = int(port)
        self.server_port = int(server_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def conncet(self):
        try:
            self.sock.connect((self.server_address, self.server_port))
        except socket.error as err:
            print("err", err)
            sys.exit(1)
            
    def start(self):
        self.conncet()
        self.sendData()
        
    def sendData(self):
        message = b"Hello my name is morio nakatani!"
        self.sock.sendall(message)
        print("sending data.....")
        self.sock.settimeout(2)
        
        try:
            while True:
                data = str(self.sock.recv(4096))
                if data:
                    print("Server response : ", data)
                else:
                    break
        except TimeoutError:
            print("No time, end listening for server response")
        finally:
            print("Closing socket")
            self.sock.close()
    

def main():
    client = Client("0.0.0.0", "0.0.0.0", 9050, 9001)
    client.start()
    
if __name__ == "__main__":
    main()
    