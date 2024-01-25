import socket
import os
import sys
import json
from MMP import MMP


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
        except ConnectionError:
            print("サーバーが起動されていません。")
            sys.exit(1)
        except socket.error as err:
            print("err", err)
            sys.exit(1)
            
    def start(self):
        path = "./video/sample.m3"
        if os.path.exists(path):    
            self.conncet()
            self.sendData()
        else:
            print("そのパスは存在しません。")
        
        
    def sendData(self, path):
        try:
            with open(path, "rb") as f:
                f.seek(0, os.SEEK_END)
                filesize = f.tell()
                f.seek(0, 0)
                
                if filesize > pow(2, 32):
                    raise Exception("file size must be below 4GB")
                
                filename = os.path.basename(f.name)
                
                if self.checkFileType(filename) == "mp4":
                    print("ファイル拡張子は mp4です")
                    # JSONファイルの読み込み
                    with open("./request.json", "r") as f2:
                        json_data = f2.read()
                        json_len = len(json_data)
                    print("data: ", json_data,"jsonlen" ,json_len)
                    
                    header = MMP.makeHeader(json_len, len(self.checkFileType(filename)), filesize)
                    # ヘッダーの送信
                    self.sock.sendall(header)
                
                    # 次にボディの送信
                    body = json_data.encode("utf-8") + self.checkFileType(filename).encode("utf-8") + f.read()
                    self.sock.sendall(body)
                    print("ボディの送信まで完了しました。")
                else:
                    print("その拡張子のファイルは送信できません。")
        
        except TimeoutError:
            print("Time out!")    
    
        except KeyboardInterrupt :
            print("キーボードが押されました。")
        
        finally:
            print("Closing socket")
            self.sock.close()
        
    
    def makeHeaderD(self, jsonSize, mediaTypeSize, payloadSize):
        return  jsonSize.to_bytes(16, "big") + mediaTypeSize.to_bytes(1, "big") + payloadSize.to_bytes(47, "big")
    
    def makeHeader(self, filename_length, filesize):
        return  filename_length.to_bytes(1, "big") + filesize.to_bytes(4, "big") 
    
    def checkFileType(self, filename):
        return filename[filename.find(".")+1:]     
    

def main():
    client = Client("0.0.0.0", "0.0.0.0", 9050, 9001)
    client.start()
    
if __name__ == "__main__":
    main()
    