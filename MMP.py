import subprocess


class MMP:
    # def __init__(self, json, mediaType, payload) -> None:
    #     self.json = json
    #     self.mediaType = mediaType
    #     self.payload = payload
    
    @staticmethod
    def makeHeader(jsonSize, mediaTypeSize, payloadSize):
        return  jsonSize.to_bytes(16, "big") + mediaTypeSize.to_bytes(1, "big") + payloadSize.to_bytes(47, "big")
    
    # 動画を圧縮
    def compressionData(input_file, output_file):                #圧縮率(18~28)
        command = ["ffmpeg", "-i", input_file, "-c:v","libx264", "-crf", "23", "-c:a","aac", "-b:a", "128k", output_file]
        # "ffmpeg" "-i" "./temp/something.mp4" "-c:v libx264" "-crf 23" "-c:a aac" "-b:a 128k" "./temp/v.mp4"
        subprocess.call(command)
        return 
    
    # 動画の解像度を変更する
    def changeResolution(input, output):
        command = ["ffmpeg","-i", input,  "-vf", "scale=1280:720",  output]
        subprocess.call(command)
        return
    
    # 動画のアスペクト比を変更
    def changeAspect(self):
        command = []
        subprocess.call(command)
        return
    
    # 動画 to 音声
    def changeToMp3(self):
        command = []
        subprocess.call(command)
        return
    
    # 指定した時間範囲で GIF や WEBM を作成
    def makeGIForWEBM(self):
        command = []
        subprocess.call(command)
        return