import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from client import Client
from make_json import makeRequest_JsonFile

class ViewContlloer:
    resolution_combobox = None
    combobox = None
    
    filePath = None
    convertionMethod = None
    selected_item = None
    
    selected_radio = None
    entryW = None
    entryH = None

    file_label = None
    
    method_Converter = {
        "圧縮": "compression",
        "解像度変更" : "resolution",
        "アスペクト比変更" : "aspect",
        "MP3変換": "mp3",
        "GIF作成" : "gif",
        "WEBM作成": "webm"
    }
    
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(u"Video Comprssor Service")
        self.root.geometry("720x480")
        self.root.resizable(width=False, height=False)
        self.root.update_idletasks()
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        self.frame = tk.Frame(self.root, height=100, width=self.width)
        self.frame.place(x=0, y=140)
        self.client = Client("0.0.0.0", "0.0.0.0", 9050, 9001)

    def getMp4File(self, event):
        ViewContlloer.filePath = filedialog.askopenfilename(title="mp4ファイルを選択", filetypes=[("MP4 files", "*.mp4")] , initialdir=os.getcwd())
        if ViewContlloer.filePath != "":
            if hasattr(ViewContlloer, "file_label") and ViewContlloer.file_label is not None:
                ViewContlloer.file_label.destroy()
            ViewContlloer.file_label = tk.Label(self.root, text=ViewContlloer.filePath, font=("", 15))
            ViewContlloer.file_label.place(x=self.width//4, y = 45)        
        print("選択されたファイル: ", ViewContlloer.filePath)
        

    def makeCustomInput(self):
        validate_numeric = self.frame.register(self.only_numbers)
        ViewContlloer.entryW = tk.Entry(self.frame, validate="key", validatecommand=(validate_numeric, '%S'), width=10)
        ViewContlloer.entryW.place(x=self.width//2-150, y=40)
        
        x_label = tk.Label(self.frame, text="x", font=("", 15))
        x_label.place(x=self.width//2, y=40)
        
        ViewContlloer.entryH = tk.Entry(self.frame, validate="key", validatecommand=(validate_numeric, '%S'), width=10)
        ViewContlloer.entryH.place(x=self.width//2+50, y=40)
        
    def on_resolution_change(self, event):
        ViewContlloer.selected_item = ViewContlloer.resolution_combobox.get()
        if ViewContlloer.selected_item == "custom":
            print("カスタム入力")
            self.makeCustomInput()
        else:
            print("解像度は以下に変更します", ViewContlloer.selected_item)
            
    def on_combobox_selected(self, event):
        print("選択されたファイル:" , ViewContlloer.filePath)
        if ViewContlloer.filePath == None:
            messagebox.showinfo("mp4ファイル選択", "MP4ファイルを選択してください")
            ViewContlloer.combobox.set("変換方法を選択してください")
            return

        selected_item = ViewContlloer.combobox.get()
        self.clearAllElement()
        self.makeFrameArea(selected_item)
        ViewContlloer.convertionMethod = selected_item
        print(ViewContlloer.convertionMethod, "が選択されました。")
        
            
    def convertVideo(self, event):
        if ViewContlloer.filePath == None:
            messagebox.showinfo("mp4ファイル選択", "MP4ファイルを選択してください")
        elif ViewContlloer.convertionMethod == None:
            messagebox.showinfo("変換方法選択", "変換方法を選択してください")
        else:
            method = ViewContlloer.method_Converter[ViewContlloer.convertionMethod]
            # 変換方法確認
            print("最終変換方法=> ",ViewContlloer.convertionMethod, " : ", method)
            if ViewContlloer.convertionMethod == "圧縮":
                print(ViewContlloer.selected_radio)
                if ViewContlloer.selected_radio == None:
                    messagebox.showinfo("圧縮方法選択", "圧縮方法が選択されていません")
                    return
                else:
                    print("圧縮で決定: ", ViewContlloer.selected_radio)
                    makeRequest_JsonFile(ViewContlloer.filePath, method, ViewContlloer.selected_radio, "mp4")
                    self.client.start()                    
                    
            elif ViewContlloer.convertionMethod == "解像度変更":
                if ViewContlloer.selected_item == None:
                    messagebox.showinfo("解像度選択", "解像度が選択されていません")
                elif ViewContlloer.selected_item == "custom":
                    print(ViewContlloer.entryH, ViewContlloer.entryW)
                    width = ViewContlloer.entryW.get()
                    height = ViewContlloer.entryH.get()                    
                    if width == "" or height == "":
                        messagebox.showinfo("カスタム入力不適切", "カスタム入力が正しくされていません")
                        return
                    else:
                        print(width, " * " , height)
                        makeRequest_JsonFile(ViewContlloer.filePath, method, ViewContlloer.selected_item, "mp4", [width, height]) 
                        self.client.start()        
                else:
                    print("解像度選択で決定", ViewContlloer.selected_item)
                    makeRequest_JsonFile(ViewContlloer.filePath, method, ViewContlloer.selected_item, "mp4") 
                    self.client.start()        
                    
            elif ViewContlloer.convertionMethod == "アスペクト比変更":
                width = ViewContlloer.entryW.get()
                height = ViewContlloer.entryH.get()                    
                if width == "" or height == "":
                    messagebox.showinfo("カスタム入力不適切", "カスタム入力が正しくされていません")
                    return
                else:
                    print("アスペクト比変更で決定", width, " * " , height)
                    makeRequest_JsonFile(ViewContlloer.filePath, method, None, "mp4", [width, height])
                    self.client.start()        
                    
            elif ViewContlloer.convertionMethod == "MP3変換":
                makeRequest_JsonFile(ViewContlloer.filePath, method, ViewContlloer.selected_radio, "mp3", None,)
                self.client.start() 
                print("MP3変換で決定")
                
            elif ViewContlloer.convertionMethod == "GIF作成":
                print("GIF作成で決定")
            elif ViewContlloer.convertionMethod == "WEBM作成":
                print("WEBM作成で決定")
    
    def clearAllElement(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root, height=100, width=self.width,)
        self.frame.place(x=0, y=140)
        ViewContlloer.convertionMethod = None
        ViewContlloer.selected_radio = None
        ViewContlloer.entryW = None
        ViewContlloer.entryH = None
        
    def only_numbers(self, char):
        return char.isdigit() and (len(char) <= 4 and len(char) > 0)
    
    # def destroyCustomInput(self):
    #     ViewContlloer.entryH.destroy()
    #     ViewContlloer.entryW.destroy()
    #     ViewContlloer.x_label.destroy()

    def on_radio_selected(self, radio_var):
        ViewContlloer.selected_radio = radio_var.get()
        print("選択されたラジオ値: ", ViewContlloer.selected_radio)
        return

    def makeFrameArea(self, type):
        if type == "圧縮":
            radio_label = ["high", "normal", "low"]
            radio_var = tk.StringVar(value=None)
            for i in range(len(radio_label)):
                radio = tk.Radiobutton(self.frame, value=radio_label[i], variable=radio_var, text=radio_label[i], command=lambda: self.on_radio_selected(radio_var))
                radio.place(x = self.width/2, y = i * 20)

            print("圧縮だな〜")
            
        elif type == "解像度変更":
            pulldown_label = ["360p", "720p", "1080p", "WQHD", "4K", "custom"]
            ViewContlloer.resolution_combobox = ttk.Combobox(self.frame, values=pulldown_label, state="readOnly")
            ViewContlloer.resolution_combobox.set("解像度を選択してください")
            ViewContlloer.resolution_combobox.place(x=280, y= 0)
            ViewContlloer.resolution_combobox.bind("<<ComboboxSelected>>", self.on_resolution_change)
            print("解像度変更するか〜")
        
        elif type == "アスペクト比変更":
            self.makeCustomInput()
            print("アスペクト比変更しようかな〜")
            
        elif type == "MP3変換":
            radio_label = ["high", "normal", "low"]
            radio_var = tk.StringVar(value=None)
            for i in range(len(radio_label)):
                radio = tk.Radiobutton(self.frame, value=radio_label[i], variable=radio_var, text=radio_label[i], command=lambda: self.on_radio_selected(radio_var))
                radio.place(x = self.width/2, y = i * 20)
            print("MP3変換しちゃう")
            
        elif type == "GIF作成":
            print("GIF作成するを")
        
        elif type == "WEBM作成":
            print("WEBMを作成しま〜す!!")

            
            
    def makeUI(self):
        file_label = tk.Label(self.root, text="mp4ファイルを選択: ", font=("", 15))
        file_label.place(x=self.width//4, y = 10)
        
        Button = tk.Button(self.root, text=u'選択', bg='skyblue', width=5)
        Button.bind("<Button-1>", self.getMp4File)
        Button.place(x=self.width // 2 + 100, y = 10)
                
        select_label = tk.Label(self.root, text="変換方法: ", font=("", 15))
        select_label.place(x=self.width//4, y = 100)
        
        module = ('圧縮', '解像度変更', 'アスペクト比変更', 'MP3変換', 'GIF作成', 'WEBM作成')
        ViewContlloer.combobox = ttk.Combobox(self.root, values=module, state='readonly')
        ViewContlloer.combobox.set("変換方法を選択してください")
        ViewContlloer.combobox.place(x=self.width//2 + 100, y = 100)
        ViewContlloer.combobox.bind("<<ComboboxSelected>>", self.on_combobox_selected)
        
        Convert = tk.Button(self.root, text=u'変換', bg='skyblue', width=10)
        Convert.bind("<Button-1>", self.convertVideo)
        Convert.place(x=self.width//2 - 50 , y = 250)
               
        self.root.mainloop()


contlloer = ViewContlloer()
contlloer.makeUI()
