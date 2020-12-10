from home_page import *
from resources import *

# Main Function
root = Tk()
root.title('Banking Record management System')
positionRight = int((root.winfo_screenwidth()-WINDOWX)/2)
positionDown = int((root.winfo_screenheight()-WINDOWY)/2)
root.geometry('{}x{}+{}+{}'.format(WINDOWX, WINDOWY, positionRight, positionDown))
root.resizable(0, 0)
homepage(root)
root.mainloop()
