import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import os


root = tk.Tk()
root.title(u"Video Comprssor Service")
root.geometry("720x480")


def getMp4File():
    filename = filedialog.askopenfilename(title="mp4ファイルを選択", filetypes=[("MP4 files", "*.mp4")] , initialdir=os.getcwd())
    return filename

def on_combobox_selected(event):
    global radio, resolution_combobox
    selected_item = combobox.get()
    if selected_item == "圧縮":
        radio_label = ["high", "normal", "low"]
        radio_var = tk.IntVar()
        for i in range(len(radio_label)):
            radio = tk.Radiobutton(root, value=i, variable= radio_var, text=radio_label[i])
            radio.place(y = 180 + i * 20)        
        print("圧縮だな〜")
        
    elif selected_item == "解像度変更":
        pulldown_label = ["360p", "720p", "1080p", "WQHD", "4K", "custom"]
        resolution_combobox = ttk.Combobox(root, values=pulldown_label, state="readOnly")
        resolution_combobox.set("解像度を選択してください")
        resolution_combobox.place(x=300, y= 300)
        
        print("解像度変更するか〜")
    elif selected_item == "アスペクト比変更":
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


def on_window_resize(event):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    mid = width // 2
    print(width)
    
    if (width >= 600):
        file_label.place(x=width//4, y=10)
        Button.place(x=width//2+100, y=10)
        select_label.place(x=width//4, y=100)
        combobox.place(x=width//2+100, y=100)
        Convert.place(x=mid - 50, y=200)
        radio.place(x = mid)
    else:
        file_label.place(x=10,y=10)
        Button.place(x=10, y=30)
        select_label.place(x=10, y=100)
        combobox.place(x=10, y=120)
        Convert.place(x=mid - 50, y=200)
        radio.place(x = mid) 
        

def makeUI(root):
    global file_label, Button, select_label, combobox, Convert
    file_label = tk.Label(root, text="mp4ファイルを選択: ", font=("", 15))
    
    Button = tk.Button(root, text=u'選択', bg='skyblue', width=5)
    Button.bind("<Button-1>", getMp4File)
    
    select_label = tk.Label(root, text="圧縮方法選択: ", font=("", 15))
    
    module = ('圧縮', '解像度変更', 'アスペクト比変更', 'MP3変換', 'GIF作成', 'WEBM作成')
    combobox = ttk.Combobox(root, values=module, state='readonly')
    combobox.set("変換方法を選択してください")
    
    combobox.bind("<<ComboboxSelected>>", on_combobox_selected)
    
    Convert = tk.Button(root, text=u'変換', bg='skyblue', width=10)
    Convert.bind("<Button-1>", convertVideo)
    
    # ウィンドウのサイズ変更イベントをバインド
    root.bind("<Configure>", on_window_resize)
    
    
makeUI(root)
root.mainloop()