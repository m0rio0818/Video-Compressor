import socket
import os

class Server:
    def __init__(self, address, port) -> None:
        self.address = address
        self.port = int(port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = 4096
        self.dpath = "./temp"
        
    def start(self):
        print("Starting up on {} port {}".format(self.address, self.port))
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
                header = connection.recv(5)
                filename_length = int.from_bytes(header[:1])
                filesize = int.from_bytes(header[1:])
                if filesize == 0:
                    raise Exception('No data  to read from client')
                
                filename = connection.recv(filename_length).decode()
                
                if not os.path.exists(self.dpath):
                    os.makedirs(self.dpath)
                
                # もしそのファイルが既に存在している場合。
                if not os.path.exists(os.path.join(self.dpath, filename)):
                    with open(os.path.join(self.dpath, filename), "wb+" ) as f:
                        while filesize > 0:
                            data = connection.recv(filesize if filesize  <= self.buffer else self.buffer)
                            f.write(data)
                            print("Recived {} bytes".format(len(data)))
                            filesize -= len(data)
                            print(filesize)        
                            if data:
                                print("Recived data: ", data)
                            else:
                                print("No data from:" , client_address)
                                break
                else:
                    print("そのファイル名+pathはすでに存在しています。")
            finally:
                print("Closing current connection")
                connection.close()
      
               
        

def main():
    server = Server("0.0.0.0",  9001)
    server.start()
    
if __name__ == "__main__":
    main()