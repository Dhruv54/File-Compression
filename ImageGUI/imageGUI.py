from pathlib import Path
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as tmsg
from tkinter import ttk
import os.path
from JPEG import *
import time

def upload_file():
    val=True
    global file
    while val:
        file=askopenfilename();
        file_extension =Path(file).suffix
        if(file_extension!=".jpeg" and file_extension!=".jpg"):
            val=tmsg.askretrycancel("ERROR!!!","SORRY !!! YOU CANNOT OPEN THIS FILE.PLEASE SELECT Image FILE(.jpg/.jpeg)")
            print(val)
        else:
            progress()
            val=False
            text_lbl4.pack()

def compress_img():
    try:
        file_extension =Path(file).suffix
        if(file_extension==".jpg" or file_extension==".jpeg"):
            compressfilestr=os.path.splitext(f"{file}")[0];
            canvas.pack()
            start_loading()
            canvas.pack_forget()
            exists = canvas.winfo_exists()
            if exists == 1:
                print("The widget exists.")
            else:
                print("The widget does not exist.")
            tmp=True
            print(file)
            JPEG(file)
            while tmp:
                if os.path.isfile(f"{compressfilestr}_compress.{file_extension}"):
                    print ("File Exist")
                    tmp=False

            tmsg.showinfo(title="SUCCESS",message='Image Compressed Successfully!!!')
            text_lbl4.pack_forget()
        else:
            tmsg.showinfo(title="ERROR!!!",message='Please Select Image file(.jpg/.jpeg) !!!')
    except:
        tmsg.showinfo(title="ERROR!!!",message='Please Select Image file(.jpg/.jpeg) !!!')

def progress():
    pb.pack(side=BOTTOM,fill=X)
    value_label.pack(pady=10)
    import time
    pb['value']=0
    while  pb['value'] < 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
        root.update_idletasks()
        time.sleep(0.5)
    tmsg.showinfo(title="DONE",message='File Uploaded Successfully!!!')
    destroy()

def update_progress_label():
    if pb['value']<100:
        return f"Current Progress: {pb['value']}%"
    else:
        return f"Uploaded Successfully"

def destroy():
    pb.pack_forget()
    value_label.pack_forget()

def start_loading():
    for i in range(0,3):
        for gif in giflist:
                canvas.delete(ALL)
                canvas.create_image(width/2.0, height/2.0, image=gif)
                canvas.update()
                time.sleep(0.1)



root=Tk()
root.title("Image Compression-Tkinter(Python)")
width=700
height=450
root.geometry(f"{width}x{height}")
root.minsize(width,height)
root.maxsize(width,height)
root.wm_iconbitmap("compress.ico")
root.config(background="#ffffff")
imagelist = ["dog001.gif","dog002.gif","dog003.gif","dog004.gif","dog005.gif","dog006.gif","dog007.gif"]

Header=Label(root,text="Image Compression",font="Sans-serif 22 bold",pady=20)
Header.pack(fill=X)


text_lbl1=Label(root,text="Choose Image file(.jpg/.jpeg)",font="Sans-serif 15 bold",pady=5)
text_lbl1.pack(fill=X)

text_lbl2=Label(root,text="Click here to upload file ↓",font="Sans-serif 10",pady=5,background="white")
text_lbl2.pack(fill=X)

button = Button(root, text="UPLOAD",font="Sans-serif 13 bold",command=upload_file,pady=5,height=2,width=20)
button.pack(pady=5)


pb = ttk.Progressbar(root,orient='horizontal',mode='determinate',length=280)
value_label = ttk.Label(root, text=update_progress_label(),background="#3AAFA9",font="Sans-serif 10 bold")

text_lbl3=Label(root,text="Click here to Compress file ↓",font="Sans-serif 10",pady=5,background="white")
text_lbl3.pack(fill=X)
text_lbl4=Label(root,text="Click Now ↑",font="Sans-serif 13 bold",pady=5,background="#3AAFA9")

button2 = Button(root, text="COMPRESS",font="Sans-serif 13 bold",command=compress_img,pady=5,height=2,width=20)
button2.pack(pady=5)


photo = PhotoImage(file=imagelist[0])
width = photo.width()
height = photo.height()
canvas = Canvas(width=width, height=height,background="white")

giflist = []
for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)


root.mainloop()