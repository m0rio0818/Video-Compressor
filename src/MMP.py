import subprocess


class MMP:  
    @staticmethod
    def makeHeader(jsonSize, mediaTypeSize, payloadSize):
        return  jsonSize.to_bytes(16, "big") + mediaTypeSize.to_bytes(1, "big") + payloadSize.to_bytes(47, "big")

    def checkFileType(filename):
        return filename[filename.find(".")+1:]     

    # 動画を圧縮
    def compressionData(input_file, output_file, custom):
        #　圧縮率(18~28)          
        if custom == "high":
            rate = "18"
        elif custom == "normal":
            rate = "23"
        elif custom == "low":
            rate = "28"
        else:
            rate = "23"
        
        print("圧縮効率: ",rate, "ファイル出力先", output_file)               
        command = ["ffmpeg", "-i", input_file, "-c:v","libx264", "-crf", rate, "-c:a","aac", "-b:a", "128k", output_file]
        subprocess.call(command)
        return 
    
    # 動画の解像度を変更する
    def changeResolution(input, output, option,  params):
        print(option, params)
        if option == "custom":
            width = params[0]
            height = params[1]
            print("Width: ",width, "Height: ", height)
            if (height == None or height == 0): 
                command = ["ffmpeg","-i", input,  "-s", "scale=-1:{}".format(width),   output]
            elif (width == None or width == 0):
                command = ["ffmpeg","-i", input,  "-s", "scale={}:-1".format(height),  output]
            else:
                command = ["ffmpeg","-i", input,  "-vf", "scale={}:{}".format(width, height), output]
            subprocess.call(command)
        else:
            print("今から変換を始めます。！！！！", option, output)
            if (option == "360p"):
                command = ["ffmpeg","-i", input,  "-vf", "scale=480:320", "-c:a", "copy", output]
                print("360p")
            elif (option == "720p"):
                command = ["ffmpeg","-i", input,  "-vf", "scale=1280:720", "-c:a", "copy", output]
                print("720p")
            elif (option == "1080p"):
                command = ["ffmpeg","-i", input,  "-vf", "scale=1920:1080","-c:a", "copy", output]
                print("1080p")
            elif (option == "WQHD"):
                command = ["ffmpeg","-i", input,  "-vf", "scale=2048:1152", "-c:a", "copy",output]
                print("WQHD")
            elif (option == "4K"):
                command = ["ffmpeg","-i", input,  "-vf", "scale=3840:2160","-c:a", "copy", output]
                print("4K")
            else:
                return
            subprocess.call(command)
    
    # 動画のアスペクト比を変更
    def changeAspect(input, output, params):
        width = int(params[0])
        height = int(params[1])
        print("HEIGHT: ",width, type(width),"HEIGHT", height, type(height))
        if (height == None or width == None or height <= 0 or width <= 0): 
            command = ["ffmpeg","-y", "-i",  input,  "-c", "copy", "--aspect -1:-1",  output]
        else:
            command = ["ffmpeg", "-y", "-i", input,  "-c", "copy", "--aspect {}:{}".format(width, height),  output]
        subprocess.call(command)
        return
    
    # 動画 to 音声
    def changeToMp3(input, output, quality):
        print("QUALITY : ",quality)
        quality_mp3 = "4"
        if (quality == "high"):
            quality_mp3 = "0"
        elif (quality == "normal"):
            quality_mp3 = "4"
        elif (quality == "low"):
            quality_mp3 = "9"
        command = ["ffmpeg", "-i", input, "-vn", "-acodec", "libmp3lame", "-q:a" , quality_mp3, output,]
        subprocess.call(command)
        print("進行度")
        return
    
    # 指定した時間範囲で GIF や WEBM を作成
    def makeGIForWEBM(input, output, type):
        print("TYPE : ",type, "=>", input, "output:", output, "{}.{}".format(output,type))
        command = []
        if (type == "webm"):
            command = ["ffmpeg", "-i", input, "-c:v", "libvpx", "-b:v", "1M" ,"-c:a", "libvorbis", output]
        elif (type == "gif"):
            command = ["ffmpeg", "-i" ,input, "-vf", "fps=10,scale=320:-1:flags=lanczos", "-c:v", "gif",  output]
        subprocess.call(command)
        print(command)
        return