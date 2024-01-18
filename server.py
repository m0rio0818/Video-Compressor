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
                print(filename)
                
                if not os.path.exists(self.dpath):
                    os.makedirs(self.dpath)
                
                # もしそのファイルが既に存在している場合。
                totalRecived = 0
                fSize = filesize
                if not os.path.exists(os.path.join(self.dpath, filename)):
                    print("そのファイルは存在していません。")
                    message = self.responseStatus(400)
                    connection.send(message)
                    with open(os.path.join(self.dpath, filename), "wb+" ) as f:
                        while filesize > 0:
                            data = connection.recv(filesize if filesize  <= self.buffer else self.buffer)
                            f.write(data)
                            # print("Recived {} bytes".format(len(data)))
                            filesize -= len(data)
                            totalRecived += len(data)
                    
                    if totalRecived != fSize:
                        print("ファイル作成の途中で中断されました。")
                    print("ファイルが作成されました。")     
                
                else:
                    print("そのファイル名+pathはすでに存在しています。")
                    message = self.responseStatus(300)
                    print(message)
                    connection.send(message)
                    
            finally:
                print("Closing current connection")
                connection.close()
    
    def responseStatus(self, status):
        return status.to_bytes(2, "big")
      
               
        

def main():
    server = Server("0.0.0.0",  9001)
    server.start()
    
if __name__ == "__main__":
    main()