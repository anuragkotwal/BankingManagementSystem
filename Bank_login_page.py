from tkinter import *
import os
from encrption import *
from cryptography.fernet import Fernet
import per_detail as p
import deposit as d
import withdraw as w
from resources import *
import tkinter.messagebox
import home_page
import forgetpass


# Login confidential function
def login_confidential(root):

    # Vars
    all_acc = os.listdir()
    uname = login_name.get()
    passcode = login_pass.get()
    key = load_key()
    f = Fernet(key)
    for name in all_acc:
        if passcode == "" or uname == "":
            tkinter.messagebox.showerror(Bankname, "* All fields are Mandatory")
            return
        if uname == name:
            file = open(name, "r")
            f_data = file.read()
            f_data = f_data.split('\n')

            # Decrypting Password
            dec_msg = f.decrypt(f_data[0].encode())
            n_file = dec_msg.decode()
            paswrd = n_file

            # Account Dashboard
            if passcode == paswrd:
                # Frames
                dash_screen = Frame(root, height=500, width=900, bg=outerframecolor)
                dash_screen.place(x=0, y=0)
                Inframe = Canvas(dash_screen, height=WINDOWY - 50, width=WINDOWX - 50, bg=innerframecolor)
                Inframe.place(x=25, y=25)

                # labels
                Label(dash_screen, text="Account Dashboard", font=('Lucida Calligraphy', 13)).place(x=370, y=0)
                Label(dash_screen, text="Welcome " + f_data[1], font=('Lucida Calligraphy', 18, 'bold'), ).place(x=345, y=30)

                # Buttons
                Button(dash_screen, text="Personal Details", font=('Lucida Calligraphy', 13), width=20,
                       command=lambda: p.personal_deatil(uname, root), bg='#FFFFFF').place(x=340, y=100)
                Button(dash_screen, text="Deposit", font=('Lucida Calligraphy', 13), width=20,
                       command=lambda: d.deposit(uname, root), bg='#FFFFFF').place(x=340, y=150)
                Button(dash_screen, text="Withdraw", font=('Lucida Calligraphy', 13), width=20,
                       command=lambda: w.withdraw(uname, root), bg='#FFFFFF').place(x=340, y=200)
                Button(dash_screen, text="Logout", command=lambda: login_acc(root), font=('Lucida Calligraphy', 13),
                       bg='#ffffff').place(x=340, y=240)
                return
            else:
                tkinter.messagebox.showerror(Bankname, "Password is wrong!!!")
                return
    tkinter.messagebox.showerror(Bankname, "Account Not found with this Username!!!")

# Login in Account
def login_acc(root):

    global login_name
    global login_pass
    global login_screen
    # Vars
    login_name = StringVar()
    login_pass = StringVar()
    # Frames
    login_screen = Frame(root, height=500, width=900, bg=outerframecolor)
    login_screen.place(x=0, y=0)
    Inframe = Canvas(login_screen, height=WINDOWY - 50, width=WINDOWX - 50, bg=innerframecolor)
    Inframe.place(x=25, y=25)

    # Images
    root.logimg = logimg = PhotoImage(file=LOGINICON)
    root.usericon = usericon = PhotoImage(file=USERICON)
    Inframe.create_image((450, 20), image=usericon, anchor=N)

    # label
    Label(login_screen, text="Login Menu", font=('Lucida Calligraphy', 20), bg='#000000', fg='#FFFFFF').place(x=370, y=0)
    Label(login_screen, text="Username", font=('Lucida Calligraphy', 15), bg=innerframecolor).place(x=410, y=160)
    Label(login_screen, text="Password", font=('Lucida Calligraphy', 15), bg=innerframecolor).place(x=410, y=230)

    # Entries
    Entry(login_screen, textvariable=login_name).place(x=405, y=190)
    Entry(login_screen, textvariable=login_pass, show="*").place(x=405, y=260)

    # Buttons
    Button(login_screen, command=lambda: login_confidential(root), image=logimg).place(x=440, y=300)
    Button(login_screen, text='Forget Password', font=('Lucida Calligraphy', 8, 'underline'), bg=innerframecolor,
           fg='blue', command=lambda: forgetpass.forgetpass(root)).place(x=415, y=360)
    Button(login_screen, text="Back To Home", command=lambda: home_page.homepage(root), font=('Lucida Calligraphy', 13),
           bg='#ffffff').place(x=395, y=390)
