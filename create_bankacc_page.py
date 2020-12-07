from tkinter import *
import os
from encrption import load_key
from cryptography.fernet import Fernet
from resources import *
import home_page
import tkinter.messagebox


def submit():

    # Vars
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    username = temp_username.get()
    password = temp_paswrd.get()
    email = temp_email.get()
    all_account = os.listdir()

    if name == "" or age == "" or gender == "" or username == "" or password == "":
        tkinter.messagebox.showerror(Bankname, "* All fields are Mandatory")
        return
    for acc in all_account:
        if username == acc:
            tkinter.messagebox.showerror(Bankname, "Account already Exists With the same Username")
            return
        else:
            # Inserting data in file
            key = load_key()
            f = Fernet(key)
            new_file = open(username, "w")
            # encrpting password
            encode_pass = password.encode()
            encrypt_pass = f.encrypt(encode_pass)
            new_file.write(str(encrypt_pass.decode()) + '\n')
            new_file.write(name + '\n')
            new_file.write(age + '\n')
            new_file.write(gender + '\n')
            new_file.write(email + '\n')
            new_file.write(username + '\n')
            new_file.write('0')
            new_file.close()
    tkinter.messagebox.showinfo(Bankname, "Account Created Successfully")

# Creating User Account
def create_acc(root):

    global temp_name
    global temp_age
    global temp_gender
    global temp_username
    global temp_paswrd
    global temp_email
    # Vars
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_username = StringVar()
    temp_paswrd = StringVar()
    temp_email = StringVar()

    # Frames
    create_screen = Frame(root,height=500,width=900,bg=outerframecolor)
    create_screen.place(x=0,y=0)
    Inframe = Canvas(create_screen, height=WINDOWY-50, width=WINDOWX-50,bg=innerframecolor)
    Inframe.place(x=25, y=25)

    #labels
    Label(create_screen, text="Account Opening", font=('Lucida Calligraphy', 20), bg='#00b7fa', fg='#ffffff',).place(x=360,y=30)
    Label(create_screen, text="*Name: ", font=('Lucida Calligraphy', 13), bg=innerframecolor).place(x=80,y=100)
    Label(create_screen, text="*Age: ", font=('Lucida Calligraphy', 13), bg=innerframecolor).place(x=80,y=140)
    Label(create_screen, text="*Gender: ", font=('Lucida Calligraphy', 13), bg=innerframecolor).place(x=80,y=180)
    Label(create_screen, text="*Email: ", font=('Lucida Calligraphy', 13), bg=innerframecolor).place(x=80, y=220)
    Label(create_screen, text="*Username: ", font=('Lucida Calligraphy', 13), bg=innerframecolor).place(x=80,y=260)
    Label(create_screen, text="*Password: ", font=('Lucida Calligraphy', 13), bg=innerframecolor).place(x=80,y=300)

    #Entries
    Entry(create_screen, textvariable=temp_name).place(x=210,y=103)
    Entry(create_screen, textvariable=temp_age).place(x=210,y=143)
    Entry(create_screen, textvariable=temp_gender).place(x=210,y=183)
    Entry(create_screen, textvariable=temp_email).place(x=210,y=223)
    Entry(create_screen, textvariable=temp_username).place(x=210,y=263)
    Entry(create_screen, textvariable=temp_paswrd, show="*").place(x=210,y=303)

    #buttons
    Button(create_screen, text="Submit", command=submit, font=('Lucida Calligraphy', 13), fg='#7d00b3', bg='#ffffff').place(x=420,y=350)
    Button(create_screen, text="Back To Home", command=lambda: home_page.homepage(root), font=('Lucida Calligraphy', 13), bg='#ffffff').place(x=390, y=400)

