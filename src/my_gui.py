import sys
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

def on_combobox_selected(event, combobox):
    selected_item = combobox.get()
    if selected_item == "圧縮":
        print("圧縮だな〜")
    elif selected_item == "解像度変更":
        print("解像度変更するか〜")
    elif selected_item == "アスペクト比変更":
        print("アスペクト比変更しようかな〜")
    elif selected_item == "MP3変換":
        print("MP3変換しちゃう")
    elif selected_item == "GIF作成":
        print("GIF作成するを")
    elif selected_item == "WEBM作成":
        print("WEBMを作成しま〜す!!")

def makeUI(root):
    label = tk.Label(root, text="mp4ファイルを選択: ", font=("", 15))
    label.place(x=120, y=10)
    
    Button = tk.Button(root, text=u'選択', bg='skyblue', width=5)
    Button.bind("<Button-1>", getMp4File)
    Button.place(x=500, y=10)
    
    label = tk.Label(root, text="圧縮方法選択: ", font=("", 15))
    label.place(x=120, y=100)
    
    module = ('圧縮', '解像度変更', 'アスペクト比変更', 'MP3変換', 'GIF作成', 'WEBM作成')
    combobox = ttk.Combobox(root, values=module, state='readonly')
    combobox.set("変換方法を選択してください")
    combobox.place(x=350, y=100)
    
    combobox.bind("<<ComboboxSelected>>", lambda event, combobox = combobox : on_combobox_selected(event, combobox))
    
    
makeUI(root)
root.mainloop()