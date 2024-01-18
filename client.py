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
        path = "./video/sample-5s.mp4"
        try:
            with open(path, "rb") as f:
                print(os.SEEK_END)
                f.seek(0, os.SEEK_END)
                filesize = f.tell()
                print(filesize)
                f.seek(0, 0)
                
                if filesize > pow(2, 32):
                    raise Exception("file size must be below 4GB")
                
                filename = os.path.basename(f.name)
                
                if self.checkFileType(filename) == "mp4":
                    print("ファイル拡張子は mp4です")
                
                # まずファイルサイズを送信
                header = self.makeHeader(len(filename), filesize)
                self.sock.sendall(header)
                self.sock.sendall(bytes(filename, "utf-8"))
                message = f.read()
                print(message)
                print("sending data.....")
                self.sock.sendall(message)
        except KeyboardInterrupt :
            print("キーボードが押されました。")
            
        self.sock.settimeout(2)
        
        try:
            while True:
                data = self.sock.recv(4096)
                if data:
                    print("Server response : ", str(data))
                else:
                    break
        except TimeoutError:
            print("No time, end listening for server response")
        finally:
            print("Closing socket")
            self.sock.close()
   
    def makeHeader(self, filename_length, filesize):
        return  filename_length.to_bytes(1, "big") + filesize.to_bytes(4, "big") 
    
    def checkFileType(self, filename):
        return filename[filename.find(".")+1:]     
    

def main():
    client = Client("0.0.0.0", "0.0.0.0", 9050, 9001)
    client.start()
    
if __name__ == "__main__":
    main()
    