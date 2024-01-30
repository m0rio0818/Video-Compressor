import socket
import os
import sys
import json
from MMP import MMP


class Client:
    def __init__(self, address, server_address, port, server_port) -> None:
        self.HEADER_BYTES_SIZE = 64
        self.address = address
        self.server_address = server_address
        self.port = int(port)
        self.buffer = 4096
        self.server_port = int(server_port)
        self.dpath = "video"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        
    def conncet(self):
        try:
            self.sock.connect((self.server_address, self.server_port))
        except ConnectionError:
            print("サーバーが起動されていません。")
            sys.exit(1)
        except socket.error as err:
            print("err", err)
            sys.exit(1)
            
    def start(self):
        input_path = "./video/sample.mp4"
        output_filename = "sample"
        if os.path.exists(input_path):    
            self.conncet()
            self.sendData(input_path)
            self.reciveResponse(output_filename)
        else:
            print("そのパスは存在しません。")
            
    def select_file(self):
        path = input("input filename which you want to select")
                
        
    def sendData(self, path):
        try:
            with open(path, "rb") as f:
                f.seek(0, os.SEEK_END)
                filesize = f.tell()
                f.seek(0, 0)
                
                if filesize > pow(2, 32):
                    raise Exception("file size must be below 4GB")
                
                filename = os.path.basename(f.name)
                
                if MMP.checkFileType(filename) == "mp4":
                    print("ファイル拡張子は mp4です")
                    # JSONファイルの読み込み
                    with open("./json/request.json", "r") as f2:
                        json_data = f2.read()
                        json_len = len(json_data)
                    print("data: ", json_data,"jsonlen" ,json_len)
                    
                    header = MMP.makeHeader(json_len, len(MMP.checkFileType(filename)), filesize)
                    # ヘッダーの送信
                    self.sock.sendall(header)
                
                    # 次にボディの送信
                    body = json_data.encode("utf-8") + MMP.checkFileType(filename).encode("utf-8") + f.read()
                    self.sock.sendall(body)
                    print("ボディの送信まで完了しました。")
                else:
                    print("その拡張子のファイルは送信できません。")
            
    
        except KeyboardInterrupt :
            print("キーボードが押されました。")
        
        
    def savePayload(self, connection, filesize, filename ,mediaType):
        totalRecived = 0        
        print("mediaType", mediaType)
        output_path = "{}/{}.{}".format(self.dpath, filename, mediaType)
        with open(output_path, "wb") as f:
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
            
    def reciveResponse(self, filename):
        try:
            while True:
                print("今からレスポンスを待ちます。")
                header = self.sock.recv(self.HEADER_BYTES_SIZE)
                jsonSize = int.from_bytes(header[:16])
                mediaTypeSize = int.from_bytes(header[16:17])
                payloadSize = int.from_bytes(header[17:])
                print(jsonSize, mediaTypeSize, payloadSize)

                
                # body 受け取り
                jsonData = self.sock.recv(jsonSize).decode()
                mediaType = self.sock.recv(mediaTypeSize).decode()
                
                self.savePayload(self.sock, payloadSize, filename, mediaType)
                # if data:
                #     print("Server response:", data)
                # else:
                #     break
                break
        finally:
            print("Closing socket")
            self.sock.close()
              
    

def main():
    client = Client("0.0.0.0", "0.0.0.0", 9050, 9001)
    client.start()
    
if __name__ == "__main__":
    main()
    