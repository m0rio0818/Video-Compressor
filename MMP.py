import subprocess


class MMP:
    # def __init__(self, json, mediaType, payload) -> None:
    #     self.json = json
    #     self.mediaType = mediaType
    #     self.payload = payload
    
    def makeHeader(self, jsonSize, mediaTypeSize, payloadSize):
        return  jsonSize.to_bytes(16, "big") + mediaTypeSize.to_bytes(1, "big") + payloadSize.to_bytes(47, "big")
    
    # 動画を圧縮
    def compressionData(self, input, output):                #圧縮率(18~28)
        command = ["ffmpeg","-i", input, "-c:v libx264", "-crf", "23", "-c:a aac", "-b:a 128k", output]
        return 
    
    # 動画の解像度を変更する
    def changeResolution(self, input, output):
        command = ["ffmpeg","-i", input,  "-vf", "scale=1280:720",  output]
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