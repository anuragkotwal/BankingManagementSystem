from tkinter import *
from resources import *
import tkinter.messagebox
import Bank_login_page


def depo_amount(username):
    if amountdepo.get() == "":
        tkinter.messagebox.showerror(Bankname, "Please Enter Amount")
        return
    if float(amountdepo.get()) <= 0:
        tkinter.messagebox.showerror(Bankname, "Account Either have zero Balance or Negative Balance")
        return
    file = open(username, 'r+')
    file_data = file.read()
    data_read = file_data.split('\n')
    curr_bal = data_read[6]
    update_bal = curr_bal
    update_bal = float(update_bal) + float(amountdepo.get())
    data_read[6] = str(update_bal)
    file.seek(0)
    file.truncate(0)
    file.write("\n".join(data_read))
    file.close()
    tkinter.messagebox.showinfo(Bankname, "Balance Updated & Current Balance is: " + str(update_bal))
# deposit
def deposit(uname, root):

    global amountdepo
    global curr_bal
    root.backicon = backicon = PhotoImage(file=BACK)

    amountdepo = StringVar()
    file_obj = open(uname, "r")
    file_obj_data = file_obj.read()
    user_details = file_obj_data.split('\n')
    bal = user_details[6]
    deposit_screen = Frame(root, height=500, width=900, bg=outerframecolor)
    deposit_screen.place(x=0, y=0)
    Inframe = Canvas(deposit_screen, height=WINDOWY - 50, width=WINDOWX - 50, bg=innerframecolor)
    Inframe.place(x=25, y=25)
    # Labels
    Label(deposit_screen, text="Deposit Menu", font=('Courier New', 13)).place(x=385, y=0)
    curr_bal_label = Label(deposit_screen, text="Current Balance: " + bal, font=('Courier New', 13))
    curr_bal_label.place(x=80,y=100)
    Label(deposit_screen, text="Enter Amount to Deposit = ", font=('Courier New', 13), bg=innerframecolor).place(x=80,y=140)
    # Entries
    Entry(deposit_screen, textvariable=amountdepo).place(x=350,y=143)
    # # Buttons
    Button(deposit_screen, text="Deposit to Account", font=('Courier New', 13), command=lambda: depo_amount(uname)).place(x=300, y=180)
    Button(deposit_screen, command=lambda: Bank_login_page.login_confidential(root), image=backicon, bg='#000000').place(
        x=830, y=30)