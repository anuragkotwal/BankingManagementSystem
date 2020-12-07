from tkinter import *
from resources import *
import tkinter.messagebox
import Bank_login_page


def With_amount(username):
    if amount_with.get() == "":
        tkinter.messagebox.showerror(Bankname, "Please Enter Amount")
        return
    if float(amount_with.get()) <= 0:
        tkinter.messagebox.showerror(Bankname, "Account Either have zero Balance or Negative Balance")
        return
    file_obj = open(username, 'r+')
    file_data = file_obj.read()
    data = file_data.split('\n')
    curr_bal = data[6]
    if float(amount_with.get()) > float(curr_bal):
        tkinter.messagebox.showerror(Bankname, "Insufficient Balance")
        return
    update_bal = curr_bal
    update_bal = float(update_bal) - float(amount_with.get())
    data[6] = str(update_bal)
    file_obj.seek(0)
    file_obj.truncate(0)
    file_obj.write("\n".join(data))
    file_obj.close()
    tkinter.messagebox.showinfo(Bankname, "Amount debit from your account & Current Balance is: " + str(update_bal))


# WithDraw Function
def withdraw(uname, root):

    global amount_with
    global curr_bal
    # Back Button Icon
    root.backicon = backicon = PhotoImage(file=BACK)

    amount_with = StringVar()
    file_obj = open(uname, "r")
    file_obj_data = file_obj.read()
    user_details = file_obj_data.split('\n')
    bal = user_details[6]
    # Frames
    Withdraw_screen = Frame(root, height=500, width=900, bg=outerframecolor)
    Withdraw_screen.place(x=0, y=0)
    Inframe = Canvas(Withdraw_screen, height=WINDOWY - 50, width=WINDOWX - 50, bg=innerframecolor)
    Inframe.place(x=25, y=25)

    # Labels
    Label(Withdraw_screen, text="Withdraw Menu", font=('Lucida Calligraphy', 13)).place(x=385, y=0)
    curr_bal_label = Label(Withdraw_screen, text="Current Balance: " + bal, font=('Lucida Calligraphy', 13))
    curr_bal_label.place(x=80, y=100)
    Label(Withdraw_screen, text="Enter Amount to Withdraw = ", font=('Lucida Calligraphy', 13), bg=innerframecolor).place(x=80,
                                                                                                                   y=140)

    # Entries
    Entry(Withdraw_screen, textvariable=amount_with).place(x=370, y=143)

    # Buttons
    Button(Withdraw_screen, text="Withdraw", font=('Lucida Calligraphy', 13), command=lambda: With_amount(uname)).place(x=300,
                                                                                                                 y=180)
    Button(Withdraw_screen, command=lambda: Bank_login_page.login_confidential(root), image=backicon,
           bg='#000000').place(
        x=830, y=30)
