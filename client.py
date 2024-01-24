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
        except socket.error as err:
            print("err", err)
            sys.exit(1)
            
    def start(self):
        self.conncet()
        self.sendData()
        
        
    def sendData(self):
        path = "./video/sample.mp4"
        try:           
            with open(path, "rb") as f:
                f.seek(0, os.SEEK_END)
                filesize = f.tell()
                f.seek(0, 0)
                
                if filesize > pow(2, 32):
                    raise Exception("file size must be below 4GB")
                
                filename = os.path.basename(f.name)
                
                # JSONファイルの読み込み
                with open("./request.json", "r") as f2:
                    json_data = f2.read()
                    json_len = len(json_data)
                print("data: ",json_data,"jsonlen" ,json_len)
                
                header = MMP.makeHeader(json_len, len(self.checkFileType(filename)), filesize)
                # ヘッダーの送信
                self.sock.sendall(header)
            
                # 次にボディの送信
                body = json_data.encode("utf-8") + self.checkFileType(filename).encode("utf-8") + f.read()
                self.sock.sendall(body)
                print("ボディの送信まで完了しました。")
                
                                
                if self.checkFileType(filename) == "mp4":
                    print("ファイル拡張子は mp4です")
                    # header = self.makeHeader(len(filename), filesize)
                    # filesize, filename_lengthを送信
                    # filenameを送信
                    # self.sock.sendall(bytes(filename, "utf-8"))
                    data = self.sock.recv(2)
    
                    if int.from_bytes(data) == 400:
                        print("ファイルは存在してません。")
                        message = f.read()
                        print("sending data.....")
                        try:
                            self.sock.sendall(message)
                            print("ファイルの送信が完了しました。")
                        except BrokenPipeError as e:
                            print(f"BrokenPipeError: {e}")
                        except ConnectionResetError as e:
                            print(f"ConnectionResetError: {e}")
                        # finally:
                        #     self.sock.settimeout(2)
                        
                    else:
                        print("ファイルはすでに存在しています。")
                else:
                    print("その拡張子のファイルは送信できません。")
            
            
            # ここでサーバーのレスポンスチェック 正常アップロード完了 or　アップロードできていないか。
            data = self.sock.recv(2)
            if data:
                print("responseがありました。")
                if (int.from_bytes(data) == 404):
                    print("Server にVideoをアップロード中に問題が発生しました。再度実行してください")
                elif (int.from_bytes(data) == 200):
                    print("アップロードは正常終了しました。")
                
                
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
    