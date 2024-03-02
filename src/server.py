import socket
import os
import json
from MMP import MMP

class Server:
    def __init__(self, address, port) -> None:
        self.address = address
        self.port = int(port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = 4096
        self.dpath = "../temp"
        self.HEADER_BYTES_SIZE = 64
        
    def start(self):
        print("Starting up on {} port {}".format(self.address, self.port))
        self.connect()
        self.reviveData()
        
    def connect(self):
        self.sock.bind((self.address, self.port))
        self.sock.listen(1)
        
    def savePayload(self, connection, filesize, input_path):
        totalRecived = 0
        fSize = filesize
        if not os.path.exists(self.dpath):
            os.makedirs(self.dpath)
                    
        with open(input_path, "wb") as f:
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
            
    def covert_MP4_Video(self, connection, input_path, output_path, method, custom, params=None):
        # 圧縮 compression
        # 解像度　resolution
        # アスペクト aspect
        # 音声変更 mp3
        # GIForWEBM gifwebm
        if method == "compression":
            MMP.compressionData(input_path, output_path, custom)
            self.loadAndSend(connection, output_path)
            self.deleteVideo(output_path)   
        elif method == "resolution":
            MMP.changeResolution(input_path, output_path, custom, params)
            self.loadAndSend(connection, output_path)
            self.deleteVideo(output_path)   
        elif method == "aspect":
            MMP.changeAspect(input_path, output_path, 0, params[1])
            self.loadAndSend(connection, output_path)
            self.deleteVideo(output_path)   
        elif method == "mp3":
            MMP.changeToMp3(input_path, output_path, params[0])
            self.loadAndSend(connection, output_path)
            self.deleteVideo(output_path)   
        elif method == "gifwebm":
            MMP.makeGIForWEBM(input_path, output_path, params[0])
            self.loadAndSend(connection, output_path)
            self.deleteVideo(output_path)   
                
                
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
                jsonReqeuest = json.loads(jsonData)
               
                filepath = jsonReqeuest["filepath"]
                method = jsonReqeuest["method"]
                custom = jsonReqeuest["custom"]
                params = jsonReqeuest["params"]
                res_type = jsonReqeuest["res_type"]
        
                print("method: ", method, "params: ", params,"custom:", custom, "res_type", res_type)
                
                input_path = os.path.join(self.dpath, "recived.{}".format(mediaType))
                output_path  = os.path.join(self.dpath, "response.{}".format(res_type))
                print("input: ",input_path, "output_path: ",output_path)
                
                
                self.savePayload(connection, payloadSize, input_path)
                print("ファイルは一旦サーバーに保存されました。")
                
                self.covert_MP4_Video(connection, input_path, output_path, method, params)
            
            except OSError as e:
                print(f"Error: {e}")
                    
            finally:
                print("Closing current connection")
                connection.close()
                
                
    def loadAndSend(self, connection, path):
        try:
            with open (path, "rb") as f:
                f.seek(0, os.SEEK_END)
                filesize = f.tell()
                f.seek(0, 0)
                
                if filesize > pow(2, 32):
                    raise Exception("file must be below 4GB")
            
                filename = os.path.basename(f.name)
                print("filename: ", filename, "filetype: ", MMP.checkFileType(filename))
                
                with open("../json/request.json", "r") as f2:
                    json_data = f2.read()
                    print(json_data)
                    json_len = len(json_data)
                
                header = MMP.makeHeader(json_len, len(MMP.checkFileType(filename)), filesize)
                print("Response Header: ", header, len(header))
                # ヘッダーの送信
                connection.sendall(header)
                print("ResponseFILENAME: ",filename)
                
                # bodyの送信
                converted_data = json_data.encode("utf-8") + MMP.checkFileType(filename).encode("utf-8") + f.read()
                connection.sendall(converted_data)
                
        finally:
            print("a")
    
    
    def deleteVideo(self, path):
        if os.path.exists(path):
            os.remove(path)      

               
        

def main():
    server = Server("0.0.0.0",  9001)
    server.start()
    
if __name__ == "__main__":
    main()