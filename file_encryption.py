import os
import sys
import hashlib
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Cryptodome.Cipher import AES
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


import secrets
import base64
import getpass

global filename


w = Tk()
w.title("File_encryption_and_decryption")
w.config(bg = "black")
w.geometry("500x500")


def openfile():
    filename = filedialog.askopenfilename(filetypes=(("text file","*.txt"),("all files","*.*"),))
    a2.insert(END,filename)




def encrypt():
    

    """
    #key = Fernet.generate_key()
    

    #with open('filekey.key', 'wb') as filekey:
     #   filekey.write(key)
    
    #with open('filekey.key', 'rb') as filekey:
     #   key = filekey.read()

     """
    
    try:
        b = a2.get()

        key = a5.get()
         
        fernet = Fernet(key)

    
        with open(b, 'rb') as file:
            original = file.read()
        
        encrypted = fernet.encrypt(original)
    
        with open(b, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        messagebox.showinfo("info","file Encrypt sucessfully")

    except Exception as e:
        #print(e)
        e = messagebox.showerror("info","already file Encrypt sucessfully")



def decrypt():

    try:
        h = a2.get()

        key = a5.get()

        fernet = Fernet(key)
        with open(h, 'rb') as enc_file:
            encrypted = enc_file.read()
    
        decrypted = fernet.decrypt(encrypted)
    

        with open(h, 'wb') as dec_file:
            dec_file.write(decrypted)

        messagebox.showinfo("info","file decrypt sucessfully")


    except Exception as e:
        print(e)
        e = messagebox.showerror("info","already file decrypt sucessfully")


def Reset(): 
    a2.delete(0,"end")
    a5.delete(0,"end")
    

def q():
    w.destroy()


a1 = Label(w,text = "Enter file path or click select file button",font = ("optima",12),fg="yellow",bg="black")
a1.place(x =5, y = 20)

a2 = Entry(w,font = ("optima",12))
a2.place(x = 5, y = 50,width=490,height=50)

a3 = Button(w,text = "Select file",command=openfile,bg="blue",activebackground="skyblue",font = ("optima",12,"bold"))
a3.place(x =5, y =120,width=490,height=50)

a4 = Label(w,text="Enter fernet Generating key..",font = ("optima",12),fg="yellow",bg="black")
a4.place(x=5,y=180)

a5 = Entry(w,font = ("optima",12))
a5.place(x = 5, y = 220,width=490,height=50)

a6 = Button(w,text = "Encryption",command = encrypt,bg="green",activebackground="green",font = ("optima",12,"bold"))
a6.place(x =5, y =280,width=240,height=50)

a7 = Button(w,text = "Decryption",command= decrypt,bg="red",activebackground="red",font = ("optima",12,"bold"))
a7.place(x =250, y =280,width=240,height=50)

a8 = Button(w,text="Reset",command=Reset,bg="gray",activebackground="gray",font = ("optima",12,"bold"))
a8.place(x=5,y=340,width=490,height=50)

a9 = Button(w,text="Quit",command = q,background="darkgray",activebackground="red",font = ("optima",12,"bold"))
a9.place(x=5,y=400,width=490,height=50)


w.mainloop()
