import socket
import os

class Server:
    def __init__(self, address, port) -> None:
        self.address = address
        self.port = int(port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = 4096
        self.dpath = "./temp"
        self.HEADER_BYTES_SIZE = 64
        
    def start(self):
        print("Starting up on {} port {}".format(self.address, self.port))
        self.connect()
        self.reviveData()
        
    def connect(self):
        self.sock.bind((self.address, self.port))
        self.sock.listen(1)
        
    def savePayload(self, connection, filesize, mediaType):
        totalRecived = 0
        fSize = filesize
        if not os.path.exists(self.dpath):
            os.makedirs(self.dpath)
                    
        with open(os.path.join(self.dpath, "something." + mediaType), "wb") as f:
            while filesize > 0:
                try:
                    data = connection.recv(min(filesize, self.buffer))
                    if not data:
                        print("NO DATA")
                        break
                    f.write(data)
                    filesize -= len(data) 
                    totalRecived += len(data)
                except Exception as e:
                    print("Error ", e)
            print("データの受信は終了しました。")
                
                
    def reviveData(self):
        while True:
            connection, client_address = self.sock.accept()
            try:
                print("Connection from {} port {}".format(client_address[0], client_address[1]))
                
                # header 受け取り
                header = connection.recv(self.HEADER_BYTES_SIZE)
                jsonSize = int.from_bytes(header[:16])
                mediaTypeSize = int.from_bytes(header[16:17])
                payloadSize = int.from_bytes(header[17:])
                
                if payloadSize == 0:
                    raise Exception('No data to read from client')
                
                # body 受け取り
                jsonData = connection.recv(jsonSize).decode()
                mediaType = connection.recv(mediaTypeSize).decode()
                self.savePayload(connection, payloadSize, mediaType)
                
                method = jsonData["method"]
                params = jsonData["params"]
                # 圧縮 compression
                # 解像度　resolution
                # アスペクト aspect
                # 音声変更 mp3
                # GIForWEBM gifwebm
                
                if method == "compression":
                    self.compressionData()
                elif method == "resolution":
                    self.changeResolution()
                elif method == "aspect":
                    self.changeAspect()
                elif method == "mp3":
                    self.changeToMp3()
                elif method == "gifwebm":
                    self.makeGIForWEBM()               
            
            except OSError as e:
                print(f"Error: {e}")
                    
            finally:
                print("Closing current connection")
                connection.close()
    
   
    
    # 動画を圧縮
    def compressionData(self):
        return 
    
    # 動画の解像度を変更する
    def changeResolution(self):
        return
    
    # 動画のアスペクト比を変更
    def changeAspect(self):
        return
    
    # 動画 to 音声
    def changeToMp3(self):
        return
    
    # 指定した時間範囲で GIF や WEBM を作成
    def makeGIForWEBM(self):
        return
      
      

               
        

def main():
    server = Server("0.0.0.0",  9001)
    server.start()
    
if __name__ == "__main__":
    main()