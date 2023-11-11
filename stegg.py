from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Steganography")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

# Define filename, text, and secret as global variables
filename = ""
text = None
secret = None

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File',
                                          filetype=(("PNG file", "*.png"), ("JPG File", "*.jpg"), ("All file", "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img

def Hide():
    global filename, secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)

def Show():
    global text, filename
    clear_message = lsb.reveal(filename)
    if text is None:
        text = Text(frame2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
        text.place(x=0, y=0, width=320, height=295)
        
        scrollbar1 = Scrollbar(frame2)
        scrollbar1.place(x=320, y=0, height=300)
        scrollbar1.configure(command=text.yview)
        text.configure(yscrollcommand=scrollbar1.set)

    text.delete(1.0, END)
    text.insert(END, clear_message)

def save():
    global secret
    if secret:
        secret.save("hidden.png")

image_icon = PhotoImage(file="download.png")
root.iconphoto(False, image_icon)

logo = PhotoImage(file="logo1.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

Label(root, text="STEGANOGRAPHY", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()
