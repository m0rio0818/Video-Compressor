import sys
import tkinter
from tkinter import filedialog
import os


root = tkinter.Tk()
root.title(u"Video Comprssor service")
root.geometry("720x480")


def findmp4File():
    filename = filedialog.askopenfilename(title="mp4ファイルを選択", filetypes=[("MP4 files", "*.mp4")] , initialdir=os.getcwd())
    print(filename)


def DeleteEntryValue(event):
    EditBox.delete(0, tkinter.END)
    

#エントリー
EditBox = tkinter.Entry(width=50)
EditBox.insert(tkinter.END,"挿入する文字列")
EditBox.place(x=5, y=10)

# ボタン
Button = tkinter.Button(text=u"ボタン", width=50)
Button.bind("<Button-1>", DeleteEntryValue)
Button.place(x=105, y=60)

findmp4File()

root.mainloop()