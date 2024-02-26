import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import os

class ViewContlloer:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title(u"Video Comprssor Service")
        self.root.geometry("720x480")
        self.root.resizable(width=False, height=False)
        self.root.update_idletasks()
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        print(self.width, " x ", self.height)

    def getMp4File(self, event):
        global filename
        filename = filedialog.askopenfilename(title="mp4ファイルを選択", filetypes=[("MP4 files", "*.mp4")] , initialdir=os.getcwd())
        print(filename)
        return filename

    def only_numbers(self, char):
        return char.isdigit() and (len(char) <= 4 and len(char) > 0)

    def makeCustomInput(self):
        validate_numeeric = self.root.register(self.sonly_numbers)
        entryW = tk.Entry(self.root, validate="key", validatecommand=(validate_numeeric, '%S'), width=10)
        entryW.place(x=250, y=200)
        x_label = tk.Label(self.root, text="x", font=("", 15))
        x_label.place(x=370, y=200)
        entryH = tk.Entry(self.root, validate="key", validatecommand=(validate_numeeric, '%S'), width=10)
        entryH.place(x=400, y=200)
        
    def on_resolution_change(self, event):
        selected_item = resolution_combobox.get()
        if selected_item == "custom":
            print("カスタム入力")
            self.makeCustomInput()
        else:
            print("解像度は以下に変更します", selected_item)
    def on_combobox_selected(self, sevent):
        try:
            print(filename)
        except NameError:
            print("ファイル名は定義されていません")
            
        global resolution_combobox
        selected_item = combobox.get()
        if selected_item == "圧縮":
            radio_label = ["high", "normal", "low"]
            radio_var = tk.IntVar()
            for i in range(len(radio_label)):
                radio = tk.Radiobutton(self.root, value=i, variable= radio_var, text=radio_label[i])
                radio.place(x = mid, y = 180 + i * 20)
                print("圧縮だな〜")
            
        elif selected_item == "解像度変更":
            pulldown_label = ["360p", "720p", "1080p", "WQHD", "4K", "custom"]
            resolution_combobox = ttk.Combobox(self.root, values=pulldown_label, state="readOnly")
            resolution_combobox.set("解像度を選択してください")
            resolution_combobox.place(x=300, y= 150)
            resolution_combobox.bind("<<ComboboxSelected>>", self.on_resolution_change)
            
            print("解像度変更するか〜")
        elif selected_item == "アスペクト比変更":
            self.makeCustomInput()
            
            print("アスペクト比変更しようかな〜")
        elif selected_item == "MP3変換":
            print("MP3変換しちゃう")
        elif selected_item == "GIF作成":
            print("GIF作成するを")
        elif selected_item == "WEBM作成":
            print("WEBMを作成しま〜す!!")
            
    def convertVideo():
        print("変換ボタンが押されました")
        pass
    
    # def on_window_resize(event):
    #     global width, height, mid
    #     self.root.update_idletasks()
    #     width = self.root.winfo_width()
    #     height = self.root.winfo_height()
    #     mid = width // 2
        
    #     if (width >= 600):
    #         file_label.place(x=width//4, y=10)
    #         Button.place(x=width//2+100, y=10)
    #         select_label.place(x=width//4, y=100)
    #         combobox.place(x=width//2+100, y=100)
    #         Convert.place(x=mid - 50, y=300)
    #         # radio.place(x = mid)

            
    def makeUI(self):
        file_label = tk.Label(self.root, text="mp4ファイルを選択: ", font=("", 15))
        file_label.place(x=self.width//4, y = 10)
        
        Button = tk.Button(self.root, text=u'選択', bg='skyblue', width=5)
        Button.bind("<Button-1>", self.getMp4File)
        Button.place(x=self.width // 2 + 100, y = 10)
        
        select_label = tk.Label(self.root, text="圧縮方法選択: ", font=("", 15))
        select_label.place(x=self.width//4, y = 100)
        
        module = ('圧縮', '解像度変更', 'アスペクト比変更', 'MP3変換', 'GIF作成', 'WEBM作成')
        combobox = ttk.Combobox(self.root, values=module, state='readonly')
        combobox.set("変換方法を選択してください")
        combobox.place(x=self.width//2 + 100, y = 100)
        
        combobox.bind("<<ComboboxSelected>>", self.on_combobox_selected)
        
        Convert = tk.Button(self.root, text=u'変換', bg='skyblue', width=10)
        Convert.bind("<Button-1>", self.convertVideo)
        Convert.place(x=self.width//2 - 50, y = 300)
        
        # # ウィンドウのサイズ変更イベントをバインド
        # root.bind("<Configure>", on_window_resize)
        
        self.root.mainloop()


contlloer = ViewContlloer()
contlloer.makeUI()
