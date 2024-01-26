import subprocess


class MMP:  
    @staticmethod
    def makeHeader(jsonSize, mediaTypeSize, payloadSize):
        return  jsonSize.to_bytes(16, "big") + mediaTypeSize.to_bytes(1, "big") + payloadSize.to_bytes(47, "big")

    def checkFileType(filename):
        return filename[filename.find(".")+1:]     

    # 動画を圧縮
    def compressionData(input_file, output_file,):                #圧縮率(18~28)
        command = ["ffmpeg", "-i", input_file, "-c:v","libx264", "-crf", "23", "-c:a","aac", "-b:a", "128k", output_file]
        # "ffmpeg" "-i" "./temp/something.mp4" "-c:v libx264" "-crf 23" "-c:a aac" "-b:a 128k" "./temp/v.mp4"
        subprocess.call(command)
        return 
    
    # 動画の解像度を変更する
    def changeResolution(input, output, width= None, height = None):
        print("HEIGHT: ",width, "HEIGHT", height)
        if (height == None or height == 0): 
            command = ["ffmpeg","-i", input,  "-s", "scale=-1:{}".format(width),   "{}.{}".format(output, "mp4")]
        elif (width == None or width == 0):
            command = ["ffmpeg","-i", input,  "-s", "scale={}:-1".format(height),  "{}.{}".format(output, "mp4")]
        else:
            command = ["ffmpeg","-i", input,  "-vf", "scale={}:{}".format(width, height),   "{}.{}".format(output, "mp4")]
        subprocess.call(command)
        return
    
    # 動画のアスペクト比を変更
    def changeAspect(input, output, width, height):
        print("HEIGHT: ",width, "HEIGHT", height)
        if (height == None or height <= 0 or width == None or width <= 0): 
            command = ["ffmpeg","-i", input,  "-vf", "setsar=-1:-1",  output]
        else:
            command = ["ffmpeg","-i", input,  "-vf", "setsar={}:{}".format(width, height),   "{}.{}".format(output, "mp4")]
        subprocess.call(command)
        return
    
    # 動画 to 音声
    def changeToMp3(input, output, quality):
        print("QUALITY : ",quality)
        quality_mp3 = "4"
        if (quality == "hight"):
            quality_mp3 = "0"
        elif (quality == "normal"):
            quality_mp3 = "4"
        elif (quality == "low"):
            quality_mp3 = "9"
        command = ["ffmpeg", "-i", input, "-vn", "-acodec", "libmp3lame", "-q:a" , quality_mp3, "{}.{}".format(output, "mp3")]
        subprocess.call(command)
        return
    
    # 指定した時間範囲で GIF や WEBM を作成
    def makeGIForWEBM(input, output, type):
        print("TYPE : ",type, "=>", input, "output:", output, "{}.{}".format(output,type))
        command = []
        if (type == "webm"):
            command = ["ffmpeg", "-i", input, "-c:v", "libvpx", "-b:v", "1M" ,"-c:a", "libvorbis", "{}.{}".format(output, type)]
        elif (type == "gif"):
            command = ["ffmpeg", "-i" ,input, "-vf", "fps=10,scale=320:-1:flags=lanczos", "-c:v", "gif",  "{}.{}".format(output, type)]
        subprocess.call(command)
        print(command)
        return