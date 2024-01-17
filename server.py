import socket
import os

class Server:
    def __init__(self, address, port) -> None:
        self.address = address
        self.port = int(port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start(self):
        print("Starting up on {} port ".format(self.address, self.port))
        self.connect()
        self.reviveData()
        
    def connect(self):
        self.sock.bind((self.address, self.port))
        self.sock.listen(1)
                
    def reviveData(self):
        while True:
            connection, client_address = self.sock.accept()
            try:
                print("Connection from {} port {}".format(client_address[0], client_address[1]))
                while True:
                    data = connection.recvfrom(32)
                    print(data)
                    if data:
                        print("Recived data: ", data)
                    else:
                        print("No data from:" , client_address)
                        break
            finally:
                print("Closing current connection")
                connection.close()

def main():
    server = Server("0.0.0.0",  9001)
    server.start()
    
if __name__ == "__main__":
    main()