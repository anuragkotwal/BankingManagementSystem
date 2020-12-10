from create_bankacc_page import *
from Bank_login_page import *
from resources import *


def homepage(root):
    # Farmes
    MainFrame = Frame(root, height=WINDOWY, width=WINDOWX, bg=outerframecolor)
    MainFrame.place(x=0,y=0)
    InFrame = Canvas(MainFrame, height=WINDOWY-50, width=WINDOWX-50,bg=innerframecolor)
    InFrame.place(x=25,y=25)

    # Images
    root.bankimg = bankimg = PhotoImage(file=BANKUSER)
    InFrame.create_image((375, 130), image=bankimg, anchor=NW)
    Title = Label(MainFrame, text="Welcome to Our Bank", font='Jokerman', bg='#ffffff')
    Title.place(x=360,y=0)

    # Buttons
    Button(root, text="Create Account", font=('Jokerman', 15), width=20, command=lambda: create_acc(root), bg='#ffffff').place(x=325,y=300)
    Button(root, text="Login", font=('Jokerman', 15), width=20, command=lambda: login_acc(root), bg='#ffffff').place(x=325,y=370)