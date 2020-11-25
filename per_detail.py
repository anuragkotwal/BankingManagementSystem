from tkinter import *
from resources import *
import Bank_login_page

def personal_deatil(uname,root):
    #vars
    file = open(uname, 'r')
    f_data = file.read()
    details = f_data.split('\n')
    name = details[1]
    age = details[2]
    gen = details[3]
    email = details[4]
    bal = details[6]
    root.backicon = backicon = PhotoImage(file=BACK)
    detail_screen = Frame(root, height=500, width=900, bg=outerframecolor)
    detail_screen.place(x=0, y=0)
    Inframe = Canvas(detail_screen, height=WINDOWY - 50, width=WINDOWX - 50, bg=innerframecolor)
    Inframe.place(x=25, y=25)
    #Label
    Label(detail_screen, text="Personal Details" , font=('Courier New', 13), bg='#FFFFFF').place(x=370, y=0)
    Label(detail_screen, text="Name: "+name, font=('Courier New', 13)).place(x=80,y=100)
    Label(detail_screen, text="Age: "+age, font=('Courier New', 13)).place(x=80,y=140)
    Label(detail_screen, text="Gender: "+gen, font=('Courier New', 13)).place(x=80,y=180)
    Label(detail_screen, text="Email: " + email, font=('Courier New', 13)).place(x=80, y=220)
    Label(detail_screen, text="Current Balance: "+bal, font=('Courier New', 13)).place(x=80,y=260)

    # Buutons
    Button(detail_screen, command=lambda: Bank_login_page.login_confidential(root), image=backicon, bg='#000000').place(x=830, y=30)