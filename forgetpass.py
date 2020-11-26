from tkinter import *
from resources import *
import os
import tkinter.messagebox
from encrption import *
import smtplib
import Bank_login_page

# Function sending mail
def sendemail(email, passwrd):
    rec_email = email
    msg = passwrd
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(senderemail, password)
    server.sendmail(senderemail, rec_email, msg)
    server.close()
    tkinter.messagebox.showinfo(Bankname, "Password is Successfully send to Your Registered Email id (Also Check Spam)")

def verifing():
    all_acc = os.listdir()
    username = forgetuser_name.get()
    key = load_key()
    f = Fernet(key)
    for name in all_acc:
        if username == "":
            tkinter.messagebox.showerror(Bankname, "* All fields are Mandatory")
            return
        if username == name:
            file = open(name, "r")
            f_data = file.read()
            f_data = f_data.split('\n')
            email = f_data[4]
            dec_msg = f.decrypt(f_data[0].encode())
            n_file = dec_msg.decode()
            passwrd = n_file
            sendemail(email, passwrd)
            return
    tkinter.messagebox.showerror(Bankname, "Account Not found with this Username!!!")


def forgetpass(root):
    global forgetuser_name

    # Vars
    forgetuser_name = StringVar()
    forget_screen = Frame(root, height=500, width=900, bg=outerframecolor)
    forget_screen.place(x=0, y=0)
    Inframe = Canvas(forget_screen, height=WINDOWY - 50, width=WINDOWX - 50, bg=innerframecolor)
    Inframe.place(x=25, y=25)

    # labels
    Label(forget_screen, text="Enter Your Username", font=('Forte', 15), bg=innerframecolor).place(x=200, y=100)

    # Entry
    Entry(forget_screen, textvariable=forgetuser_name).place(x=480, y=105)

    # Button
    Button(forget_screen, text='Next', command=verifing).place(x=500, y=140)
    Button(forget_screen, text="Back To Login Page", command=lambda: Bank_login_page.login_acc(root), font=('Forte', 13),
           bg='#ffffff').place(x=375, y=390)