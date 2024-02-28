import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
import os

class ViewContlloer:
    resolution_combobox = None
    optionArea = None
    combobox = None
    fileName = None
    file_label = None
    entryW = None
    x_label = None
    entryH = None
    
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(u"Video Comprssor Service")
        self.root.geometry("720x480")
        self.root.resizable(width=False, height=False)
        self.root.update_idletasks()
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        self.frame = tk.Frame(self.root, height=100, width=self.width, bg="blue")
        self.frame.place(x=0, y=140)

    def getMp4File(self, event):
        ViewContlloer.fileName = filedialog.askopenfilename(title="mp4ファイルを選択", filetypes=[("MP4 files", "*.mp4")] , initialdir=os.getcwd())
        if ViewContlloer.fileName != "":
            if hasattr(ViewContlloer, "file_label") and ViewContlloer.file_label is not None:
                ViewContlloer.file_label.destroy()
            ViewContlloer.file_label = tk.Label(self.root, text=ViewContlloer.fileName, font=("", 15))
            ViewContlloer.file_label.place(x=self.width//4, y = 45)        
        print("選択されたファイル: ",ViewContlloer.fileName)


    def only_numbers(self, char):
        return char.isdigit() and (len(char) <= 4 and len(char) > 0)
    
    def destroyCustomInput(self):
        ViewContlloer.entryH.destroy()
        ViewContlloer.entryW.destroy()
        ViewContlloer.x_label.destroy()
        

    def makeCustomInput(self):
        validate_numeeric = self.root.register(self.only_numbers)
        ViewContlloer.entryW = tk.Entry(self.frame, validate="key", validatecommand=(validate_numeeric, '%S'), width=10)
        ViewContlloer.entryW.place(x=self.width//2-150, y=40)
        ViewContlloer.x_label = tk.Label(self.frame, text="x", font=("", 15))
        ViewContlloer.x_label.place(x=self.width//2, y=40)
        ViewContlloer.entryH = tk.Entry(self.frame, validate="key", validatecommand=(validate_numeeric, '%S'), width=10)
        ViewContlloer.entryH.place(x=self.width//2+50, y=40)
        
    def on_resolution_change(self, event):
        selected_item = ViewContlloer.resolution_combobox.get()
        if selected_item == "custom":
            print("カスタム入力")
            self.makeCustomInput()
        else:
            print("解像度は以下に変更します", selected_item)
            self.destroyCustomInput()
            
    def on_combobox_selected(self, event):
        print("選択されたファイル:" , ViewContlloer.fileName)
        if ViewContlloer.fileName == None:
            messagebox.showinfo("mp4ファイル選択", "MP4ファイルを選択してください")
            ViewContlloer.combobox.set("変換方法を選択してください")
            return

        selected_item = ViewContlloer.combobox.get()
        print(selected_item,"が選択されました。")
        self.clearAllElement()
        self.makeFrameArea(selected_item)
        
            
    def convertVideo(self, event):
        print("変換ボタンが押されました")
    
    def clearAllElement(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root, height=100, width=self.width,)
        self.frame.place(x=0, y=140)    
    
    def makeFrameArea(self, type):
        if type == "圧縮":
            radio_label = ["high", "normal", "low"]
            radio_var = tk.IntVar()
            for i in range(len(radio_label)):
                radio = tk.Radiobutton(self.frame, value=i, variable= radio_var, text=radio_label[i])
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
